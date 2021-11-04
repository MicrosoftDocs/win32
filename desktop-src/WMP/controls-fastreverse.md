---
title: Controls.fastReverse method
description: The fastReverse method starts fast scanning of the media item in the reverse direction.
ms.assetid: 4fc61739-9006-4d62-b2c1-2b8e8830f2d9
keywords:
- fastReverse method Windows Media Player
- fastReverse method Windows Media Player , Controls class
- Controls class Windows Media Player , fastReverse method
topic_type:
- apiref
api_name:
- Controls.fastReverse
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.fastReverse method

The **fastReverse** method starts fast scanning of the media item in the reverse direction.

## Syntax


```JScript
Controls.fastReverse()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **fastReverse** method scans the clip in reverse at five times the normal speed, displaying only the key frames if it is a video file. Invoking **fastReverse** changes the *Settings*.**rate** property to  5.0. If **rate** is subsequently changed, or if **play** or **stop** is called, Windows Media Player will cease fast reverse.

If the item is part of a playlist, **fastReverse** stops at the beginning of the current track. For instance, if track 3 is in **fastReverse**, when the beginning of track 3 is reached, Windows Media Player will not go to track 2. The play count is not incremented when calling **fastReverse**.

If you call **fastForward** while **fastReverse** is in effect, **fastReverse** will be stopped and **fastForward** will begin.

This method does not work for live broadcasts and certain media types. To determine whether you can use fast reverse in a clip, call **isAvailable**("FastReverse").

## Examples

The following example creates an HTML BUTTON element that uses **fastReverse** to start fast-reverse play of the media item. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "REW"  NAME = "REW"  VALUE = "<<"  

    /* Run JScript when the BUTTON is clicked. 
       Check first to make sure fast-reverse mode is available
       for this particular media item */
    onClick = "if (Player.controls.isAvailable('FastReverse'))
        Player.controls.fastReverse();
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

[**Controls.fastForward**](controls-fastforward.md)
</dt> <dt>

[**Controls.isAvailable**](controls-isavailable.md)
</dt> <dt>

[**Controls.play**](controls-play.md)
</dt> <dt>

[**Controls.stop**](controls-stop.md)
</dt> <dt>

[**Settings.rate**](settings-rate.md)
</dt> </dl>

 

 





