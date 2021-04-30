---
title: Warning Event of the AxWindowsMediaPlayer Object
description: The Warning event is reserved for future use.
ms.assetid: 3de63756-2726-4864-8988-fd614f23bcad
keywords:
- Warning Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- Warning Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# Warning Event of the AxWindowsMediaPlayer Object

The Warning event is reserved for future use.

``` syntax
[C#]
private void player_Warning(
  object sender,
  _WMPOCXEvents_WarningEvent e
)

[Visual Basic]
Private Sub player_Warning(
  sender As Object,
  e As _WMPOCXEvents_WarningEvent
) Handles player.Warning
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_WarningEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_WarningEvent**, which contains the following properties related to this event.



| Property    | Description                                |
|-------------|--------------------------------------------|
| warningType | **System.Int32**Not supported.<br/>  |
| param       | **System.Int32**Not supported.<br/>  |
| description | **System.String**Not supported.<br/> |



 

## Remarks

This event is reserved for future use.

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

 

 





