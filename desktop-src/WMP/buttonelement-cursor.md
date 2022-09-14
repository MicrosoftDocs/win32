---
title: BUTTONELEMENT.cursor
description: The cursor attribute specifies or retrieves the value of the BUTTONELEMENT cursor that appears when the mouse is over the BUTTONELEMENT.
ms.assetid: 29e7fadb-30d8-40e4-9a64-6b6f45eac80a
keywords:
- BUTTONELEMENT.cursor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.cursor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONELEMENT.cursor

The **cursor** attribute specifies or retrieves the value of the **BUTTONELEMENT** cursor that appears when the mouse is over the **BUTTONELEMENT**.

``` syntax
        elementID.cursor
```

## Possible Values

This attribute is a read/write **String**.



| Value            | Description                                                                                 |
|------------------|---------------------------------------------------------------------------------------------|
| system           | Default. Platform-dependent cursor (usually an arrow).                                      |
| hand             | Hand.                                                                                       |
| help             | Arrow with question mark indicating Help is available.                                      |
| sizeall          | Four-pointed arrow pointing north, south, east, and west.                                   |
| sizenesw         | Double-pointed arrow pointing northeast and southwest.                                      |
| sizens           | Double-pointed arrow pointing north and south.                                              |
| sizenwse         | Double-pointed arrow pointing northwest and southeast.                                      |
| sizewe           | Double-pointed arrow pointing west and east.                                                |
| uparrow          | Vertical arrow pointing upward.                                                             |
| \*.ani or \*.cur | Any .ani or .cur file (must be in the same directory as the .wms file or in the .wmz file). |



 

## Remarks

If an invalid value is specified, the previous value is maintained.

Cursor file name paths are ignored, so the cursor file must reside in the default directory.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> </dl>

 

 





