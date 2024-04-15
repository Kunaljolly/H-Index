class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in descending order
        citations.sort(reverse=True)
        n = len(citations)
        h_index = 0

        # Find the maximum h-index
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index
