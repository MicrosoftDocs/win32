---
title: Controls.currentPositionTimecode
description: The currentPositionTimecode property specifies or retrieves the current position in the current media item using a time code format. This property currently supports SMPTE time code.
ms.assetid: 98d79756-c6cf-4dbc-936a-58229452451c
keywords:
- Controls.currentPositionTimecode Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentPositionTimecode
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentPositionTimecode

The **currentPositionTimecode** property specifies or retrieves the current position in the current media item using a time code format. This property currently supports SMPTE time code.

``` syntax
player.controls.currentPositionTimecode
      
```

## Possible Values

This property is a read/write **String**.

## Remarks

SMPTE time code provides a standard way of identifying an individual video frame, which is useful for synchronizing playback. If a digital media file supports SMPTE time code, Windows Media Player can retrieve the current time code position information or seek to a video frame identified by a particular time code **String**.

SMPTE time code identifies a particular frame by the number of hours, minutes, seconds, and frames that separate it from a particular reference frame the frame designated as time zero. Usually the time zero frame is the start of the file and a particular SMPTE time code value represents the elapsed time since the start of the file.

The time code **String** is in the format \[*range*\]*hh*:*mm*:*ss*.*ff* where \[*range*\] represents the range, *hh* represents hours, *mm* represents minutes, *ss* represents seconds, and *ff* represents frames. When specifying a value using **currentPositionTimecode**, you must include all eight digits using zeros as placeholders.

The \[*range*\] specifier corresponds to the **wRange** member of the Windows Media Format **WMT\_TIMECODE\_EXTENSION\_DATA** structure. For more information about time code ranges, see the Windows Media Format SDK.

Specifying and retrieving **currentPositionTimecode** is only supported for files that contain SMPTE time code information.

## Examples

The following code example specifies **currentPositionTimecode** as 1 hour, zero minutes, 30 seconds, and 5 frames. The **Player** object was created with ID = "Player".


```
// Seek to a frame using SMPTE time code.
Player.controls.currentPositionTimecode = "[00000]01:00:30.05";

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> </dl>

 

 





