---
title: MediaCollectionMediaAdded Event of the AxWindowsMediaPlayer Object
description: The MediaCollectionMediaAdded event occurs when a media item is added to the local library. | MediaCollectionMediaAdded Event of the AxWindowsMediaPlayer Object
ms.assetid: ba1779f6-a212-44f4-b52a-c88e22aebcce
keywords:
- MediaCollectionMediaAdded Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaCollectionMediaAdded Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollectionMediaAdded Event of the AxWindowsMediaPlayer Object

The MediaCollectionMediaAdded event occurs when a media item is added to the local library.

``` syntax
[C#]
private void player_MediaCollectionMediaAdded(
  object sender,
  _WMPOCXEvents_MediaCollectionMediaAddedEvent e
)

[Visual Basic]
Private Sub player_MediaCollectionMediaAdded(
  sender As Object,
  e As _WMPOCXEvents_MediaCollectionMediaAddedEvent
) Handles player.MediaCollectionMediaAdded
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionMediaAddedEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionMediaAddedEvent**, which contains the following property related to this event.



| Property | Description                                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------------------|
| pMedia   | System.ObjectThe media item added to the local library. You can cast this to an IWMPMedia interface to access it.<br/> |



 

## Remarks

This event occurs only for the local library.

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

[**AxWindowsMediaPlayer.mediaCollection (VB and C#)**](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





