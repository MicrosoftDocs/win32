---
title: KeyPress Event of the AxWindowsMediaPlayer Object
description: The KeyPress event occurs when a key is pressed and released. | KeyPress Event of the AxWindowsMediaPlayer Object
ms.assetid: 73ecd6f9-1b58-4e28-ad1b-2d930a235e1d
keywords:
- KeyPress Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- KeyPress Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# KeyPress Event of the AxWindowsMediaPlayer Object

The KeyPress event occurs when a key is pressed and released.

``` syntax
[C#]
private void player_KeyPressEvent(
  object sender,
  _WMPOCXEvents_KeyPressEvent e
)

[Visual Basic]
Private Sub player_KeyPressEvent(  
  sender As Object,  
  e As _WMPOCXEvents_KeyPressEvent
) Handles player.KeyPressEvent
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_KeyPressEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_KeyPressEvent**, which contains the following property related to this event.



| Property      | Description                                                                        |
|---------------|------------------------------------------------------------------------------------|
| **nKeyAscii** | System.Int16Specifies the standard numeric ANSI code for the character.<br/> |



 

## Remarks

This event occurs when the keystroke results in any printable keyboard character, the CTRL key combined with a character from the standard alphabet or one of a few special characters, and the ENTER or BACKSPACE key.

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

 

 





