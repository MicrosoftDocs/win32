---
title: Player.CurrentPlaylistItemAvailable event
description: The CurrentPlaylistItemAvailable event occurs when the current playlist becomes available. | Player.CurrentPlaylistItemAvailable event
ms.assetid: 4894e2fc-3464-413f-8abf-8b5e91899946
keywords:
- CurrentPlaylistItemAvailable event Windows Media Player
- CurrentPlaylistItemAvailable event Windows Media Player , Player class
- Player class Windows Media Player , CurrentPlaylistItemAvailable event
topic_type:
- apiref
api_name:
- Player.CurrentPlaylistItemAvailable
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.CurrentPlaylistItemAvailable event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CurrentPlaylistItemAvailable** event occurs when the current playlist becomes available.

## Syntax


```JScript
Player.CurrentPlaylistItemAvailable(
  bstrItemName
)
```



## Parameters

<dl> <dt>

*bstrItemName* 
</dt> <dd>

**String** containing the name of the current playlist item.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The name of the current playlist can be used to retrieve the corresponding **Playlist** object using the *PlaylistCollection*.**getByName** method.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**PlaylistCollection.getByName**](playlistcollection-getbyname.md)
</dt> </dl>

 

 





