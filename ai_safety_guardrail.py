import time

# This script demonstrates a simple AI automation safety guardrail.
# The core concept is to implement a 'maximum execution time' or 'safe operation window'
# to prevent runaway AI processes that could lead to unintended consequences.

class AISystem:
    def __init__(self, name):
        self.name = name
        self.is_running = False
        self.start_time = None

    def start_task(self, max_duration_seconds):
        if self.is_running:
            print(f"[{self.name}] Task already running.")
            return

        print(f"[{self.name}] Starting task. Max duration: {max_duration_seconds} seconds.")
        self.is_running = True
        self.start_time = time.time()
        self.max_duration = max_duration_seconds

    def perform_operation(self):
        if not self.is_running:
            print(f"[{self.name}] No task running.")
            return

        # --- Safety Guardrail Check --- 
        # This is the core of the guardrail: check if the operation has exceeded the allowed time.
        elapsed_time = time.time() - self.start_time
        if elapsed_time > self.max_duration:
            print(f"[{self.name}] !!! SAFETY GUARDRAIL TRIGGERED !!! Maximum duration ({self.max_duration}s) exceeded. Stopping task.")
            self.stop_task()
            return
        # --- End Safety Guardrail Check ---

        # Simulate some AI operation
        print(f"[{self.name}] Performing operation... (Elapsed: {elapsed_time:.2f}s)")
        # In a real AI, this would be complex computation, decision making, etc.
        time.sleep(0.5) # Simulate work

    def stop_task(self):
        if not self.is_running:
            return
        print(f"[{self.name}] Task stopped.")
        self.is_running = False
        self.start_time = None
        self.max_duration = None

# --- Example Usage ---

# Create an AI system with a safety limit of 5 seconds
financial_bot = AISystem("FinancialBot")
financial_bot.start_task(max_duration_seconds=5)

# Simulate the bot running for a bit longer than allowed
for _ in range(12):
    financial_bot.perform_operation()
    # If the guardrail is not in place, this loop would continue indefinitely or until an error.

# Try to start another task after the first one was stopped by the guardrail
print("\nAttempting to restart the bot...")
financial_bot.start_task(max_duration_seconds=3)
for _ in range(5):
    financial_bot.perform_operation()

# Example of a system that finishes within its limit
autonomous_vehicle_ai = AISystem("AutonomousVehicleAI")
autonomous_vehicle_ai.start_task(max_duration_seconds=10)
for _ in range(8):
    autonomous_vehicle_ai.perform_operation()
autonomous_vehicle_ai.stop_task() # Manually stop if done early
