---
title: Click Event of the AxWindowsMediaPlayer Object
description: The Click event occurs when the user clicks a mouse button on a Windows Media Player control.
ms.assetid: 41a719a2-103a-46b5-806d-5c21c4a09e00
keywords:
- Click Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- Click Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Click Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Click event occurs when the user clicks a mouse button on a Windows Media Player control.

``` syntax
[C#]
private void player_OnClick(
  object  sender,
  _WMPOCXEvents_ClickEvent e
);

[Visual Basic]
Private Sub player_OnClick(  
  sender As Object,
  e As WMPOCXEvents_ClickEvent
) Handles player.ClickEvent
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_ClickEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_ClickEvent**, which contains the following properties related to this event.



| Property    | Description                                                                                                                                                                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nButton     | System.Int16A bitfield with bits corresponding to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event.<br/>                                                |
| nShiftState | System.Int16A bitfield with the least significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed.<br/> |
| fX          | System.Int32The x-coordinate of the mouse pointer relative to the upper-left corner of the control.<br/>                                                                                                                                                                                                                 |
| fY          | System.Int32The y-coordinate of the mouse pointer relative to the upper-left corner of the control.<br/>                                                                                                                                                                                                                 |



 

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





