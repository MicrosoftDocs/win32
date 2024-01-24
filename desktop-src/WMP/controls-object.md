---
title: Controls Object
description: The Controls object provides a way to manipulate the playback of media using the following properties and methods.
ms.assetid: 'bcc1e768-4fa6-4c82-a12f-52c9bfb4c10c'
keywords:
- Controls Object Windows Media Player
topic_type:
- apiref
api_name:
- Controls Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Controls Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Controls** object provides a way to manipulate the playback of media using the following properties and methods.

The **Controls** object supports the following properties.



| Property                                                            | Description                                                                                                                                       |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [audioLanguageCount](controls-audiolanguagecount.md)               | Retrieves the number of supported audio languages.                                                                                                |
| [currentAudioLanguage](controls-currentaudiolanguage.md)           | Specifies or retrieves the locale identifier (LCID) of the audio language for playback                                                            |
| [currentAudioLanguageIndex](controls-currentaudiolanguageindex.md) | Specifies or retrieves the one-based index that corresponds to the audio language for playback.                                                   |
| [currentItem](controls-currentitem.md)                             | Specifies or retrieves the current media item.                                                                                                    |
| [currentMarker](controls-currentmarker.md)                         | Specifies or retrieves the current marker number.                                                                                                 |
| [currentPosition](controls-currentposition.md)                     | Specifies or retrieves the current position in the media item in seconds from the beginning.                                                      |
| [currentPositionString](controls-currentpositionstring.md)         | Retrieves the current position in the media item as a **String**.                                                                                 |
| [currentPositionTimecode](controls-currentpositiontimecode.md)     | Specifies or retrieves the current position in the current media item using a time code format. This property currently supports SMPTE time code. |
| [isAvailable](controls-isavailable.md)                             | Retrieves whether a specified type of information is available or a given action can be performed.                                                |



 

The **Controls** object supports the following methods.



| Method                                                                  | Description                                                                                      |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [fastForward](controls-fastforward.md)                                 | Starts fast play of the media item in the forward direction.                                     |
| [fastReverse](controls-fastreverse.md)                                 | Starts fast play of the media item in the reverse direction.                                     |
| [getAudioLanguageDescription](controls-getaudiolanguagedescription.md) | Retrieves the description for the audio language corresponding to the specified one-based index. |
| [getAudioLanguageID](controls-getaudiolanguageid.md)                   | Retrieves the LCID for a specified audio language index.                                         |
| [getLanguageName](controls-getlanguagename.md)                         | Retrieves the name of the audio language with the specified LCID.                                |
| [next](controls-next.md)                                               | Sets the current item to the next item in the playlist.                                          |
| [pause](controls-pause.md)                                             | Pauses the playing of the media item.                                                            |
| [play](controls-play.md)                                               | Causes the media item to start playing.                                                          |
| [playItem](controls-playitem.md)                                       | Causes the current media item to start playing, or resumes play of a paused item.                |
| [previous](controls-previous.md)                                       | Sets the current item to the previous item in the playlist.                                      |
| [step](controls-step.md)                                               | Causes the current video media item to freeze playback on the next frame.                        |
| [stop](controls-stop.md)                                               | Stops the playing of the media item.                                                             |



 

The **Controls** object is accessed through the following property.



| Object                      | Property                        |
|-----------------------------|---------------------------------|
| [Player](player-object.md) | [controls](player-controls.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




