---
title: ErrorItem.customUrl
description: The customURL property retrieves the URL of a website that displays specific information about codec download failure.
ms.assetid: 51028f45-2ce6-4e57-86bd-d7c2d8fb3af8
keywords:
- ErrorItem.customUrl Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.customUrl
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ErrorItem.customUrl

The **customURL** property retrieves the URL of a website that displays specific information about codec download failure.

``` syntax
player.error.item(
        index
        ).customURL
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

**Windows Media Player 10 Mobile:** This property always returns an empty string.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





