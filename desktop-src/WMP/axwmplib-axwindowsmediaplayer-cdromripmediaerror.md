---
title: CdromRipMediaError Event of the AxWindowsMediaPlayer Object
description: The CdromRipMediaError event occurs when an error happens while ripping an individual track from a CD.
ms.assetid: 542d0184-d893-4b98-903e-339909276fd6
keywords:
- CdromRipMediaError Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromRipMediaError Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# CdromRipMediaError Event of the AxWindowsMediaPlayer Object

The CdromRipMediaError event occurs when an error happens while ripping an individual track from a CD.

``` syntax
[C#]
private void player_CdromRipMediaError(
  object sender,
  _WMPOCXEvents_CdromRipMediaErrorEvent e
)

[Visual Basic]
Private Sub player_CdromRipMediaError( 
  sender As Object,
  e As _WMPOCXEvents_CdromRipMediaErrorEvent
) Handles player.CdromRipMediaError
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CdromRipMediaErrorEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CdromRipMediaErrorEvent**, which contains the following properties related to this event.



| Property  | Description                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| pCdromRip | WMPLib.IWMPCdromRipThe interface that represents the ripping operation that raised the error.<br/>                |
| pMedia    | System.ObjectThe media item that raised the error. You can cast this to an IWMPMedia interface to access it.<br/> |



 

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

[**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





