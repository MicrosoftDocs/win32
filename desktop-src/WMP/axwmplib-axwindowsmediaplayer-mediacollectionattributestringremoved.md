---
title: MediaCollectionAttributeStringRemoved Event of the AxWindowsMediaPlayer Object
description: The MediaCollectionAttributeStringRemoved event occurs when an attribute value is removed from the library. | MediaCollectionAttributeStringRemoved Event of the AxWindowsMediaPlayer Object
ms.assetid: 2f264416-0bc5-41d0-8863-32c284393082
keywords:
- MediaCollectionAttributeStringRemoved Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaCollectionAttributeStringRemoved Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollectionAttributeStringRemoved Event of the AxWindowsMediaPlayer Object

The MediaCollectionAttributeStringRemoved event occurs when an attribute value is removed from the library.

``` syntax
[C#]
private void player_MediaCollectionAttributeStringRemoved(
  object sender,
  _WMPOCXEvents_MediaCollectionAttributeStringRemovedEvent e
)

[Visual Basic]
Private Sub player_MediaCollectionAttributeStringRemoved(
  sender As Object,
  e As _WMPOCXEvents_MediaCollectionAttributeStringRemovedEvent
) Handles player.MediaCollectionAttributeStringRemoved
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringRemovedEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaCollectionAttributeStringRemovedEvent**, which contains the following properties related to this event.



| Property           | Description                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **bstrAttribName** | System.StringSpecifies the name of the attribute. For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).<br/> |
| bstrAttribVal      | System.StringSpecifies the value of the attribute.<br/>                                                                                                                                |



 

## Remarks

When a media item is removed from the library, its metadata is removed from the **MediaCollection** and this event is fired for each attribute removed.

## Requirements



| Requirement | Value |
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

 

 





