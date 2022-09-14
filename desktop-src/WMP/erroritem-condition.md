---
title: ErrorItem.condition
description: The condition property retrieves a value indicating the condition for the error.
ms.assetid: efb54b48-cfaa-479f-9ee6-ce6724dca24c
keywords:
- ErrorItem.condition Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.condition
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ErrorItem.condition

The **condition** property retrieves a value indicating the condition for the error.

``` syntax
player.error.item(
        index
        ).condition
      
```

## Possible Values

This property is a read-only **Number** (**long**) that represents the condition code.

## Remarks

The condition code is a value that is used by Microsoft to provide additional information for technical support personnel.

**Windows Media Player 10 Mobile:** This property always returns 0.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





