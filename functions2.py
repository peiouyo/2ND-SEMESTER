def s_score(s1, s2, s3):
    return (s1 + s2 + s3) / 3

avg = s_score(
    float(input("Score 1: ")),
    float(input("Score 2: ")),
    float(input("Score 3: "))
)

print("Average:", avg)

if avg >= 90:
    print("Excellent")
elif avg >= 75:
    print("Good")
else:
    print("Needs Improvement")