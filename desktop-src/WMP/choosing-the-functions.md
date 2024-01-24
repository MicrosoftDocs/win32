---
title: Choosing the Functions
description: Choosing the Functions
ms.assetid: ded3c578-5087-4e4f-bf21-2149cf72719d
keywords:
- Windows Media Player Mobile skins,functions for audio
- skins,functions for audio
- creating skins,functions for audio
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Choosing the Functions

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The purpose of this skin is to provide basic functionality for playing audio. The following functions will be used:



| Function                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PlayPause or PlayPauseStop\* | Starting the media item is of prime importance. If you are creating a skin for Windows Media Player 10 Mobile or later, then you should use PlayPauseStop. If you are working with an earlier version of Windows Media Player Mobile, then you must use PlayPause. Both functions give you the added functionality of pausing, but only PlayPauseStop allows you to stop a live broadcast when pause functionality is not available. |
| Stop                         | You will want to add Stop to stop playing the item. If you are creating a skin for Windows Media Player 10 Mobile or later, the PlayPauseStop function already provides this functionality.                                                                                                                                                                                                                                          |
| Next                         | If you have a playlist, you will want to be able to choose the next item. You need this for basic navigation of digital media.                                                                                                                                                                                                                                                                                                       |
| Prev                         | While you could use Next to cycle through the playlist until you came to the beginning, adding Prev will make it easy for the user to go backward as well as forward when navigating the playlist.                                                                                                                                                                                                                                   |
| VolumeUp or VolumeDown\*     | You will want to provide the user with the ability to turn the volume up or down.                                                                                                                                                                                                                                                                                                                                                    |



 

\*Available for Windows Media Player 10 Mobile or later.

## Related topics

<dl> <dt>

[**Skin Guide**](skin-guide.md)
</dt> </dl>

 

 




