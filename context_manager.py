from collections import defaultdict

class ContextManager:
    def __init__(self):
        self.contexts = defaultdict(list)

    def add_message(self, user_id: int, role: str, content: str):
        self.contexts[user_id].append({
            "role": role,
            "content": content
        })

    def get_context(self, user_id: int) -> list:
        return self.contexts[user_id]

    def clear_context(self, user_id: int):
        self.contexts[user_id] = []

    def get_context_length(self, user_id: int) -> int:
        return len(self.contexts[user_id])


