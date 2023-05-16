# # ABC is a right triangle, 90° at B.
# Therefore, <ABC = 90°
# Point M is the midpoint of hypotenuse AC.
# You are given the lengths AB and BC.
# Your task is to find <M BC (angle 0°
# , as shown in the figure
# degrees.
# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.
# Constraints
# • 0 < AB < 100
# • 0 < BC < 100
# • Lengths AB and BC are natural numbers.
# Output Format
# Output < MBC in degrees.
# Note: Round the angle to the nearest integer.
# Examples:
# If angle is 56.5000001°, then output 57°.


from math import atan2, acos, degrees, isclose

a_len = int(input())
b_len = int(input())

print(str(int(round(degrees(atan2(a_len, b_len))))) + '\u00B0'.encode('utf-8').decode('utf-8'))
# find the arctangent of length_a / length_b in radians, as degrees, rounded to whole as integer, concat this with degrees symbol, in utf-8, encoded then decoded, to permit string concat. 





