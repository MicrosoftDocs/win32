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
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using Announcements

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

 

 




