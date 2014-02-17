import sys
import pygame
from pygame.locals import *
import color

WIDTH = 800
HEIGHT = 800

class MathPractice:
    """Main class"""
    """Practicing geometry with pygame - draw graphs, plot points, explore MATH!"""

    def __init__(self, width = WIDTH, height = HEIGHT):

        #initialize settings
        self.background_color = color.WHITE
        self.graph_size = 4
        self.graph_color = color.BLACK
        self.point_color = color.BLUE
        #pause to admire y=mx+b making itself useful for scaling function
        self.point_size = int((-.2 * self.graph_size) + 12)

        #initialize display
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()


        #initialize graph's subsurface
        self.graph = Graph(self.graph_size)
        offset_x = self.width - .9 * self.width
        offset_y = self.height -.9 * self.height
        self.graph_surface = self.background.subsurface(pygame.Rect(offset_x, offset_y, self.width - offset_x*2, self.height - offset_y*2))




    def MainLoop(self):
        """

        @type self: object
        """

        self.graph.add_point(3,1)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        self.graph.toggle_circle()
                    if event.key == K_EQUALS:
                        #TODO bugs out of precise point location when length > 12
                        if self.graph.length < 12:
                            self.resize_graph(2)
                    if event.key == K_MINUS:
                        if self.graph.length > 2:
                            self.resize_graph(-2)
            self.draw_screen()
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()



    def draw_screen(self):

        self.background.fill(self.background_color)

        #Draw the graph on the screen
        origin = (self.graph_surface.get_width()/2, self.graph_surface.get_height()/2 )
        distance = self.graph_surface.get_height() / self.graph.length
        pygame.draw.rect(self.graph_surface, self.graph_color, (0, 0, self.graph_surface.get_width(), self.graph_surface.get_height()), 1)
        for x in range(0, self.graph.length):
            #heavier lines drawn in the middle to indicate x and y axis
            if x == self.graph.length/2:
                pygame.draw.line(self.graph_surface, self.graph_color, [x * distance,0], [x * distance,self.graph_surface.get_width()], 5 )
                pygame.draw.line(self.graph_surface, self.graph_color, [0, distance * x], [self.graph_surface.get_height(), x * distance], 5)
            else:
                pygame.draw.line(self.graph_surface, self.graph_color, [x * distance,0], [x * distance,self.graph_surface.get_width()] )
                pygame.draw.line(self.graph_surface, self.graph_color, [0, distance * x], [self.graph_surface.get_height(), x * distance])

        #draw an enveloping circle if necessary
        if self.graph.env_circle:
            pygame.draw.circle(self.graph_surface, self.graph_color, origin, self.graph_surface.get_height() / 2, 1)


        #draw points on the graph
        for point in self.graph.point_list:
            pygame.draw.circle(self.graph_surface, self.point_color, (int(origin[0] + point.x_coord * distance),int(origin[1] - point.y_coord * distance)), self.point_size)


    def resize_graph(self, length):
        self.graph.length += length
        self.point_size = int((-.2 * self.graph.length) + 12)

class Graph:
    """Maintains the graph state"""

    def __init__(self, length = 10, env_circle = False):
        """Initialize square graph with integer value of length - 0,0 will be at the center of the square"""
        """The length of the graph must be an even integer greater than 1"""
        if length < 2 or length % 2 == 1:
            raise ValueError("Length of the graph must be an even number integer greater than 1")
        self.length = length
        self.point_list = []

        self.env_circle = env_circle

    def get_location(self, x, y):
        """Receives x and y coordinates of a grid.  Returns the coordinates of the location on the screen.
           Assumes grid fills its surface completely """

    def add_point(self, x, y):
        point = Point(x, y)
        self.point_list.append(point)

    def toggle_circle(self):
        if self.env_circle:
            self.env_circle = False
        else:
            self.env_circle = True


class Point:
    """A point on the graph"""
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.loc = (self.x_coord, self.y_coord)



if __name__ == "__main__":
    MainWindow = MathPractice()
    MainWindow.MainLoop()
