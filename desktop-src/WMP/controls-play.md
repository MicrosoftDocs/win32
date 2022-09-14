---
title: Controls.play method
description: The play method causes the current media item to start playing, or resumes play of a paused item.
ms.assetid: 2218a13b-6294-45f5-bb6f-c5a1e433e0c6
keywords:
- play method Windows Media Player
- play method Windows Media Player , Controls class
- Controls class Windows Media Player , play method
topic_type:
- apiref
api_name:
- Controls.play
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.play method

The **play** method causes the current media item to start playing, or resumes play of a paused item.

## Syntax


```JScript
Controls.play()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If this method is called while fast-forwarding or rewinding, the value of *Settings*.**rate** is set to 1.0.

## Examples

The following example creates an HTML BUTTON element that uses **play** to play the current media item. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "PLAY"  NAME = "PLAY"  VALUE = "Play"
    onClick = "

        /* Check first to be sure the operation is valid. */
        if (Player.controls.isAvailable('Play'))

            /* Start playback. */
            Player.controls.play();
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
</dt> </dl>

 

 





