(function () {
	"use strict";

	// Za produkciju zameniti sa produkcionim API URL-om.
	const API_URL = window.PIT_CONFIG?.API_URL || "http://127.0.0.1:8000/chat";
	const STREAM_API_URL = window.PIT_CONFIG?.STREAM_API_URL || API_URL.replace(/\/chat\/?$/, "/chat/stream");
	const CONVERSATION_KEY = "pitNavigatorConversationId";
	const MESSAGES_KEY = "pitNavigatorMessages";
	const MAX_HISTORY_MESSAGES = 6;
	const MAX_STORED_MESSAGES = 50;
	const STARTER_MESSAGE = "Zdravo, ja sam PIT Navigator. Postavite pitanje o PIT modulu, predmetima, izbornim korpama ili karijernim putanjama.";
	const API_ERROR_MESSAGE = "Greška u komunikaciji. Nismo mogli da dohvatimo odgovor. Proverite da li je PIT Navigator API pokrenut i pokušajte ponovo.";
	const NEW_CHAT_CONFIRM = "Da li ste sigurni da želite da započnete novi razgovor? Trenutni razgovor će biti obrisan iz ovog browsera.";

	const messagesEl = document.getElementById("pitMessages");
	const questionEl = document.getElementById("pitQuestion");
	const sendButton = document.getElementById("pitSend");
	const newButton = document.getElementById("pitNew");
	const statusEl = document.getElementById("pitStatus");
	const chips = document.querySelectorAll(".pit-chip");

	function createConversationId() {
		if (window.crypto && typeof window.crypto.randomUUID === "function") {
			return window.crypto.randomUUID();
		}
		return "conv-" + Date.now() + "-" + Math.random().toString(16).slice(2);
	}

	function getConversationId() {
		let conversationId = localStorage.getItem(CONVERSATION_KEY);
		if (!conversationId) {
			conversationId = createConversationId();
			localStorage.setItem(CONVERSATION_KEY, conversationId);
		}
		return conversationId;
	}

	function loadMessages() {
		try {
			const parsed = JSON.parse(localStorage.getItem(MESSAGES_KEY) || "[]");
			return Array.isArray(parsed) ? parsed : [];
		} catch (error) {
			return [];
		}
	}

	function saveMessages(messages) {
		const cappedMessages = messages.slice(-MAX_STORED_MESSAGES);
		localStorage.setItem(MESSAGES_KEY, JSON.stringify(cappedMessages));
	}

	function addStoredMessage(role, content) {
		const messages = loadMessages();
		messages.push({ role: role, content: content });
		saveMessages(messages);
	}

	function escapeHtml(value) {
		return String(value || "")
			.replace(/&/g, "&amp;")
			.replace(/</g, "&lt;")
			.replace(/>/g, "&gt;")
			.replace(/"/g, "&quot;")
			.replace(/'/g, "&#039;");
	}

	function renderInlineMarkdown(value) {
		return value.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
	}

	function renderMarkdown(value) {
		const escapedLines = escapeHtml(value).split(/\r?\n/);
		const parts = [];
		let listItems = [];
		let paragraphLines = [];

		function flushParagraph() {
			if (paragraphLines.length === 0) {
				return;
			}
			parts.push("<p>" + renderInlineMarkdown(paragraphLines.join("<br>")) + "</p>");
			paragraphLines = [];
		}

		function flushList() {
			if (listItems.length === 0) {
				return;
			}
			parts.push(
				"<ul>" +
				listItems.map(function (item) {
					return "<li>" + renderInlineMarkdown(item) + "</li>";
				}).join("") +
				"</ul>"
			);
			listItems = [];
		}

		escapedLines.forEach(function (line) {
			const bulletMatch = line.match(/^\s*(?:\*|-)\s+(.+)$/);
			if (bulletMatch) {
				flushParagraph();
				listItems.push(bulletMatch[1]);
				return;
			}

			flushList();
			if (line.trim() === "") {
				flushParagraph();
				return;
			}
			paragraphLines.push(line);
		});

		flushParagraph();
		flushList();
		return parts.join("");
	}

	function readableSourceLabel(source) {
		const path = String(source || "");
		const labelMap = {
			"pit_data_ai_bi_korpa": "Data / AI / BI korpa",
			"pit_software_erp_digital_korpa": "Software / ERP / digital korpa",
			"pit_finance_analytics_korpa": "Finance analytics korpa",
			"pit_izborne_korpe_overview": "Izborne korpe",
			"pit_minor_electives_reference": "Izborni predmeti, referenca",
			"poslovna_analitika": "Poslovna analitika",
			"poslovna_inteligencija": "Poslovna inteligencija",
			"erp_softver": "ERP softver",
			"razvoj_softvera": "Razvoj softvera",
			"masinsko_ucenje": "Mašinsko učenje",
			"analiza_podataka": "Analiza podataka",
			"baze_podataka": "Baze podataka",
			"pin_2020_vs_pit_2027": "PIN 2020 vs PIT 2027",
			"pit_navigator_answering_policy": "Pravila odgovaranja"
		};
		const withoutKnownPrefix = path.replace(
			/^(?:03_course_plans\/[0-9_]+\/|04_baskets\/[0-9_]+\/)/,
			""
		);
		const lastPart = withoutKnownPrefix.split(/[\\/]/).pop() || withoutKnownPrefix;
		const slug = lastPart.replace(/\.md$/i, "");
		return labelMap[slug] || slug.replace(/[_-]+/g, " ").trim() || path;
	}

	function filterDisplaySources(sources) {
		if (!Array.isArray(sources) || sources.length === 0) {
			return [];
		}

		const publicFacingSources = sources.filter(function (source) {
			const path = String(source || "");
			return !(
				path.includes("00_project_rules") ||
				path.includes("knowledge_base_index") ||
				path.includes("knowledge_base_changelog") ||
				path.includes("05_retrieval_guides/")
			);
		});
		return publicFacingSources.length > 0 ? publicFacingSources : sources;
	}

	function appendSources(sources) {
		return;
	}

	function appendMessage(role, content, sources) {
		const row = document.createElement("div");
		row.className = "pit-message-row " + role;
		row.setAttribute("data-label", role === "user" ? "Vi" : role === "assistant" ? "PIT Navigator" : "Greška");

		const bubble = document.createElement("div");
		bubble.className = "pit-message " + role;
		if (role === "assistant") {
			bubble.innerHTML = renderMarkdown(content);
		} else {
			bubble.textContent = content;
		}
		row.appendChild(bubble);
		messagesEl.appendChild(row);

		if (role === "assistant") {
			appendSources(sources);
		}

		messagesEl.scrollTop = messagesEl.scrollHeight;
		return row;
	}

	function appendErrorMessage(content) {
		return appendMessage("error", content, []);
	}

	function appendTypingPlaceholder() {
		const row = document.createElement("div");
		row.className = "pit-message-row assistant";
		row.setAttribute("data-label", "PIT Navigator");

		const bubble = document.createElement("div");
		bubble.className = "pit-message assistant";
		bubble.setAttribute("aria-label", "PIT Navigator priprema odgovor");
		bubble.innerHTML = "<span class=\"pit-loading-text\">PIT Navigator priprema odgovor</span><span class=\"pit-typing\"><span></span><span></span><span></span></span>";
		row.appendChild(bubble);
		messagesEl.appendChild(row);
		messagesEl.scrollTop = messagesEl.scrollHeight;

		return { row: row, bubble: bubble };
	}

	function replaceTypingPlaceholder(placeholder, answer, sources) {
		if (!placeholder || !placeholder.bubble) {
			appendMessage("assistant", answer, sources);
			return;
		}
		placeholder.bubble.innerHTML = renderMarkdown(answer);
		appendSources(sources);
		messagesEl.scrollTop = messagesEl.scrollHeight;
	}

	function updateTypingPlaceholder(placeholder, answer) {
		if (!placeholder || !placeholder.bubble) {
			return;
		}
		placeholder.bubble.removeAttribute("aria-label");
		placeholder.bubble.innerHTML = renderMarkdown(answer || "");
		messagesEl.scrollTop = messagesEl.scrollHeight;
	}

	function removeTypingPlaceholder(placeholder) {
		if (placeholder && placeholder.row && placeholder.row.parentNode) {
			placeholder.row.parentNode.removeChild(placeholder.row);
		}
	}

	function renderConversation() {
		const storedMessages = loadMessages();
		messagesEl.innerHTML = "";

		if (storedMessages.length === 0) {
			appendMessage("assistant", STARTER_MESSAGE, []);
			questionEl.focus();
			return;
		}

		storedMessages.forEach(function (message) {
			if (message && (message.role === "user" || message.role === "assistant") && message.content) {
				appendMessage(message.role, message.content, []);
			}
		});
		messagesEl.scrollTop = messagesEl.scrollHeight;
	}

	function setBusy(isBusy) {
		sendButton.disabled = isBusy;
		questionEl.disabled = isBusy;
		statusEl.textContent = isBusy ? "PIT Navigator priprema odgovor..." : "";
	}

	function parseSseChunk(buffer, onEvent) {
		const events = buffer.split(/\r?\n\r?\n/);
		const rest = events.pop() || "";

		events.forEach(function (rawEvent) {
			let eventName = "message";
			const dataLines = [];
			rawEvent.split(/\r?\n/).forEach(function (line) {
				if (line.startsWith("event:")) {
					eventName = line.slice(6).trim();
					return;
				}
				if (line.startsWith("data:")) {
					dataLines.push(line.slice(5).trimStart());
				}
			});
			if (dataLines.length === 0) {
				return;
			}
			try {
				onEvent(eventName, JSON.parse(dataLines.join("\n")));
			} catch (error) {
				onEvent("error", {});
			}
		});

		return rest;
	}

	async function fetchJsonAnswer(payload) {
		const response = await fetch(API_URL, {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify(payload)
		});

		if (!response.ok) {
			throw new Error("API error");
		}

		return response.json();
	}

	async function streamAnswer(payload, placeholder) {
		const response = await fetch(STREAM_API_URL, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "text/event-stream"
			},
			body: JSON.stringify(payload)
		});

		if (!response.ok || !response.body) {
			throw new Error("Streaming API error");
		}

		const reader = response.body.getReader();
		const decoder = new TextDecoder();
		let buffer = "";
		let streamedAnswer = "";
		let finalData = null;

		function handleEvent(eventName, data) {
			if (eventName === "meta" && data.conversation_id) {
				localStorage.setItem(CONVERSATION_KEY, data.conversation_id);
				return;
			}
			if (eventName === "token") {
				streamedAnswer += data.text || "";
				updateTypingPlaceholder(placeholder, streamedAnswer);
				return;
			}
			if (eventName === "final") {
				finalData = data;
				if (data.conversation_id) {
					localStorage.setItem(CONVERSATION_KEY, data.conversation_id);
				}
				return;
			}
			if (eventName === "error") {
				throw new Error("Streaming event error");
			}
		}

		while (true) {
			const readResult = await reader.read();
			if (readResult.done) {
				break;
			}
			buffer += decoder.decode(readResult.value, { stream: true });
			buffer = parseSseChunk(buffer, handleEvent);
		}
		buffer += decoder.decode();
		if (buffer.trim()) {
			parseSseChunk(buffer + "\n\n", handleEvent);
		}

		if (!finalData) {
			throw new Error("Missing final streaming event");
		}

		return finalData;
	}

	async function sendQuestion() {
		const question = questionEl.value.trim();
		if (!question || sendButton.disabled) {
			return;
		}

		const conversationId = getConversationId();
		const historyBeforeQuestion = loadMessages().slice(-MAX_HISTORY_MESSAGES);

		appendMessage("user", question, []);
		addStoredMessage("user", question);
		questionEl.value = "";
		setBusy(true);
		const typingPlaceholder = appendTypingPlaceholder();
		const payload = {
			conversation_id: conversationId,
			question: question,
			history: historyBeforeQuestion
		};

		try {
			let data;
			try {
				data = await streamAnswer(payload, typingPlaceholder);
			} catch (streamError) {
				data = await fetchJsonAnswer(payload);
			}
			if (data.conversation_id) {
				localStorage.setItem(CONVERSATION_KEY, data.conversation_id);
			}

			const answer = data.answer || API_ERROR_MESSAGE;
			replaceTypingPlaceholder(typingPlaceholder, answer, data.sources || []);
			addStoredMessage("assistant", answer);
		} catch (error) {
			removeTypingPlaceholder(typingPlaceholder);
			appendErrorMessage(API_ERROR_MESSAGE);
			questionEl.value = question;
		} finally {
			setBusy(false);
			questionEl.focus();
		}
	}

	function startNewConversation() {
		if (!window.confirm(NEW_CHAT_CONFIRM)) {
			return;
		}

		localStorage.removeItem(CONVERSATION_KEY);
		localStorage.removeItem(MESSAGES_KEY);
		questionEl.value = "";
		renderConversation();
		statusEl.textContent = "Započet je novi razgovor.";
		setTimeout(function () {
			statusEl.textContent = "";
		}, 2200);
		questionEl.focus();
	}

	sendButton.addEventListener("click", sendQuestion);
	newButton.addEventListener("click", startNewConversation);

	questionEl.addEventListener("keydown", function (event) {
		if (event.key === "Enter" && !event.shiftKey) {
			event.preventDefault();
			sendQuestion();
		}
	});

	chips.forEach(function (chip) {
		chip.addEventListener("click", function () {
			questionEl.value = chip.textContent;
			questionEl.focus();
		});
	});

	getConversationId();
	renderConversation();
})();
