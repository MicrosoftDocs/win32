---
title: Player.playState
description: The playState property retrieves a value indicating the state of the Windows Media Player operation.
ms.assetid: 8ed1ee1f-8731-402a-aff5-5ae513a35eea
keywords:
- Player.playState Windows Media Player
topic_type:
- apiref
api_name:
- Player.playState
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.playState

The **playState** property retrieves a value indicating the state of the Windows Media Player operation.

## Syntax

*player* .**playState**

## Possible Values

This property is a read-only **Number** (**long**). The C-style enumeration constant can be derived by prefixing the state value with "wmpps". For example, the constant for the Playing state is **wmppsPlaying**.



| Value | State         | Description                                                                                                                 |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0     | Undefined     | Windows Media Player is in an undefined state.                                                                              |
| 1     | Stopped       | Playback of the current media item is stopped.                                                                              |
| 2     | Paused        | Playback of the current media item is paused. When a media item is paused, resuming playback begins from the same location. |
| 3     | Playing       | The current media item is playing.                                                                                          |
| 4     | ScanForward   | The current media item is fast forwarding.                                                                                  |
| 5     | ScanReverse   | The current media item is fast rewinding.                                                                                   |
| 6     | Buffering     | The current media item is getting additional data from the server.                                                          |
| 7     | Waiting       | Connection is established, but the server is not sending data. Waiting for session to begin.                                |
| 8     | MediaEnded    | Media item has completed playback.                                                                                          |
| 9     | Transitioning | Preparing new media item.                                                                                                   |
| 10    | Ready         | Ready to begin playing.                                                                                                     |
| 11    | Reconnecting  | Reconnecting to stream.                                                                                                     |



 

## Remarks

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

## Examples

The following JScript code shows the use of the *player*.**playState** property. An HTML text element, named "myText", displays the current status. The **Player** object was created with ID = "Player".


```JScript
// Test whether Windows Media Player is in the playing state.
if (3 == Player.playState)
    myText.value = "Windows Media Player is playing!";
else
    myText.value = "Windows Media Player is NOT playing!";
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.PlayStateChange Event**](player-player-playstatechange.md)
</dt> </dl>

 

 





