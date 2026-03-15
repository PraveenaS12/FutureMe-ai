import pandas as pd
import random

data = []

for i in range(1000):

    sleep = random.randint(3,9)
    study = random.randint(0,6)
    screen = random.randint(1,10)
    exercise = random.randint(0,3)
    stress = random.randint(1,10)

    focus = (
        sleep*8 +
        study*6 -
        screen*4 +
        exercise*5 -
        stress*3
    )

    energy = (
        sleep*9 -
        stress*4 +
        exercise*6
    )

    productivity = (
        study*10 +
        sleep*5 -
        stress*4
    )

    burnout = (
        stress*8 +
        screen*3 -
        sleep*4
    )

    data.append([
        sleep,
        study,
        screen,
        exercise,
        stress,
        focus,
        energy,
        productivity,
        burnout
    ])

df = pd.DataFrame(data,columns=[

"sleep",
"study",
"screen",
"exercise",
"stress",

"focus",
"energy",
"productivity",
"burnout"

])

df.to_csv("model/dataset.csv",index=False)

print("Dataset Created!")