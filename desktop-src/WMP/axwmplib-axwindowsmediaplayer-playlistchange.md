---
title: PlaylistChange Event of the AxWindowsMediaPlayer Object
description: The PlaylistChange event occurs when a playlist changes. | PlaylistChange Event of the AxWindowsMediaPlayer Object
ms.assetid: e4166d81-a205-401a-94c4-a1619e764647
keywords:
- PlaylistChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistChange Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The PlaylistChange event occurs when a playlist changes.

``` syntax
[C#]
private void player_PlaylistChange(
  object sender,
  _WMPOCXEvents_PlaylistChangeEvent e
)

[Visual Basic]
Private Sub player_PlaylistChange(
  sender As Object,
  e As _WMPOCXEvents_PlaylistChangeEvent
) Handles player.PlaylistChange
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_PlaylistChangeEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_PlaylistChangeEvent**, which contains the following properties related to this event.



| Property     | Description                                                                                                                   |
|--------------|-------------------------------------------------------------------------------------------------------------------------------|
| **playlist** | System.ObjectThe object which changed. You can cast this to an IWMPPlaylist interface to access it.<br/>                |
| **change**   | WMPLib.WMPPlaylistChangeEventTypeAn enumeration value indicating the type of change that occurred to the playlist.<br/> |



 

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

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





