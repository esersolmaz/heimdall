from connectors.base.interface import BaseConnector


class JiraConnector(BaseConnector):
    name = "jira"

    def test_connection(self) -> dict:
        return {"ok": True, "connector": self.name}

    def execute_action(self, action: str, payload: dict) -> dict:
        return {"ok": True, "action": action, "payload": payload}
