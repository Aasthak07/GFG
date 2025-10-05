# User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        total = 0
        is_date_even = (date % 2 == 0)
        
        for c, f in zip(car, fine):
            is_car_even = (c % 2 == 0)
            
            # Collect fine if parity is different
            if is_date_even != is_car_even:
                total += f
                
        return total
