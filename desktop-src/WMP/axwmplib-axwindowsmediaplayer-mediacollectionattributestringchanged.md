---
title: MediaCollectionAttributeStringChanged Event of the AxWindowsMediaPlayer Object
description: The MediaCollectionAttributeStringChanged event occurs when an attribute value in the library is changed. | MediaCollectionAttributeStringChanged Event of the AxWindowsMediaPlayer Object
ms.assetid: f5b91399-42b7-4202-9b65-caa9b15847b9
keywords:
- MediaCollectionAttributeStringChanged Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaCollectionAttributeStringChanged Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollectionAttributeStringChanged Event of the AxWindowsMediaPlayer Object

The MediaCollectionAttributeStringChanged event occurs when an attribute value in the library is changed.

``` syntax
[C#]
private void player_MediaCollectionAttributeStringChanged(
  object sender,
  _WMPOCXEvents_MediaCollectionAttributeStringChangedEvent e
)

[Visual Basic]
Private Sub player_MediaCollectionAttributeStringChanged(
  sender As Object,
  e As _WMPOCXEvents_MediaCollectionAttributeStringChangedEvent
) Handles player.MediaCollectionAttributeStringChanged
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringChangedEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringChangedEvent**, which contains the following properties related to this event.



| Property         | Description                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bstrAttribName   | System.StringSpecifies the name of the attribute. For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).<br/> |
| bstrOldAttribVal | System.StringSpecifies the old value of the attribute.<br/>                                                                                                                            |
| bstrNewAttribVal | System.StringSpecifies the new value of the attribute.<br/>                                                                                                                            |



 

## Remarks

When a user modifies library metadata, the media collection is updated and this event fires for each attribute changed.

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.mediaCollection (VB and C#)**](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





