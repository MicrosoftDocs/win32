---
title: PlaylistCollectionPlaylistSetAsDeleted Event of the AxWindowsMediaPlayer Object
description: The PlaylistCollectionPlaylistSetAsDeleted event is reserved for future use.
ms.assetid: 6c0a4d2c-e965-4a88-acd4-2a2a12265e36
keywords:
- PlaylistCollectionPlaylistSetAsDeleted Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistCollectionPlaylistSetAsDeleted Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# PlaylistCollectionPlaylistSetAsDeleted Event of the AxWindowsMediaPlayer Object

The PlaylistCollectionPlaylistSetAsDeleted event is reserved for future use.

``` syntax
[C#]
private void player_PlaylistCollectionPlaylistSetAsDeleted(
  object sender,
  _WMPOCXEvents_PlaylistCollectionPlaylistSetAsDeletedEvent e
)

[Visual Basic]
Private Sub player_PlaylistCollectionPlaylistSetAsDeleted(
  sender As Object,
  e As _WMPOCXEvents_PlaylistCollectionPlaylistSetAsDeletedEvent
) Handles player.PlaylistCollectionPlaylistSetAsDeleted
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_PlaylistCollectionPlaylistSetAsDeletedEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_PlaylistCollectionPlaylistSetAsDeletedEvent**, which contains the following properties related to this event.



| Property         | Description                                 |
|------------------|---------------------------------------------|
| bstrPlaylistName | **System.String**Not supported.<br/>  |
| varfIsDeleted    | **System.Boolean**Not supported.<br/> |



 

## Remarks

This event is reserved for future use.

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





