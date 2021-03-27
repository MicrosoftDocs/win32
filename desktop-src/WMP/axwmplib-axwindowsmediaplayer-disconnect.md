---
title: Disconnect Event of the AxWindowsMediaPlayer Object
description: The Disconnect event is reserved for future use.
ms.assetid: 3baecc6c-e772-4269-96c1-900be270543e
keywords:
- Disconnect Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- Disconnect Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# Disconnect Event of the AxWindowsMediaPlayer Object

The Disconnect event is reserved for future use.

``` syntax
[C#]
private void player_Disconnect(
  object sender,
  _WMPOCXEvents_DisconnectEvent e
)

[Visual Basic]
Private Sub player_Disconnect(  
  sender As Object,
  e As _WMPOCXEvents_DisconnectEvent
) Handles player.Disconnect
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_DisconnectEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_DisconnectEvent**, which contains the following property related to this event.



| Property | Description                               |
|----------|-------------------------------------------|
| result   | **System.Int32**Not supported.<br/> |



 

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

 

 





