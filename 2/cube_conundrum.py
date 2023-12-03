from data_parser import DataParser

import colour

cubes_in_bag = {colour.Colour.RED: 12, colour.Colour.GREEN: 13, colour.Colour.BLUE: 14}


def sum_possible_games(data):
    sum_of_games = 0
    for game in data.games:
        game_possible = True
        for reveal in game.reveals:
            for key, value in cubes_in_bag.items():
                if reveal.cubes.get(key, 0) > value:
                    game_possible = False
                    break
            if not game_possible:
                break
        if game_possible:
            sum_of_games += game.game_number
    return sum_of_games


def power_of_cubes(data):
    sum_of_powers = 0

    for game in data.games:
        minimum_of_colour = {}
        for reveal in game.reveals:
            for key, value in reveal.cubes.items():
                if minimum_of_colour.get(key, 0) < value:
                    minimum_of_colour[key] = value
        product_of_colours = 1
        for colour_enum in colour.Colour:
            product_of_colours *= minimum_of_colour.get(colour_enum, 0)
        sum_of_powers += product_of_colours
    return sum_of_powers


def main():
    data_parser = DataParser("star1.dat")
    data = data_parser.parse_data()
    print(sum_possible_games(data))
    print(power_of_cubes(data))


if __name__ == "__main__":
    main()
