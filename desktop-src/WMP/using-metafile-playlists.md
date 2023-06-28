---
title: Using Metafile Playlists
description: Using Metafile Playlists
ms.assetid: f5711a7f-7674-4b92-8262-cee8bac4aa77
keywords:
- Windows Media metafile playlists,about
- playlists,about
- metafile playlists,about
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Metafile Playlists

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Playlists specify how the streaming media or media files will be played and what metadata Windows Media Player will display.

This section explains several ways you can use playlists. The section is divided into the following topics.



| Topic                                                                                              | Description                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Modifying the Display](modifying-the-display.md)                                                 | Adding text, links, and images.                                                                                                                                |
| [Redirection](redirection.md)                                                                     | Using playlists to redirect the browser to Windows Media Player and specifying the URL of a stream or media file to play.                                      |
| [Accessing Media](accessing-media.md)                                                             | Using metafile elements and their child elements to specify the content to access, and the order and duration of their playback.                               |
| [Using Live Event Stream Switching](using-live-event-stream-switching.md)                         | Using the **EVENT** element to specify a media stream to access and then resume playing the original stream. Used for ad insertion.                            |
| [Using Metafiles for Seamless Stream Switching](using-metafiles-for-seamless-stream-switching.md) | Using the **EVENT** element to preload the next media stream to access to avoid gaps in the presentation.                                                      |
| [Using Announcements](using-announcements.md)                                                     | Using a metafile to provide information about the URL for a media stream, including the multicast IP address, port, stream format, and other station settings. |
| [Using URL and Server Rollover](using-url-and-server-rollover.md)                                 | Using metafile playlists to provide a means of automatically rolling over to alternate content sources when a stream cannot be accessed or played.             |
| [Using Custom Parameters and Commands](using-custom-parameters-and-commands.md)                   | Using the **PARAM** element to define custom elements to provide additional metadata.                                                                          |
| [Personalizing Media Delivery](personalizing-media-delivery.md)                                   | Using user preferences to determine broadcast content.                                                                                                         |



 

## Related topics

<dl> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




