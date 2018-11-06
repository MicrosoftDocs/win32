---
title: Playlists and the MediaCollection Object
description: Playlists and the MediaCollection Object
ms.assetid: 3c98ceed-2545-4774-998b-c1db0d172a81
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player Mobile,playlists
- Windows Media Player ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- ActiveX control,playlists
- playlists,MediaCollection object
- metafile playlists,MediaCollection object
- Windows Media metafile playlists,MediaCollection object
- MediaCollection object
ms.topic: article
ms.date: 05/31/2018
---

# Playlists and the MediaCollection Object

The **MediaCollection** object gives you access to a variety of special playlists, and includes a method for creating a new playlist from a metafile.

The following methods retrieve special playlists:

-   **getAll**
-   **getByAlbum**
-   **getByAttribute**
-   **getByAuthor**
-   **getByGenre**
-   **getByName**

As their names suggest, these methods retrieve playlists containing all of the media items in the library that match certain criteria.

Be careful not to confuse the *MediaCollection*.**getByName** method with the *PlaylistCollection*.**getByName** method. The **MediaCollection** method returns a **Playlist** object containing all of the media items that have the specified name. The **PlaylistCollection** method returns a **PlaylistArray** object containing all of the playlists that have the specified name.

You can use the *MediaCollection*.**add** method to add playlists as well as media items to the library. To add a playlist, you pass the method the path to the metafile that defines the playlist. The method always returns a **Media** object. You cannot cast between **Media** and **Playlist** objects. To work with the playlist that you added, retrieve the **Playlist** object that has the same name as the **Media** object.

The following C# example demonstrates how to retrieve media by type using the **MediaCollection**.**getByAttribute** method. This code retrieves the names of all attributes associated with a given type as well as the read/write or read-only status of those attributes. It generates a single file that contains lists of attributes for the Audio, Video, Radio, Playlist, Other, Music, and Photo types.


```C++
string strOutFile = "AttribList.txt";    // Name of the output file
...
StreamWriter sw = new StreamWriter(strOutFile, true);

sw.Write(getMediaCollectionNames("Audio"));
sw.Write(getMediaCollectionNames("Video"));
sw.Write(getMediaCollectionNames("Radio"));
sw.Write(getMediaCollectionNames("Playlist"));
sw.Write(getMediaCollectionNames("Other"));
sw.Write(getMediaCollectionNames("Music"));
sw.Write(getMediaCollectionNames("Photo"));
sw.Close();
...
// The getMediaCollection method retrieves the names of
// all attributes for a specified type.
private string getMediaCollectionNames(string sSchema)
{
IWMPPlaylist playlist;
IWMPMedia media;
string strResult = "";    // Cumulative list of attributes
string strAttrName = "";  // Attribute name
string strReadWrite = ""; // Read/Write status of attribute
int iAttrCount = 0;       // Count of playlist attributes

// Retrieve a playlist corresponding to the requested type.
playlist = Player.mediaCollection.getByAttribute("MediaType", sSchema);

// Initialize the result string
strResult += "\n" + sSchema.ToString() + " Schema: \n";

// Retrieve the attributes for the playlist
if (playlist.count != 0)
{
    media = playlist.get_Item(0);
    iAttrCount = media.attributeCount;
    for (int i = 0; i < iAttrCount; i++)
    {
        strAttrName = media.getAttributeName(i);
        strResult += "   " + strAttrName  +"\n";
        if (media.isReadOnlyItem(strAttrName))
            strReadWrite = "Read Only";
        else
            strReadWrite = "Read/Write";
        strResult += "         " + strReadWrite + "\n";
    }
}

return strResult;
}

```



The following C# example demonstrates how to add a playlist from a metafile to the library.


```C++
// Add a playlist as a media item
IWMPMedia Media = Player.mediaCollection.add("c:\\testPlayList.asx");

```



Static playlists include specific media items. Auto playlists search the library every time they are opened and may contain different media items at different times. You can add both static and auto playlists to the library by using the *MediaCollection*.**add** method. You can also add static playlists by using the *PlaylistCollection*.**importPlaylist** method.

## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**Playlists and the PlaylistCollection Object**](playlists-and-the-playlistcollection-object.md)
</dt> <dt>

[**Static and Auto Playlists**](static-and-auto-playlists.md)
</dt> </dl>

 

 




