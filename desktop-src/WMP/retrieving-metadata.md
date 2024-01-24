---
title: Retrieving Metadata
description: Retrieving Metadata
ms.assetid: f634118a-0a62-4407-8be1-a907347de55b
keywords:
- Windows Media metafile playlists,retrieving metadata
- playlists,retrieving metadata
- metafile playlists,retrieving metadata
- Windows Media metafile playlists,metadata retrieval
- playlists,metadata retrieval
- metafile playlists,metadata retrieval
- metadata,retrieving
- retrieving metadata
- Windows Media Player,retrieving metadata
- Windows Media Player,metadata retrieval
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Retrieving Metadata

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

While a show or clip is playing, your script can retrieve metadata, such as title and author, by using the **getItemInfo** methods of the Windows Media Player **Media** and **Playlist** objects. You can retrieve metadata from the ASX scope using **Playlist** object methods and from the ENTRY scope using **Media** object methods.

For example, to retrieve the values for AUTHOR, ABSTRACT and PARAM in the following file, use the **getItemInfo** method of the **Playlist** object. The attribute name is required for this method. Attribute names can be obtained by providing the index number to the **attributeName** property. The available indexes for a **Playlist** object can be obtained using the **attributeCount** property.

## Example Code


```XML

    <ASX version="3.0">
        <AUTHOR>My Talking File</AUTHOR>
        <ABSTRACT>Talking File Album</ABSTRACT>
        <PARAM name="one" value="111"/>
        <ENTRY>
            <REF href="Artists_Only.wma"/>
            <TITLE>Artists Only</TITLE>
            <COPYRIGHT>2000</COPYRIGHT>
            <PARAM name="three" value="333"/>
        </ENTRY>
        <PARAM name="two" value="222"/>
    </ASX>
    

```



To retrieve the values of the current **Media** object in the ENTRY scope for REF,TITLE,COPYRIGHT, and PARAM ("three"), use the **currentMedia** property of the **Player** object. Use the **attributeCount** property of the **Media** object to determine the number of attributes available for the specified **Media** object. Use index numbers with the **getItemInfoByAtom** method to retrieve attribute values. Use index numbers with the **getAttributeName** method of the **Media** object to determine the names of the available attributes, and then use the results with the **getItemInfo** method.

For an example of using Windows Media Player object methods to retrieve metadata, see [Playlist.attributeCount](playlist-attributecount.md).

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




