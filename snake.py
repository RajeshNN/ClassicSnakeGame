class snake:
    def __init__(self):
        self.snake_coor = [[20,40], [21,40], [22,40], [22,41], [22,42]]
        self.snake_coor_dict= {'20,40':[20,40], '21,40':[21,40],
                               '22,40':[22,40], '22,41':[22,41],
                               '22,42':[22,42]}
        self.length = 5
        self.head_dir = b'w'
        self.eaten = 0
        self.body_chewed = 0

    def move_snake(self):
        x = self.snake_coor[0].copy()
        if self.head_dir==b'w' or self.head_dir=='w':
            x[0]-=1
            if x[0]<0:
                x[0]=30
        elif self.head_dir==b's' or self.head_dir=='s':
            x[0]+=1
            if x[0]>30:
                x[0]=0
        elif self.head_dir==b'a' or self.head_dir=='a':
            x[1]-=1
            if x[1]<0:
                x[1]=80
        elif self.head_dir==b'd' or self.head_dir=='d':
            x[1]+=1
            if x[1]>80:
                x[1]=0
        try:
            if self.snake_coor_dict[str(x[0])+','+str(x[1])]:
                self.body_chewed = 1
        except:
            self.snake_coor.insert(0, x)
            self.snake_coor_dict[str(x[0])+','+str(x[1])] = x
            if not self.eaten:
                e = self.snake_coor.pop()
                del self.snake_coor_dict[str(e[0])+','+str(e[1])]
