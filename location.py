import config

class Location:
    def __init__(self, name, address, rating, totalRating, type, restaurantPic, photos, price):
        self.name = name
        self.address = address
        self.rating = rating
        self.totalRating = totalRating
        self.restaurantPic = restaurantPic

        self.photos = self.createURL(photos)

        words = type.split('_')
        self.type = words[0].capitalize()

        if price == "PRICE_LEVEL_INEXPENSIVE ":
            self.price = "$"
        elif price == "PRICE_LEVEL_MODERATE":
            self.price = "$$"
        elif price == "PRICE_LEVEL_EXPENSE":
            self.price = "$$$"
        else:
            self.price = "$$$$"


    def createURL(self, photos):
        tmp = []
        for pic in photos:
            url = f"https://places.googleapis.com/v1/{pic}/media?maxHeightPx=400&maxWidthPx=400&key={config.API_KEY}"
            tmp.append(url)
        return tmp
