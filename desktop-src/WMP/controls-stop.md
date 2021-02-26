---
title: Controls.stop method
description: The stop method stops playback of the media item. | Controls.stop method
ms.assetid: ace95fde-9c94-4737-88f2-94321cbc687c
keywords:
- stop method Windows Media Player
- stop method Windows Media Player , Controls class
- Controls class Windows Media Player , stop method
topic_type:
- apiref
api_name:
- Controls.stop
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.stop method

The **stop** method stops playback of the media item.

## Syntax


```JScript
Controls.stop()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method causes Windows Media Player to release any system resources it is using, such as the audio device. The current media item, however, is not released.

When the player is stopped, the track rewinds to the beginning. Calling **play** will then begin playback of the clip from the beginning. To halt a play operation without changing the current position, use the **pause** method.

## Examples

The following example creates an HTML BUTTON element that uses **stop** to stop playback. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "STOP"  NAME = "STOP"  VALUE = "Stop"
    onClick = "

        /* Check first to be sure the operation is valid. */
        if (Player.controls.isAvailable('Stop'))

            /* Stop the Player. */
            Player.controls.stop();
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

[**Controls.next**](controls-next.md)
</dt> <dt>

[**Controls.pause**](controls-pause.md)
</dt> <dt>

[**Controls.previous**](controls-previous.md)
</dt> </dl>

 

 





