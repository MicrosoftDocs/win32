---
title: Settings.volume
description: The volume property specifies or retrieves the current volume.
ms.assetid: 60143eff-3a34-43eb-a86d-641c2a5cfc01
keywords:
- Settings.volume Windows Media Player
topic_type:
- apiref
api_name:
- Settings.volume
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.volume

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **volume** property specifies or retrieves the current volume.

## Syntax

player.settings.volume

## Possible Values

This property is a read/write **Number** (**long**) ranging from 0 to 100.

## Remarks

Zero specifies no volume and 100 specifies full volume. If no value is specified for this property, it defaults to the last volume setting established for the player.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





