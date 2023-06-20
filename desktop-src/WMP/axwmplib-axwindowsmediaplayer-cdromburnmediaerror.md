---
title: CdromBurnMediaError Event of the AxWindowsMediaPlayer Object
description: The CdromBurnMediaError event occurs when an error happens while burning an individual media item to a CD.
ms.assetid: 0847a8a2-1fef-41a0-affb-9fa6bd10b925
keywords:
- CdromBurnMediaError Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromBurnMediaError Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CdromBurnMediaError Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The CdromBurnMediaError event occurs when an error happens while burning an individual media item to a CD.

``` syntax
[C#]
private void player_CdromBurnMediaError(
  object sender,
  _WMPOCXEvents_CdromBurnMediaErrorEvent e
)

[Visual Basic]
Private Sub player_CdromBurnMediaError(
  sender As Object,
  e As _WMPOCXEvents_CdromBurnMediaErrorEvent
) Handles player.CdromBurnMediaError
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_CdromBurnMediaErrorEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_CdromBurnMediaErrorEvent**, which contains the following properties related to this event.



| Property   | Description                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| pCdromBurn | WMPLib.IWMPCdromBurnThe interface that represents the burning operation that raised the error.<br/>               |
| pMedia     | System.ObjectThe media item that raised the error. You can cast this to an IWMPMedia interface to access it.<br/> |



 

## Remarks

To capture generic errors, handle the AxWMPLib.\_WMPOCXEvents\_CdromBurnError event.

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

[**AxWindowsMediaPlayer.CdromBurnError Event (VB and C#)**](axwmplib-axwindowsmediaplayer-cdromburnerror.md)
</dt> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





