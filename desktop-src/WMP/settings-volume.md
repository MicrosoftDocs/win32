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
ms.date: 05/31/2018
---

# Settings.volume

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

 

 





