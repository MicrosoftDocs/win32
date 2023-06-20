---
title: Settings.balance
description: The balance property specifies or retrieves the current stereo balance.
ms.assetid: 26f04989-a1b1-4aec-8a15-c4e3737a4e62
keywords:
- Settings.balance Windows Media Player
topic_type:
- apiref
api_name:
- Settings.balance
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.balance

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **balance** property specifies or retrieves the current stereo balance.

## Syntax

player.settings.balance

## Possible Values

This property is a read/write **Number** (**long**). Values range from  100 to 100, with a default value of zero.

## Remarks

The value zero indicates that the audio plays at equal volume on both left and right channels. A value of  100 indicates that audio plays only on the left channel. A value of 100 indicates that audio plays only on the right channel.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





