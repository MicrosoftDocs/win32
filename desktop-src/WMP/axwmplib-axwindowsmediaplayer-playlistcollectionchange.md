---
title: PlaylistCollectionChange Event of the AxWindowsMediaPlayer Object
description: The PlaylistCollectionChange event occurs when something changes in the playlist collection. | PlaylistCollectionChange Event of the AxWindowsMediaPlayer Object
ms.assetid: 868ee1c6-b740-4614-90ac-961c59091f0f
keywords:
- PlaylistCollectionChange Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistCollectionChange Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollectionChange Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The PlaylistCollectionChange event occurs when something changes in the playlist collection.

``` syntax
[C#]
private void player_PlaylistCollectionChange(
  object sender,
  System.EventArgs e
)

[Visual Basic]
Private Sub player_PlaylistCollectionChange(
  sender As Object,
  e As System.EventArgs
) Handles player.PlaylistCollectionChange
```

## Event Data

This event does not contain data.

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

 

 





