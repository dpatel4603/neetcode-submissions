class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        cars = sorted(
            zip(position, speed), key=lambda x: x[0], reverse=True
        )
        # [(4, 2), (1, 3)]


        stack = []

        for car_position, car_speed in cars:

            time = (target - car_position) / car_speed


            if not stack or time > stack[-1]:

                stack.append(time)

        return len(stack)