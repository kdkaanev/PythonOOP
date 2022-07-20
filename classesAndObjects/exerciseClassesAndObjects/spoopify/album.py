class Album:
    def __init__(self, name,*song):
        self.name = name
        self.songs = song
        self.published = False
        self.songs = []

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song.name in self.songs:
            return "Song is already in the album."
        self.songs.append(song.name)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song_name)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}/n'
        for songs in self.songs:
            result += f'== {song.get_info()}/n'
        return result.strip()

