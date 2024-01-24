---
title: User Interface Elements
description: User Interface Elements
ms.assetid: cb2876fb-632e-4c3d-8a6e-f7c8c4878c3f
keywords:
- Windows Media Player Mobile skins,user interfaces
- Windows Media Player Mobile skins,elements
- elements,Windows Media Player Mobile skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# User Interface Elements

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Even though you can choose from a wide range of functionality for controlling digital media, playlists, and volume, it is up to you to provide the user of your skin with a way to interact with that functionality. For example, if you want the user to start playing a media item, you must provide a user-interface button element that will cause the media item to play when the user taps the image of your button.

No elements are required, but if you do not have a few buttons to play and stop the media item, not much will happen. It is also a good idea to provide a volume control.

User interface elements correspond to types of functionality used to control digital media selection and playback.

The following elements are provided.



| Element                    | Description                                                                                                                                                                                                                                                             |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Buttons](buttons.md)     | Many button types are provided. Buttons can be used to turn functions on or off or switch between two functions.                                                                                                                                                        |
| [Trackbars](trackbars.md) | You can provide linear control through trackbars. You will want to use trackbars to change the volume or the playback position in a media item.                                                                                                                         |
| [Text](text.md)           | Text boxes can be used to display text to the user. A good use of a text box is to display the name of the song currently playing.                                                                                                                                      |
| [Marquee](marquee.md)     | A marquee is a scrolling text box that you can use to display text from more than one text category. For example, you can display the playlist, number of tracks, and track number playing. Use a marquee when you don't have much space and you have a lot to display. |
| [Status](status.md)       | You can provide a status display that you can use to automatically display text messages that inform the user about the current state of Windows Media Player. For example, the status display will inform the user when a media item is buffering.                     |
| [Video](video.md)         | You can provide a rectangular video display area in your skin if you want to play video.                                                                                                                                                                                |
| [Ratings](ratings.md)     | You can display the rating associated with any Windows Media Audio-based content that is currently playing.                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[**About Skins**](about-skins-mobile.md)
</dt> </dl>

 

 




