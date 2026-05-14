from connectors.jira.connector import JiraConnector
from connectors.slack.connector import SlackConnector

_CONNECTORS = {
    "slack": SlackConnector(),
    "jira": JiraConnector(),
}


def get_connector(name: str):
    return _CONNECTORS.get(name)
