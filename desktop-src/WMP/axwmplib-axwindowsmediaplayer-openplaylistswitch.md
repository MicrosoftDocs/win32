---
title: OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object
description: The OpenPlaylistSwitch event occurs when a title on a DVD begins playing. | OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object
ms.assetid: 0b9c37a3-1349-48bd-8e1a-aba286c82abf
keywords:
- OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The OpenPlaylistSwitch event occurs when a title on a DVD begins playing.

``` syntax
[C#]
private void player_OpenPlaylistSwitch(
  object sender,
  _WMPOCXEvents_OpenPlaylistSwitchEvent e
)

[Visual Basic]
Private Sub player_OpenPlaylistSwitch(
  sender As Object,
  e As _WMPOCXEvents_OpenPlaylistSwitchEvent
) Handles player.OpenPlaylistSwitch
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_OpenPlaylistSwitchEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_OpenPlaylistSwitchEvent**, which contains the following property related to this event.



| Property  | Description                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------|
| **pItem** | System.ObjectObject representing the title. You can cast this to an IWMPPlaylist interface to access it.<br/> |



 

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

 

 





