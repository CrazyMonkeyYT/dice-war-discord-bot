import random as r

def war(oneElite, oneNorm, twoElite, twoNorm):
    
    score = 0
    army  = (oneElite * 1.33) + one
    for i in oneElite:
        score += r.randint(0,6)
    for i in oneNorm:
        score += r.randint(0,4)
    for i in twoElite:
        score -= r.randint(0,6)
    for i in twoNorm:
        score -= r.randint(0,4)
    if score == 0:
        return ("tie")
    elif score > 0:
        return ('team 1 wins')
    else: #score < 0
        return ('team 2 wins')
