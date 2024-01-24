---
title: Using Metafiles for Seamless Stream Switching
description: Using Metafiles for Seamless Stream Switching
ms.assetid: e632f670-54c4-4b5b-8396-1d5368f90e6d
keywords:
- Windows Media metafile playlists,live event stream switching
- playlists,live event stream switching
- metafile playlists,live event stream switching
- Windows Media metafile playlists,event stream switching
- playlists,event stream switching
- metafile playlists,event stream switching
- Windows Media metafile playlists,ad insertion
- playlists,ad insertion
- metafile playlists,ad insertion
- Windows Media Player,live event stream switching
- Windows Media Player,event stream switching
- Windows Media Player,ad insertion
- live event stream switching
- event stream switching
- ad insertion
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Metafiles for Seamless Stream Switching

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can facilitate seamless stream switching using metafile playlists. Usually, when a piece of content ends, buffering occurs for the next clip or stream before it opens (if it is content received from a streaming media server). Microsoft Windows Media Services enables you to eliminate, or at least minimize, this buffering time and have another piece of streamed content begin playing nearly immediately. The normal mode of operation for Windows Media Player is to open the next media stream referenced by the playlist 20 seconds before the end of the currently rendered stream. This generally provides a seamless transition between media streams, depending on other factors such as Web access times.

Use the **EVENT** element in a playlist in conjunction with OPENEVENT commands from the encoder to facilitate seamless switching between streams or files. Sending an OPENEVENT command 20 seconds or more prior to the EVENT command can minimize delays in stream switching. Then Windows Media Player is able to preload a portion of the upcoming streaming content into a buffer.

Use Windows Media Encoder to send a script command in the stream using the following format:


```XML
OPENEVENT eventname 

```



The event name must be the one defined in the **EVENT** element in the playlist. When Windows Media Player receives an OPENEVENT script command from the encoder, it looks to the **EVENT** element in the playlist and begins buffering the clip or stream defined in the **EVENT** element. Windows Media Player then holds this information until the actual event of the same name. When the named event is received, Windows Media Player switches to that previously buffered content.

> [!Note]  
> You cannot use Unicode characters for the OPENEVENT script command in the media file or the **EVENT** element in the playlist.

 

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Player.ScriptCommand Event**](player-player-scriptcommand.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




