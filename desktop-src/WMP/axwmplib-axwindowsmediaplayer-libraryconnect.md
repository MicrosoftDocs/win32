---
title: LibraryConnect Event of the AxWindowsMediaPlayer Object
description: The LibraryConnect event occurs when a library becomes available.
ms.assetid: f67243ce-0e25-43a7-b754-6b0e80d72055
keywords:
- LibraryConnect Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- LibraryConnect Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# LibraryConnect Event of the AxWindowsMediaPlayer Object

The LibraryConnect event occurs when a library becomes available.

``` syntax
[C#]
private void player_LibraryConnect(
  object sender,
  _WMPOCXEvents_LibraryConnectEvent e
)

[Visual Basic]
Private Sub player_LibraryConnect(  
  sender As Object,
  e As _WMPOCXEvents_LibraryConnectEvent
) Handles player.LibraryConnect
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_LibraryConnectEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_LibraryConnectEvent**, which contains the following property related to this event.



| Property | Description                                                                                |
|----------|--------------------------------------------------------------------------------------------|
| pLibrary | **WMPLib.IWMPLibrary**The interface that represents the library that connected.<br/> |



 

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

 

 





