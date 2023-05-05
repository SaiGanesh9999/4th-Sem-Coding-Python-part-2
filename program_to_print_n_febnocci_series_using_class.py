class Fibonacci:
    def _init_(self, n):
        self.n = n
        self.sequence = [0, 1]
        
    def generate_sequence(self):
        for i in range(2, self.n):
            self.sequence.append(self.sequence[i-1] + self.sequence[i-2])
            
    def get_sequence(self):
        return self.sequence[:self.n]

# Example usage:
f = Fibonacci(10)
f.generate_sequence()
print(f.get_sequence())
