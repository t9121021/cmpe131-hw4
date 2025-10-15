class Circle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def __repr__(self):
        return f"({self.x}, {self.y})\n{self.size}"
    
    def draw(self):
        grid_size = 2 * self.size + 1
        grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        
        center = self.size
        
        for row in range(grid_size):
            for col in range(grid_size):
                dx = col - center
                dy = row - center
                distance = (dx * dx + dy * dy) ** 0.5
                
                if abs(distance - self.size) < 0.5:
                    grid[row][col] = ','
        
        result = '\n'.join(''.join(row) for row in grid)
        return result

def main():
    c = Circle(1, 2, 3)
    print(c.__repr__())
    print(c.draw())

main()
