class Routes():
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for column in range(self.size)] for row in range(self.size)]

    def get(self):
        for x in range(self.size):
            self.grid[x][0] = 1
            self.grid[self.size-1][x] = 1

        for x in range(self.size - 1, -1, -1):
            for y in range(self.size):
                if self.grid[x][y] != 1:
                    self.grid[x][y] = self.grid[x+1][y] + self.grid[x][y-1]

        answer = 0
        
        for x in range(self.size):
            for y in range(self.size):
                if x == 0:
                    answer += self.grid[x][y]
                elif y == self.size - 1:
                    answer += self.grid[x][y]

        answer += self.grid[0][self.size-1] # The for loop doesn't account for this.
        self.fgrid = self.grid
        return answer


for n in range(1, 10):
    r = Routes(n)
    print "%i: %i" % (n, r.get())
