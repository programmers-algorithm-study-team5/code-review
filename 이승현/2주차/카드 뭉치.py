def solution(cards1, cards2, goal):
    cards1, cards2 = cards1[::-1], cards2[::-1]
    for g in goal:
        if cards1 and g == cards1[-1] : cards1.pop()
        elif cards2 and g == cards2[-1] : cards2.pop()
        else : return 'No'
    return 'Yes'