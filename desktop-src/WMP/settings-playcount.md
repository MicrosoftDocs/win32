---
title: Settings.playCount
description: The playCount property specifies or retrieves the number of times a media item will play.
ms.assetid: e15d97c6-312a-414d-9b3c-2a15e9081b35
keywords:
- Settings.playCount Windows Media Player
topic_type:
- apiref
api_name:
- Settings.playCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.playCount

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playCount** property specifies or retrieves the number of times a media item will play.

## Syntax

player.settings.playCount

## Possible Values

This property is a read/write **Number** (**long**) with a minimum value of one and a default value of one.

**Windows Media Player 10 Mobile**: This property is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





