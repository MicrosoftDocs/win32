---
title: Using Custom Parameters and Commands
description: Using Custom Parameters and Commands
ms.assetid: 6b0bfd19-1672-41e3-9b7f-c8d541168c0e
keywords:
- Windows Media metafile playlists,custom parameters
- playlists,custom parameters
- metafile playlists,custom parameters
- Windows Media metafile playlists,custom commands
- playlists,custom commands
- metafile playlists,custom commands
- Windows Media metafile playlists,parameters
- playlists,parameters
- metafile playlists,parameters
- custom parameters
- custom commands
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Custom Parameters and Commands

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can create custom parameters to pass additional metadata in a metafile playlist by using the **PARAM** element. Use the **NAME** attribute of the **PARAM** element to define the custom parameter name. Use the **VALUE** attribute to define the value for the named custom parameter.

Retrieve **PARAM** metadata by using the **getItemInfo** methods of the **Media** and **Playlist** objects. For an example using these methods to retrieve metadata, see the [attributeCount](playlist-attributecount.md) method of the **Playlist** object.

The following example metafile playlist shows the use of the **PARAM** element to define custom parameters.


```XML
<ASX version="3.0" BANNERBAR="auto" >
    <TITLE>Example Media Player Show</TITLE>
    <PARAM NAME="Director" VALUE="Jane D." />

    <ENTRY>
        <TITLE>Example Clip</TITLE>
        <REF HREF="https://www.proseware.com/media.wma" />
        <PARAM NAME="Title" VALUE="Example Clip" />
        <PARAM NAME="Location" VALUE="North America" />
        <PARAM NAME="Release Date" VALUE="March 1998" />
    </ENTRY>

    <ENTRY>
        <TITLE>Another Clip</TITLE>
        <REF HREF="https://www.proseware.com/more_media.wma" />
        <PARAM NAME="Title" VALUE="Another Clip" />
        <PARAM NAME="Location" VALUE="Japan" />
        <PARAM NAME="Release Date" VALUE="December 2000" />
    </ENTRY>
</ASX>

```



## Related topics

<dl> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> </dl>

 

 




