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
ms.date: 05/31/2018
---

# Settings.balance

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

 

 





