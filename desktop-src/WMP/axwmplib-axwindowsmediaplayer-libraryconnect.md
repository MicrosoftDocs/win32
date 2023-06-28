---
title: LibraryConnect Event of the AxWindowsMediaPlayer Object
description: The LibraryConnect event occurs when a library becomes available.
ms.assetid: f67243ce-0e25-43a7-b754-6b0e80d72055
keywords:
- LibraryConnect Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- LibraryConnect Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# LibraryConnect Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The LibraryConnect event occurs when a library becomes available.

``` syntax
[C#]
private void player_LibraryConnect(
  object sender,
  _WMPOCXEvents_LibraryConnectEvent e
)

[Visual Basic]
Private Sub player_LibraryConnect(  
  sender As Object,
  e As _WMPOCXEvents_LibraryConnectEvent
) Handles player.LibraryConnect
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_LibraryConnectEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_LibraryConnectEvent**, which contains the following property related to this event.



| Property | Description                                                                                |
|----------|--------------------------------------------------------------------------------------------|
| pLibrary | **WMPLib.IWMPLibrary**The interface that represents the library that connected.<br/> |



 

## Remarks

This event does not occur for the local library.

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

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> </dl>

 

 





