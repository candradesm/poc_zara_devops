import random

for x in range(30, 480, 16):
    print(f'<text x="{x}" y="270" alignment-baseline="middle" font-size="8" fill="white" text-anchor="end" transform="rotate(-90 {x} 270)">25/05/2023</text>')

for x in range(30, 480, 20):
        y = random.randint(25, 250)
        print(f'<circle cx="{x}" cy="{y}" r="4" fill="#1b85b8" />')