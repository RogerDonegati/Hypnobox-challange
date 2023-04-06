
# o(n²)
def footbal_scores(TeamA, teamB):
    result = []
    teamA.sort()

    # o(n²)
    for valueB in teamB:
        cont = 0
        for valueA in teamA:
            if valueB >= valueA:
                cont += 1
        result.append(cont)


    # for i in reversed(range(len(teamA))):
    #     if teamA[i] <= teamB[j]:
    #         result.append(i +1)
    #         j -= 1

    #     if j < 0:
    #         return result

    # while j >= 0:
    #     result.append(i)
    #     j -= 1

    return result


teamA = [2, 10, 5, 4, 8]
teamB = [3, 1, 7, 8]
print(footbal_scores(teamA, teamB))
