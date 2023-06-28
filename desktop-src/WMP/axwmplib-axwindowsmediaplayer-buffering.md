---
title: Buffering Event of the AxWindowsMediaPlayer Object
description: The Buffering event occurs when the Windows Media Player control begins or ends buffering or downloading. | Buffering Event of the AxWindowsMediaPlayer Object
ms.assetid: ad152c4d-1c91-4da1-bec0-46f89f3b8c79
keywords:
- Buffering Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- Buffering Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Buffering Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Buffering event occurs when the Windows Media Player control begins or ends buffering or downloading.

``` syntax
[C#]
private void player_Buffering(
  object sender,
  _WMPOCXEvents_BufferingEvent e
)

[Visual Basic]
Private Sub player_Buffering(
  sender As Object,
  e As _WMPOCXEvents_BufferingEvent
) Handles player.Buffering
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_BufferingEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_BufferingEvent**, which contains the following property related to this event.



| Property | Description                                                                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start    | System.BooleanSpecifies whether buffering has begun or ended. A value of true indicates that it has begun; a value of false indicates that it has ended.<br/> |



 

## Remarks

Use this event to determine when buffering or downloading starts or stops. You can use the same event block for both cases and test *IWMPNetwork*.**bufferingProgress** and *IWMPNetwork*.**downloadProgress** to determine whether Windows Media Player is currently buffering or downloading content.

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

[**IWMPNetwork.bufferingProgress (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-bufferingprogress--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork.downloadProgress (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-downloadprogress--vb-and-c.md)
</dt> </dl>

 

 





