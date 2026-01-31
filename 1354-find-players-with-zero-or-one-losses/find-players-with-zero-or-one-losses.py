class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}

        for i in range(len(matches)):
            if matches[i][0] not in winners:
                winners[matches[i][0]] = 1
            else:
                winners[matches[i][0]] += 1

            if matches[i][1] not in losers:
                losers[matches[i][1]] = 1
            else:
                losers[matches[i][1]] += 1

        undeafted = []
        for player, won_matches in winners.items():
            if player not in losers:
                undeafted.append(player)
        undeafted.sort()

        defeated_once = []
        for player, lost_match in losers.items():
            if lost_match == 1:
                defeated_once.append(player)
        defeated_once.sort()

        return [undeafted ,defeated_once]