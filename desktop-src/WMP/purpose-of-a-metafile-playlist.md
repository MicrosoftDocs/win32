---
title: Purpose of a Metafile Playlist
description: Purpose of a Metafile Playlist
ms.assetid: fd5f002e-79c9-4339-bb98-86d5f378d8ed
keywords:
- Windows Media metafile playlists,purpose
- metafile playlists,purpose
- playlists,purpose
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

# Purpose of a Metafile Playlist

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The basic purpose of a metafile playlist is to redirect streaming media content away from browsers to Windows Media Player because most browsers will attempt to download the content instead of stream it. A metafile playlist provides information Windows Media Player uses to receive streams, such as the Uniform Resource Locator (URL). The metafile playlist can provide the path to media files over the Internet, an intranet or just stored media on a network or local drive. With processing redirected to Windows Media Player, you have greater control over the streaming media.

Metafile playlists are used to control the streaming experience. By combining different media files into a single content stream, you can control and customize their presentation.

## Related topics

<dl> <dt>

[**Windows Media Metafiles Overview**](windows-media-metafiles-overview.md)
</dt> </dl>

 

 




