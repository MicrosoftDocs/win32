---
title: Player.status
description: The status property retrieves a value indicating the status of Windows Media Player.
ms.assetid: 781c44d0-15cf-4be2-9e83-76706ce1cb85
keywords:
- Player.status Windows Media Player
topic_type:
- apiref
api_name:
- Player.status
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.status

The **status** property retrieves a value indicating the status of Windows Media Player.

## Syntax

*player* .**status**

## Possible Values

This property is a read-only String.

## Remarks

The values contained in this property are subject to change at any time, and should be used for display purposes only.

The **StatusChange** event is fired whenever this property changes value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later.<br/>                                      |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.StatusChange Event**](player-player-statuschange.md)
</dt> </dl>

 

 





