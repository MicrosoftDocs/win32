---
title: Player.enabled
description: The enabled property specifies or retrieves a value indicating whether the Windows Media Player control is enabled.
ms.assetid: 65fea4d2-3330-4cce-bdaf-fae00304271a
keywords:
- Player.enabled Windows Media Player
topic_type:
- apiref
api_name:
- Player.enabled
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.enabled

The **enabled** property specifies or retrieves a value indicating whether the Windows Media Player control is enabled.

## Syntax

*player* .**enabled**

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                           |
|-------|-------------------------------------------------------|
| true  | Default. The Windows Media Player control is enabled. |
| false | The Windows Media Player control is disabled.         |



 

## Remarks

If **enabled** equals false then during full-screen playback Windows Media Player hides the user controls.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





