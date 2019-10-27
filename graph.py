


class Point:
    def __init__(self, x=0, y=0, plot=False):
        self.__x = x
        self.__y = y

        # The point is on the graph
        self.__plot = plot

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.__y = value

    def flip_plot(self):
        """ Flip plot value to True """
        if not self.__plot:
            self.__plot = not self.__plot

    def get_plot(self):
        return self.__plot

    def move_delta(self, deltax, deltay):
        self.x = self.__x + deltax
        self.y = self.__y + deltay


sample = [
    [Point(-1, 1), Point(0, 1), Point(1, 1)],
    [Point(-1, 0), Point(0, 0), Point(1, 0)],
    [Point(-1, -1), Point(0, -1), Point(1, -1)],
] # type: List[List[Point]]

class Graph:
    def __init__(self, rows=5, cols=5):
        if isinstance(rows, int):
            self.__rows = rows
            self.__rows = fix_even(self.__rows)
        if isinstance(cols, int):
            self.__cols = cols
            self.__cols = fix_even(self.__cols)

        self.__graph = []
        self.__current_plots = self.get_current_plots()

        self.__generate()



    def __generate(self):
        """
        Each List encountered in graph represents a row.
        Row = [Point, Point, Point]
        Row = [Point, Point, Point]
        ...

        Iterate over number of rows     (y value, set for each point)
        Iterate over numbers of cols    (x value, set for each point)
        """
        if self.__rows is None or self.__cols is None:
            print("Warning: rows or cols is None.")
            return

        for y in range(-(self.__rows), (self.__rows+1)):
            tmp = []
            for x in range(-self.__cols, (self.__cols+1)):
                p = Point(x=x, y=y)
                tmp.append(p)

            self.__graph.append(tmp)

    def draw(self):
        """ Print, for now """
        part = "[{}]"
        line = ""
        lines = [] # Store to print in reverse order

        for row in self.__graph:
            line = ""
            for point in row:
                # Uncomment for debugging point locations
                # line += part.format(point.x, point.y)
                line += part.format("o" if point.get_plot() else " ")

            # print(line)
            lines.append(line)

        for line in reversed(lines):
            print(line)

    def plot(self, x, y):
        point = self.__search_point(x, y)

        print("Point plotted: ({}, {})".format(x, y))
        point.flip_plot()

    def __search_point(self, x, y) -> "Point":
        """
        :returns: the point at position given
        :rtype: Point
        """
        for row in self.__graph:
            for point in row:
                if point.x == x and point.y == y:
                    return point

    def __move_plots(self, deltax, deltay) -> bool:
        """
        :returns: Whether a move happened to a point
        :rtype: bool
        """
        for row in self.__graph:
            for point in row:
                if point.get_plot():
                    point.move_delta(deltax, deltay)
                    return True

        return False

    def get_current_plots(self) -> "List[Point]":
        """ Return an unordered list of plotted points """
        plots = []

        for row in self.__graph:
            for point in row:
                if point.get_plot():
                    print(point.x, point.y)
                    plots.append(point)

        return plots

    def transform(self, deltax=0, deltay=0, eq=""):
        while self.__move_plots(deltax, deltay):
            pass

def fix_even(value):
    """
    Graphs always have odd rows and columns.
    """
    if value % 2 == 0:
        return value + 1
    else:
        return value

def main():
    graph = Graph(rows=3, cols=3)

    for i in range(2):
        graph.plot(0, i+1)

    graph.transform(deltax=2, deltay=2)
    graph.draw()

if __name__ == "__main__":
    main()
