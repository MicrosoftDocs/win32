---
title: DoubleClick Event of the AxWindowsMediaPlayer Object
description: The DoubleClick event occurs when the user double-clicks a mouse button on a Windows Media Player control.
ms.assetid: 4f116d8a-1ad5-443a-9c91-66214bbdebcf
keywords:
- DoubleClick Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- DoubleClick Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# DoubleClick Event of the AxWindowsMediaPlayer Object

The DoubleClick event occurs when the user double-clicks a mouse button on a Windows Media Player control.

``` syntax
[C#]
private void player_DoubleClickEvent(
  object sender,
  _WMPOCXEvents_DoubleClickEvent e
)

[Visual Basic]
Private Sub player_DoubleClickEvent(  
  sender As Object,  
  e As _WMPOCXEvents_DoubleClickEvent
) Handles player.DoubleClickEvent
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_DoubleClickEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_DoubleClickEvent**, which contains the following properties related to this event.



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

 

 





