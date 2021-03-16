class Codec:
    codes, urls = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        code = ''.join(random.choice(self.chars) for i in range(6))
        return code

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urls:
            return self.urls[longUrl]
        requiredCode = self.getCode()
        while requiredCode in self.codes:
            requiredCode = self.getCode
        self.codes[requiredCode] = longUrl
        self.urls[longUrl] = requiredCode
        return requiredCode
        """Encodes a URL to a shortened URL.
        """

    def decode(self, shortUrl: str) -> str:
        return self.codes[shortUrl]
        """Decodes a shortened URL to its original URL.
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
