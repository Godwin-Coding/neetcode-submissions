class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return f"{strs}"
        return "-".join(strs)
    def decode(self, s: str) -> List[str]:
        if not s:
            return [s]
        elif s == "[]":
            return []
        return s.split("-")
