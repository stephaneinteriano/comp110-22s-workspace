
def favorite_color(rainbow: dict[str, str]) -> str:
    """Finding out which is the most popular color."""
    paint: dict[str, int] = {}
    for key in rainbow: 
        color: str = rainbow[key]
        if color in paint:
            paint[color] += 1
        else:
            paint[color] = 1
    limit: int = 0 
    most_popular: str = ""
    for color in paint:
        if paint[color] > limit:
            limit = paint[color]
            most_popular = color
    return most_popular
