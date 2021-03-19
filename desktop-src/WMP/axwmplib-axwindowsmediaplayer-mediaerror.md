---
title: MediaError Event of the AxWindowsMediaPlayer Object
description: The MediaError event occurs when a media object has an error condition.
ms.assetid: a1fb3422-85c4-4856-951a-332517599984
keywords:
- MediaError Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaError Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# MediaError Event of the AxWindowsMediaPlayer Object

The MediaError event occurs when a media object has an error condition.

``` syntax
[C#]
private void player_MediaError(
  object sender,
  _WMPOCXEvents_MediaErrorEvent e
)

[Visual Basic]
Private Sub player_MediaError(
  sender As Object,
  e As _WMPOCXEvents_MediaErrorEvent
) Handles player.MediaError
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_MediaErrorEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_MediaErrorEvent**, which contains the following property related to this event.



| Property     | Description                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| pMediaObject | System.ObjectObject that has an error condition. You can cast this to an IWMPMedia interface to access it.<br/> |



 

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

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





