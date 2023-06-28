---
title: Controls.pause method
description: The pause method pauses playback of the media item. | Controls.pause method
ms.assetid: 7307a3b2-e5d6-4067-bdb5-38011565142a
keywords:
- pause method Windows Media Player
- pause method Windows Media Player , Controls class
- Controls class Windows Media Player , pause method
topic_type:
- apiref
api_name:
- Controls.pause
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controls.pause method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **pause** method pauses playback of the media item.

## Syntax


```JScript
Controls.pause()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

When a file is paused, Windows Media Player does not give up any system resources, such as the audio device.

Certain media types cannot be paused, such as live streams. To determine whether a particular media type can be paused, use *Controls*.**isAvailable('Pause')**.

## Examples

The following example creates an HTML BUTTON element that uses **pause** to pause playback. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "PAUSE"  NAME = "PAUSE"  VALUE = "||"
    onClick = "

        /* Check first to be sure the operation is valid. */
        if (Player.controls.isAvailable('Pause'))

            /* Pause the Player. */
            Player.controls.pause();
">
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Controls.isAvailable**](controls-isavailable.md)
</dt> </dl>

 

 





