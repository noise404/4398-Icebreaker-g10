# 3sSgKx00ZdDvrU7QYkiy0SKek4uUjz1HkrFZPP84
import requests


user_request = requests.get("https://courses.ianapplebaum.com/api/user", headers={"Authorization":"Bearer 3sSgKx00ZdDvrU7QYkiy0SKek4uUjz1HkrFZPP84"})

print(user_request.json())
