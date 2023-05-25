---
title: Using Announcements
description: Using Announcements
ms.assetid: c372a4f8-2355-4c69-bba2-72b224879c4d
keywords:
- Windows Media metafile playlists,announcements
- playlists,announcements
- metafile playlists,announcements
- Windows Media Player,announcements
- announcements
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Announcements

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An announcement is a file that contains information about the URL for a media stream, including the multicast IP address, port, stream format, and other station settings. Announcements are created by Windows Media Administrator when a unicast or multicast publishing stream is created. The client can quickly load the announcement file, then proceed to access the streaming media file.

For a unicast publishing point, the publishing point media stream is opened. For a multicast publishing point, the URL is extracted from a broadcast station file with an .nsc extension, and the streaming media is accessed. Unlike a unicast stream, no header information is contained in a multicast stream. That information comes from the broadcast station file with an .nsc extension. Windows Media Player usually first opens an announcement file, which is one use for metafile playlists, that points to the location of the broadcast station file.

Example Code


```XML
<ASX VERSION="3.0">
    <TITLE>title</TITLE>
    <ENTRY>
        <REF HREF="mms://proseware.com/pubpoint"/>
    </ENTRY>
</ASX>

```



## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> </dl>

 

 




