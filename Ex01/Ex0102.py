"""Min Max and Avg value"""

import json
def highlow(new):

    """Spam"""

    avg = sum(new)/len(new)
    low1 = new[0]
    height = 0
    for i in new:
        if i > height:
            height = i
    for j in new:
        if j < low1:
            low1 = j

    return (round(height, 2), round(low1, 2), round(avg, 2))

print(highlow(json.loads(input())))
