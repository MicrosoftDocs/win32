---
title: PositionChange Event of the AxWindowsMediaPlayer Object
description: The PositionChange event occurs when the current playback position within the media item has been changed.
ms.assetid: 92d469b9-813a-4148-be68-0fcef2e41491
keywords:
- PositionChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- PositionChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PositionChange Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The PositionChange event occurs when the current playback position within the media item has been changed.

``` syntax
[C#]
private void player_PositionChange(
  object sender,
  _WMPOCXEvents_PositionChangeEvent e
)

[Visual Basic]
Private Sub player_PositionChange(  
  sender As Object,
  e As _WMPOCXEvents_PositionChangeEvent
) Handles player.PositionChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_PositionChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_PositionChangeEvent**, which contains the following properties related to this event.



| Property    | Description                                         |
|-------------|-----------------------------------------------------|
| oldPosition | System.DoubleSpecifies the old position.<br/> |
| newPosition | System.DoubleSpecifies the new position.<br/> |



 

## Remarks

This event is not raised routinely during playback. It only occurs when something actively changes the current position of the playing media item, such as when the user moves the seek handle or when code is executed that specifies a value for IWMPControls.**currentPosition**.

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPControls.currentPosition (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-currentposition--vb-and-c.md)
</dt> </dl>

 

 





