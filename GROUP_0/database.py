songList = []
albumList = []
from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['MIBO']
Accounts = db.Accounts
SongRatings = db.SongRatings
AlbumRatings = db.AlbumRatings


def saveInfo(username, password):
    if Accounts.find({'usernames':username}).count() == 0:
        Accounts.insert({'usernames':username,'passwords':password})
        return True
    else:
        return False


def verifyLogin(username, password):
    if Accounts.find({'usernames':username,'passwords':password}).count() != 0:
        return True
    else:
        return False
def returnAllAccounts():
    accounts = []
    for account in Accounts.find():
        accounts.append('Username: '+str(account['usernames'])+'Password: '+str(account['passwords']))
    return accounts

 
#basic login method that verifies input username and password


def addSong(song):
    pass

def addAlbum(album):
    pass

def addSongRating(song,artist,rating,comment):
    ratingList = SongRatings.findOne({'song':song,'artist':artist})
    if ratingList == None:
        pass
    else:
        ratingList = ratingList['rating']
    commentList = SongRatings.findOne({'song':song,'artist':artist})
    if commentList == None:
        pass
    else:
        commentList = commentList['comment']
    if ratingList == None:
        ratingList = [rating]
    else:
        ratingList.append(rating)
    if commentList == None:
        commentList = [comment]
    else:
        commentList.append(str(comment))
    SongRatings.update({'song':song,'artist':artist},{'$set':{'comment':commentList,'rating':ratingList}})

def addAlbumrating(album,artist,rating,comment):
    ratingList = AlbumRatings.findOne({'album':album,'artist':artist})['rating']
    commentList = AlbumRatings.findOne({'album':album,'artist':artist})['comment']
    if ratingList == None:
        ratingList = [rating]
    else:
        ratingList.append(rating)
    if commentList == None:
        commentList = [comment]
    else:
        commentList.append(str(comment))
    AlbumRatings.update({'album':album,'artist':artist},{'$set':{'comment':commentList,'rating':ratingList}})
    
def getSongRating(song,artist):
    return SongRatings.findOne({'song':song,'artist':artist})
def getAlbumRating(album,artist):
    return AlbumRatings.findOne({'album':album,'artist':artist})
#will return the rating of the song/album
    


if __name__ == '__main__':
    addSongRating('YAH','BYE',10,'TEEHEE')
    addSongRating('YAH','BYE',5,'KEKEKEE')
        
    
