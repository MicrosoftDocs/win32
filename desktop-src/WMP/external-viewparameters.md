---
title: External.viewParameters
description: Note This topic describes functionality designed for use by online stores. | External.viewParameters
ms.assetid: 0afabe35-2857-413a-a662-1a76d3fb75fe
keywords:
- External.viewParameters Windows Media Player
topic_type:
- apiref
api_name:
- External.viewParameters
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.viewParameters

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **viewParameters** property retrieves parameters associated with the current view in Windows Media Player.

## Syntax

**window.external.viewParameters**

## Possible Values

This property returns a read-only **String**.

## Remarks

This property retrieves parameters that were previously set by the online store. For example, the online store can specify view parameters in the *ViewParams* parameter of the [changeView](external-changeview.md) method or the *Params* parameter of the [changeViewOnlineList](external-changeviewonlinelist.md) method.

View parameters are not interpreted by Windows Media Player. They are created by the online store and have meaning only to the online store.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





