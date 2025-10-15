class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
    
    def __repr__(self):
        return f"({self.x}, {self.y})\n{self.size}"
    
    def shape(self):
        return "This is a circle"
    
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
    print(c.shape())
    print(c.draw())

main()
