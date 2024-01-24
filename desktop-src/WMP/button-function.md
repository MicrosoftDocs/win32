---
title: Button Function
description: Button Function
ms.assetid: 6dfcf639-5989-4da8-b78d-8e393aba641a
keywords:
- Windows Media Player Mobile skins,button functions
- skins,button functions
- reference for skins,buttons
- buttons in skins,functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Button Function

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table shows values that are valid for the Button function. You do not need to define values for functions that you will not be using in your skin.



| Value           | Description                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Play            | Plays the current selection in the playlist.                                                                                                                 |
| Pause           | Pauses playback of the current media item.                                                                                                                   |
| Stop            | Stops playback of the current media item.                                                                                                                    |
| Prev            | Moves to the previous item in the playlist.                                                                                                                  |
| Next            | Moves to the next item in the playlist.                                                                                                                      |
| Shuffle         | Shuffles the playlist randomly.                                                                                                                              |
| RepeatPlaylist  | Repeats the playlist indefinitely.                                                                                                                           |
| Mute            | Silences the audio output.                                                                                                                                   |
| PlayPause       | Toggles between the play state and the pause state.                                                                                                          |
| Info            | Provides information about the media item that is playing. For Windows Media Player 10 Mobile or later skins, this function is not used.                     |
| FullScreen      | Resizes the video to the maximum size of the device display.                                                                                                 |
| WindowsMedia\*  | Opens Pocket Internet Explorer and loads the Windowsmedia.com website.                                                                                       |
| PlayPauseStop\* | In addition to toggling between the play state and the pause state, it also allows users to stop a live broadcast when pause functionality is not available. |
| VolumeUp\*      | Increases the audio output.                                                                                                                                  |
| VolumeDown\*    | Decreases the audio output.                                                                                                                                  |



 

\*Available for Windows Media Player 10 Mobile or later.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




