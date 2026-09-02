# CSE476 CA1 Project

## 1. Tools:
 This agent uses **add_expense(item, amount, category)** to log purchases in Indian Rupees (₹) while triggering real-time overspend alerts, and **get_summary(category)** to compute total spending, net remaining balance, and usable budget minus savings buffers. A third add-on tool, **set_savings_goal(amount)**, dynamically updates and locks reserved funds.

## 2. Memory & Agentic State:
 The framework maintains a persistent **BUDGET_DATA** dictionary that tracks **financial balances**, **category limits**, and **transaction history** across all turns. When asked complex questions like "Can I afford a ₹30,000 trip?", the agent relies on multi-turn conversational history (conversation_history) to query state tools first rather than hallucinating text responses.

## 3. Honest Failure & Resolution:
 During initial integration, tool execution failed with **BadRequestError** and **NotFoundError** exceptions due to Groq model API updates and incompatible tool-calling specs on specific endpoints (e.g., allam-2-7b and llama-3.3-70b-versatile). I resolved this by adding an automated model resolution block (PREFERRED_TOOL_MODELS) to query active endpoints dynamically and safely fall back to verified function-calling models like llama-3.1-8b-instant.

## Changes

Model Updated to **openai/gpt-oss-120b** from **llama-3.1-8b-instant(EXPIRED MODEL)**
