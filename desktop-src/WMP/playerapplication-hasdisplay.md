---
title: PlayerApplication.hasDisplay
description: The hasDisplay property retrieves a value indicating whether video can display through the remoted Player control.
ms.assetid: f90c5470-f985-4b98-823f-7395f89b238b
keywords:
- PlayerApplication.hasDisplay Windows Media Player
topic_type:
- apiref
api_name:
- PlayerApplication.hasDisplay
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# PlayerApplication.hasDisplay

The **hasDisplay** property retrieves a value indicating whether video can display through the remoted Player control.

## Syntax

*playerApplication*.**hasDisplay**

## Possible Values

This property is a read-only **Boolean**.

## Remarks

This property is used only when remoting the Windows Media Player control.

Several Windows Media Player controls can be running remotely at the same time, but video can only display in one location at a time, either in the full mode of the Player or in one of the remoted Windows Media Player controls. Use this property to determine whether the current control is the one through which video can be displayed.

**Windows Media Player 10 Mobile:** This property always returns **true**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**PlayerApplication Object**](playerapplication-object.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





