---
title: MediaCollectionAttributeStringAdded Event of the AxWindowsMediaPlayer Object
description: The MediaCollectionAttributeStringAdded event occurs when an attribute value is added to the library. | MediaCollectionAttributeStringAdded Event of the AxWindowsMediaPlayer Object
ms.assetid: b14db0ce-bd78-4e28-a42c-1a231c29da2b
keywords:
- MediaCollectionAttributeStringAdded Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaCollectionAttributeStringAdded Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollectionAttributeStringAdded Event of the AxWindowsMediaPlayer Object

The MediaCollectionAttributeStringAdded event occurs when an attribute value is added to the library.

``` syntax
[C#]
private void player_MediaCollectionAttributeStringAdded(
  object sender,
  _WMPOCXEvents_MediaCollectionAttributeStringAddedEvent e
)

[Visual Basic]
Private Sub player_MediaCollectionAttributeStringAdded(
  sender As Object,
  e As _WMPOCXEvents_MediaCollectionAttributeStringAddedEvent
) Handles player.MediaCollectionAttributeStringAdded
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringAddedEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringAddedEvent**, which contains the following properties related to this event.



| Property           | Description                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **bstrAttribName** | System.StringSpecifies the name of the attribute. For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).<br/> |
| bstrAttribVal      | System.StringSpecifies the value of the attribute.<br/>                                                                                                                                |



 

## Remarks

When a media item is added to the library, its metadata is added to the media collection and this event is fired for each attribute added.

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

 

 





