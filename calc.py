import pulp as p

Lp_prob = p.LpProblem('cayo-prof', p.LpMaximize)

# All values are in thousand $
VALUE = {   
            "CASH": 87,
            "WEED": 148,
            "COCAINE": 220,
            "PAINTING": 190,
            "GOLD": 332
        }

AVAILABLE = {
            "CASH": 2,
            "WEED": 2,
            "COCAINE": 0,
            "PAINTING": 1,
            "GOLD": 2
        }

WEIGHT = {
            "CASH": 25,
            "WEED": 33,
            "COCAINE": 50,
            "PAINTING": 50,
            "GOLD": 66
        }

PEOPLE = 2

a = p.LpVariable("a", lowBound = 0)
c = p.LpVariable("c", lowBound = 0)
w = p.LpVariable("w", lowBound = 0)
d = p.LpVariable("d", lowBound = 0)
g = p.LpVariable("g", lowBound = 0)

Lp_prob += VALUE["CASH"] * d + VALUE["WEED"] * w + VALUE["COCAINE"] * c + VALUE["PAINTING"] * a + VALUE["GOLD"] * g

Lp_prob += d <= AVAILABLE["CASH"]
Lp_prob += w <= AVAILABLE["WEED"]
Lp_prob += c <= AVAILABLE["COCAINE"]
Lp_prob += a <= AVAILABLE["PAINTING"]
Lp_prob += g <= AVAILABLE["GOLD"]
Lp_prob += WEIGHT["CASH"]*d + WEIGHT["WEED"]*w + WEIGHT["COCAINE"]*c + WEIGHT["PAINTING"]*a + WEIGHT["GOLD"]*g  <= PEOPLE*100

#print(Lp_prob)
status = Lp_prob.solve()
#print(p.value(d), p.value(w), p.value(c), p.value(a), p.value(g), p.value(Lp_prob.objective))

print("CASH: ", p.value(d))
print("WEED: ", p.value(w))
print("COCAINE: ", p.value(c))
print("PAINTING: ", p.value(a))
print("GOLD: ", p.value(g))
print("MAX PROFIT: ", p.value(Lp_prob.objective))
