---
title: IWMPControls3 currentPositionTimecode property
description: The currentPositionTimecode property gets or sets the current position in the current media item using a time code format. This property currently supports SMPTE time code.
ms.assetid: 035b812c-e976-4b4e-b4e5-820653257732
keywords:
- currentPositionTimecode property Windows Media Player
- currentPositionTimecode property Windows Media Player , IWMPControls3 interface
- IWMPControls3 interface Windows Media Player , currentPositionTimecode property
topic_type:
- apiref
api_name:
- IWMPControls3.currentPositionTimecode
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls3::currentPositionTimecode property

The **currentPositionTimecode** property gets or sets the current position in the current media item using a time code format. This property currently supports SMPTE time code.

## Syntax


```CSharp
public System.String currentPositionTimecode {get; set;}
```


```VB

Public Property currentPositionTimecode As System.String
```





## Property value

A **System.String** that is the SMPTE time code.

## Remarks

SMPTE time code provides a standard way of identifying an individual video frame, which is useful for synchronizing playback. If a digital media file supports SMPTE time code, Windows Media Player can retrieve the current time code position information or seek to a video frame identified by a particular time code.

SMPTE time code identifies a particular frame by the number of hours, minutes, seconds, and frames that separate it from a particular reference frame the frame designated as time zero. Usually the time zero frame is the start of the file and a particular SMPTE time code value represents the elapsed time since the start of the file.

The time code is in the format \[*range*\]*hh*:*mm*:*ss*.*ff* where \[*range*\] represents the range, hh represents hours, *mm* represents minutes, *ss* represents seconds, and *ff* represents frames. When setting a value for **currentPositionTimecode**, you must include all eight digits, using zeros as placeholders.

\[*range*\] corresponds to the **wRange** member of the Windows Media Format **WMT\_TIMECODE\_EXTENSION\_DATA** structure. For more information about time code ranges, see the Windows Media Format SDK.

Setting and getting **currentPositionTimecode** is supported only for files that contain SMPTE time code information.

## Examples

The following code example specifies **currentPositionTimecode** as 1 hour, zero minutes, 30 seconds, and 5 frames. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Cast the interface returned by player.Ctlcontrols to an IWMPControls3 interface
// so that you can use the currentPositionTimecode property.
WMPLib.IWMPControls3 controls = (WMPLib.IWMPControls3)player.Ctlcontrols;

// Seek to a frame using SMPTE time code.
controls.currentPositionTimecode = "[00000]01:00:30.05";
```


```VB

' Cast the interface returned by player.Ctlcontrols to an IWMPControls3 interface
&#39; so that you can use the currentPositionTimecode property.
Dim controls As WMPLib.IWMPControls3 = player.Ctlcontrols

&#39; Seek to a frame using SMPTE time code.
Controls.currentPositionTimecode = &quot;[00000]01:00:30.05&quot;
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls3 Interface (VB and C#)**](iwmpcontrols3--vb-and-c.md)
</dt> </dl>

 

 





