---
title: Using a Metafile Playlist
description: Using a Metafile Playlist
ms.assetid: e6cbdb76-4405-409e-93c3-38a3baa7c231
keywords:
- Windows Media metafile playlists,using
- metafile playlists,using
- playlists,using
- Windows Media metafile playlists,about
- metafile playlists,about
- playlists,about
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using a Metafile Playlist

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Because you cannot link directly from a webpage to a streaming media server, you use metafile playlists. The metafile playlists contain the information needed by Windows Media Player and are stored on a web server. You can then link from the Web document to a metafile playlist. When a metafile playlist is opened, control transfers to Windows Media Player, which processes the file, connects to the streaming media server, and plays the specified content.

The browser first downloads the metafile playlist to the user's cache directory. Because the metafile playlist is small, this is a very quick step. The user's computer then finds in its file associations table the association of the metafile playlist with Windows Media Player. Windows Media Player opens and interprets the scripting in the metafile playlist, which contains, among other things, the URL of the streaming content. Windows Media Player uses the URL to locate the content and initiate the stream. The metafile playlist scripting then controls the streaming experience.

Because metafile playlists work through a helper application associated with the ASXMIME type (application/mplayer2 or video/x-ms-asf), they are compatible with any browser that supports helper applications. The examples shown in this document will work with Microsoft Internet Explorer 4.0 and later, and with Netscape Navigator 4.0 and later on Microsoft Win32® and Apple Macintosh platforms. In all examples, you will have to be sure that any digital media files referenced have valid paths and file names for your environment.

## Related topics

<dl> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> <dt>

[**Windows Media Metafiles Overview**](windows-media-metafiles-overview.md)
</dt> </dl>

 

 




