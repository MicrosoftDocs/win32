---
title: A Basic Playlist
description: A Basic Playlist
ms.assetid: fdd87959-861a-456e-b903-f5a27b4f6221
keywords:
- Windows Media metafile playlists,playlist examples
- playlists,playlist examples
- metafile playlists,playlist examples
- Windows Media metafile playlists,example playlists
- playlists,example playlists
- metafile playlists,example playlists
- Windows Media metafile playlists,sample playlists
- playlists,sample playlists
- metafile playlists,sample playlists
- Windows Media metafile playlists,code example
- playlists,code example
- metafile playlists,code example
- Windows Media metafile playlists,basic playlist example
- playlists,basic playlist example
- metafile playlists,basic playlist example
- Windows Media Player,playlist examples
- Windows Media Player,example playlists
- Windows Media Player,sample playlists
- Windows Media Player,basic playlist example
- playlist examples
- example playlists
- sample playlists
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# A Basic Playlist

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following playlist example shows a basic set of playlist elements. When writing your own code, you will need to change all URLs and file names to valid file names that are accessible to your Windows Media Player.

**Code Example**


```XML
<ASX version = "3.0">
<TITLE>Basic Playlist Demo</TITLE>
    <ENTRY>
        <TITLE>An Entry in a basic playlist</TITLE>
        <AUTHOR>Microsoft Corporation</AUTHOR>
        <COPYRIGHT>(c)2000 Microsoft Corporation</COPYRIGHT>
        <REF HREF = "mms://proseware.com/path/Yourfile.wma" />
    </ENTRY>
</ASX>

```



The following table provides details on the use of each element in the example code.



| Line                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<ASX version = "3.0">                                                                     | The [ASX](asx-element.md) element identifies for the client (Windows Media Player) that this is a Windows Media metafile playlist. The **version** attribute specifies the version number of the metafile elements.                                                                                                                                                                                                                                                                                                                                           |
| \<TITLE>Basic Playlist Demo\</TITLE>                                                  | The [TITLE](title-element--metafile.md) element identifies the title of the playlist as a whole. Windows Media Player displays this metadata as the show title.                                                                                                                                                                                                                                                                                                                                                                                               |
| \<ENTRY>                                                                                   | Begins the [ENTRY](entry-element.md) element. An **ENTRY** element is a way to define a particular clip in a playlist                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \<TITLE>An Entry in a basic playlist\</TITLE>                                         | Identifies the title of the playlist clip . It is different than the previous **TITLE** element because this one is nested within an **ENTRY** element. Windows Media Player displays this metadata as the clip title.                                                                                                                                                                                                                                                                                                                                         |
| \<AUTHOR>Microsoft Corporation\</AUTHOR>                                              | The [AUTHOR](author-element.md) element identifies the author of the media clip . Windows Media Player displays this metadata as the clip **AUTHOR**.                                                                                                                                                                                                                                                                                                                                                                                                         |
| \<!-- This is a comment. Change the following path to point to your Windows media file --> | A comment. [Comments](comments.md) are visible only when the code is viewed, and are in the same format as **XML** comments.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \<REF HREF = "mms://proseware.com/path/Yourfile.wma" />                                    | Actual pointer to the media file. The [REF](ref-element.md) element identifies the line as a pointer to media content, while the **HREF** attribute is the URL to the media file. In this case, the URL uses the MMS protocol, so it points to a Windows Media server.Media files on your media server are not usually kept in the same location as your HTML documents.<br/> Note the use of the XML-like closing of the element , "/>", instead of "&lt;/REF&gt;". Because this element does not have child elements, it closes itself.<br/> |
| \</ENTRY>                                                                                  | Specifies the end of the **ENTRY** element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \</ASX>                                                                                    | Specifies the end of the playlist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Example Playlists**](example-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 





