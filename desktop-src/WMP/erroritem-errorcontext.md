---
title: ErrorItem.errorContext
description: The errorContext property retrieves a value indicating the context of the error.
ms.assetid: 700d2bf0-dd3b-4211-99ea-58f952cf24b0
keywords:
- ErrorItem.errorContext Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.errorContext
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ErrorItem.errorContext

The **errorContext** property retrieves a value indicating the context of the error.

``` syntax
player.error.item(
        index
        ).errorContext
```

## Possible Values

This property is a read-only **String** that represents the error context code.

## Remarks

The error context is information that is used by Microsoft to provide additional information for technical support personnel.

**Windows Media Player 10 Mobile:** This property always returns an empty string.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/>                               |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





