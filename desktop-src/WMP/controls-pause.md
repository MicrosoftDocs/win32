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
ms.date: 05/31/2018
---

# Controls.pause method

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



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Controls.isAvailable**](controls-isavailable.md)
</dt> </dl>

 

 





