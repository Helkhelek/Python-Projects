# Note: A URL character can be one of the following

# A lowercase alphabet [‘a’ to ‘z’], total 26 characters
# An upper case alphabet [‘A’ to ‘Z’], a total of 26 characters
# A digit [‘0′ to ‘9’], a total of 10 characters

def idToShortURL(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortUrl = ""

    while (id>0):
        shortUrl += map[id%62]
        id//=62
        print(shortUrl)


idToShortURL(12)

def shortUrlToId(shortUrl):
    id = 0
    for i in shortUrl:
        val_i = ord(i)
        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*62 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*62 + val_i - ord('A') + 26
        else:
            id = id*62 + val_i - ord('0') + 52
    print(id)

shortUrlToId("m")
