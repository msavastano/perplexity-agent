from playwright.sync_api import Page, expect
import subprocess
import time
import pytest

@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Starts the flask server in a subprocess."""
    server_process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5) # give server time to start
    yield
    server_process.terminate()
    server_process.wait()

def test_chat_interface(page: Page):
    """
    This test verifies that the chat interface loads correctly,
    sends a message, and displays the "Thinking..." indicator
    followed by the agent's response.
    """
    # 1. Arrange: Go to the chat application homepage.
    try:
        page.goto("http://127.0.0.1:5000")
    except Exception as e:
        pytest.fail(f"Failed to connect to the server: {e}")

    # 2. Assert: Check that the main components are visible.
    expect(page.locator("#chat-container")).to_be_visible()
    expect(page.locator("#user-input")).to_be_visible()
    expect(page.locator("#send-button")).to_be_visible()

    # 3. Act: Type a message and click send.
    user_input = page.locator("#user-input")
    user_input.fill("Hello, world!")
    send_button = page.locator("#send-button")
    send_button.click()

    # 4. Assert: Check for user message and "Thinking..." indicator.
    expect(page.locator(".user-message")).to_have_text("Hello, world!")
    expect(page.locator(".agent-message")).to_contain_text("Thinking...")

    # 5. Assert: Wait for the agent's final response.
    # The response from the mock server can be slow, so we increase the timeout.
    expect(page.locator(".agent-message")).not_to_contain_text("Thinking...", timeout=15000)
    expect(page.locator(".agent-message")).not_to_be_empty()

    # 6. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")