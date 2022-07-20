class Band:
    def __init__(self, name):
        self.name = name
        self.attribute_albums = []

    def add_album(self, album):
        if album in self.attribute_albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.attribute_albums.append(album.name)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name, album):
        if album_name not in self.attribute_albums:
            return f"Album {album_name} is not found."
        if album.published:
            return "Album has been published. It cannot be removed."
        self.attribute_albums.remove(album_name)

    def details(self,album):
        result = f'Band{self.name}\n'
        for album in self.attribute_albums:
            result += album.details() + '\n'
        return result.strip()