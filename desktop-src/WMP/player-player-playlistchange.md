---
title: Player.PlaylistChange event
description: The PlaylistChange event occurs when a playlist changes. | Player.PlaylistChange event
ms.assetid: 09ab0560-e18d-4ee8-a649-2b2468b40c31
keywords:
- PlaylistChange event Windows Media Player
- PlaylistChange event Windows Media Player , Player class
- Player class Windows Media Player , PlaylistChange event
topic_type:
- apiref
api_name:
- Player.PlaylistChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.PlaylistChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PlaylistChange** event occurs when a playlist changes.

## Syntax


```JScript
Player.PlaylistChange(
  Playlist,
  change
)
```



## Parameters

<dl> <dt>

*Playlist* 
</dt> <dd>

**Playlist** object which changed.

</dd> <dt>

*change* 
</dt> <dd>

**Number** (**long**) indicating the type of change that occurred to the playlist. Contains one of the following values.



| Number | Name          |
|--------|---------------|
| 0      | Unknown       |
| 1      | Clear         |
| 2      | InfoChange    |
| 3      | Move          |
| 4      | Delete        |
| 5      | Insert        |
| 6      | Append        |
| 7      | Not supported |
| 8      | NameChange    |
| 9      | Not supported |
| 10     | Sort          |



 

The C-style enumeration constant can be derived by prefixing the name value with "wmplc". For example, the constant for the Move state is **wmplcMove**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

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
</dt> </dl>

 

 





