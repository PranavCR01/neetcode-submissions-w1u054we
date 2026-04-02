class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for star in asteroids:
            while stack and stack[-1] > 0 and star < 0:
                if abs(star) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(star) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(star)
        return stack


              


            
        