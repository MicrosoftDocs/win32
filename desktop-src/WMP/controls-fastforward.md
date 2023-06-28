---
title: Controls.fastForward method
description: The fastForward method starts fast play of the media item in the forward direction. | Controls.fastForward method
ms.assetid: 69cee803-f76b-4a8c-a2c2-1870665afaf9
keywords:
- fastForward method Windows Media Player
- fastForward method Windows Media Player , Controls class
- Controls class Windows Media Player , fastForward method
topic_type:
- apiref
api_name:
- Controls.fastForward
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controls.fastForward method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fastForward** method starts fast play of the media item in the forward direction.

## Syntax


```JScript
Controls.fastForward()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **fastForward** method plays the clip back at five times the normal speed. Invoking **fastForward** changes the *Settings*.**rate** property to 5.0. If **rate** is subsequently changed, or if **play** or **stop** is called, Windows Media Player will cease fast forwarding.

The **fastForward** method does not work for live broadcasts and certain media types. To determine whether you can fast forward in a clip, call **isAvailable**("FastForward").

## Examples

The following example creates an HTML BUTTON element that uses **fastForward** to start fast play of the media item. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "FF"  NAME = "FF"  VALUE = ">>"  

    /* Execute JScript when the BUTTON is clicked. 
       Check first to make sure fast-forward mode is available
       for this particular media item */
    onClick = "if (Player.controls.isAvailable('FastForward'))
        Player.controls.fastForward();
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
</dt> <dt>

[**Controls.play**](controls-play.md)
</dt> <dt>

[**Controls.stop**](controls-stop.md)
</dt> <dt>

[**Settings.rate**](settings-rate.md)
</dt> </dl>

 

 





