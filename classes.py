"""Classes for climbing competitions"""

TRY_WEIGHTS = [1, 0.9, 0.8]


class Group:
    """an age-based group"""

    id: int
    name: str
    routes: list

    def __init__(self, group_id: int, name: str) -> None:
        if not isinstance(group_id, int):
            raise TypeError("'group_id' should be an integer")
        self.id = group_id
        self.name = name

    def __repr__(self) -> str:
        return f"'Gruppe {self.id} - {self.name}'"

    def __hash__(self) -> int:
        return hash(self.id)

    def set_routes(self, routes: list) -> None:
        """assigns routes from a list of all routes"""
        self.routes = []
        for route in routes:
            if self in route.groups:
                self.routes.append(route)


class Route:
    """describes a climbing route"""

    id: int
    color: str
    handholds: int
    groups: list
    creator: str

    def __init__(
        self, route_id: int, color: str, handholds: int, groups: list, creator: str
    ) -> None:
        if not isinstance(route_id, int):
            raise TypeError("'route_id' should be an integer.")
        self.id = route_id
        self.color = color
        self.handholds = handholds
        for group in groups:
            if not isinstance(group, Group):
                raise TypeError("'groups' should be a list of 'Group' objects.")
        self.groups = groups.copy()
        self.creator = creator

    def __repr__(self) -> str:
        return f"Route{self.id}"

    def __hash__(self) -> int:
        return hash(self.id)


class Participant:
    """person who climbs routes"""

    name: str
    group: Group
    rank: int
    points: dict  # Route: list of points
    result: float  # a score between 0 and 100

    def __init__(self, name: str, group: Group, rank: int = 0, points: dict = None) -> None:
        if not isinstance(group, Group):
            raise TypeError("'group' should be a Group object.")
        self.name = name
        self.group = group
        self.rank = rank
        self.points = {}
        if points:
            for route, values in points.items():
                self.insert_points(route, values)
        else:
            for route in group.routes:
                self.insert_points(route, [0, 0, 0])
        self.compute_result()

    def __repr__(self) -> str:
        return f"{self.name}({self.group.name})"

    def to_dict(self) -> dict:
        """returns this participant as a dictionary"""
        return {
            "name": self.name,
            "group": self.group.id,
            "rank": self.rank,
            "points": {route.id: points for route, points in self.points.items()},
        }

    def insert_points(self, route: Route, points: list) -> None:
        """
        insert how many points the participant has scored for the given route

        Args:
            route_id: id of the route
            points: scored points for each try

        Raises:
            ValueError: if the participant should not climb this route
            ValueError: if the participant has more than max points
        """
        if self.group not in route.groups:
            raise ValueError(f"'{route}' ist nicht gedacht für '{self}'")
        for value in points:
            if value > route.handholds:
                raise ValueError(f"'{self}' kann nicht {value} Griffe bei '{route}' haben.")
        self.points[route] = points.copy()

    def compute_result(self) -> float:
        """
        computes the total points of the participant

        Returns:
            total points
        """
        self.result = sum(
            max(value * weight for value, weight in zip(points, TRY_WEIGHTS))
            / route.handholds
            for route, points in self.points.items()
        ) * (100 / len(self.group.routes))
        return self.result
