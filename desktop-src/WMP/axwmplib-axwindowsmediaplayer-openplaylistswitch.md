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
ms.date: 05/31/2018
---

# OpenPlaylistSwitch Event of the AxWindowsMediaPlayer Object

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

 

 





