---
title: LibraryDisconnect Event of the AxWindowsMediaPlayer Object
description: The LibraryDisconnect event occurs when a library is no longer available.
ms.assetid: 053d914a-dcd9-4fd6-a789-10c26147d08a
keywords:
- LibraryDisconnect Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- LibraryDisconnect Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# LibraryDisconnect Event of the AxWindowsMediaPlayer Object

The LibraryDisconnect event occurs when a library is no longer available.

``` syntax
[C#]
private void player_LibraryDisconnect(
  object sender,
  _WMPOCXEvents_LibraryDisconnectEvent e
)

[Visual Basic]
Private Sub player_LibraryDisconnect(  
   sender As Object,  
   e As _WMPOCXEvents_LibraryDisconnectEvent
) Handles player.LibraryDisconnect
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_LibraryDisconnectEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_LibraryDisconnectEvent**, which contains the following property related to this event.



| Property | Description                                                                                   |
|----------|-----------------------------------------------------------------------------------------------|
| pLibrary | **WMPLib.IWMPLibrary**The interface that represents the library that disconnected.<br/> |



 

## Remarks

This event does not occur for the local library.

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11<br/>                                                                                         |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> </dl>

 

 





