---
title: Player.playerApplication
description: The playerApplication property retrieves the PlayerApplication object when a remoted Windows Media Player control is running.
ms.assetid: 09a8a63f-455f-4f81-8fdb-7de337139dea
keywords:
- Player.playerApplication Windows Media Player
topic_type:
- apiref
api_name:
- Player.playerApplication
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.playerApplication

The **playerApplication** property retrieves the **PlayerApplication** object when a remoted Windows Media Player control is running.

## Syntax

**playerApplication**

## Possible Values

This property is a read-only **PlayerApplication** object or the null value.

## Remarks

This property is used only when remoting the Windows Media Playercontrol. If the value is null, the Windows Media Playercontrol is not embedded in remote mode.

This property is only accessible in C++ code or in script code in skins through the playerApplication global variable.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Global Attributes**](global-attributes.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**PlayerApplication Object**](playerapplication-object.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





