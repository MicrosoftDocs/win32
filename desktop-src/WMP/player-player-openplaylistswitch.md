---
title: Player.OpenPlaylistSwitch event
description: The OpenPlaylistSwitch event occurs when a title on a DVD begins playing. | Player.OpenPlaylistSwitch event
ms.assetid: 97d69716-602f-4522-b743-83f2dbc852a2
keywords:
- OpenPlaylistSwitch event Windows Media Player
- OpenPlaylistSwitch event Windows Media Player , Player class
- Player class Windows Media Player , OpenPlaylistSwitch event
topic_type:
- apiref
api_name:
- Player.OpenPlaylistSwitch
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.OpenPlaylistSwitch event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **OpenPlaylistSwitch** event occurs when a title on a DVD begins playing.

## Syntax


```JScript
Player.OpenPlaylistSwitch(
  pItem
)
```



## Parameters

<dl> <dt>

*pItem* 
</dt> <dd>

**Playlist** object representing the title.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





