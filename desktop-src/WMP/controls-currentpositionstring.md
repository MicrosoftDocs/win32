---
title: Controls.currentPositionString
description: The currentPositionString property retrieves the current position in the media item as a String formatted as HH MM SS (hours, minutes, and seconds).
ms.assetid: 2b360cdb-3cf8-4d3c-82c2-7eb621f82f4c
keywords:
- Controls.currentPositionString Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentPositionString
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controls.currentPositionString

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **currentPositionString** property retrieves the current position in the media item as a **String** formatted as HH:MM:SS (hours, minutes, and seconds).

``` syntax
player.controls.currentPositionString
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

If the media item is less than an hour long, the HH: portion is not included.

> [!Note]  
> You should include code to stop the timer when the media item is stopped or paused.

 

## Examples

The following JScript example starts an HTML timer that displays the current position of the media file at one-second intervals. An HTML TEXT element named MyText was created to display the current position. The **Player** object was created with ID = "Player".


```JScript
var timer = window.setInterval("MyText.value = Player.controls.currentPositionString",1000);
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

 

 





