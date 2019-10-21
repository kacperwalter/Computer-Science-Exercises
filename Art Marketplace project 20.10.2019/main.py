"""Veneer"""

class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        return "{a}. {b}. {c}, {d}.".format(a=self.artist, b=self.title, c=self.year, d=self.medium)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


girl_with_mandolin = Art("Picasso, Pablo", '"Girl with a Mandolin (Fanny Tellier)"', "Oil on canvas", 1910)
print(girl_with_mandolin)

vaneer = Marketplace()
print(vaneer.show_listings())
