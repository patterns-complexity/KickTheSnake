from src.types import List


def sanitize_whitespace(strings: List[str]) -> List[str]:
    sanitized_servers: List[str] = []
    for server in strings:
        sanitized_servers.append(server.strip())
    return strings
