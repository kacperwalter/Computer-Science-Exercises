"""Veneer"""

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{a}. {b}. {c}, {d}, {e}, {f}".format(a=self.artist, b=self.title, c=self.year, d=self.medium, e=self.owner.name, f=self.owner.location)


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


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum


"""Marketplace instantion"""
vaneer = Marketplace()

"""Clients instantion"""
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)

"""Artpiece instantion"""
girl_with_mandolin = Art("Picasso, Pablo", '"Girl with a Mandolin (Fanny Tellier)"', "Oil on canvas", 1910, edytta)
print(girl_with_mandolin)


