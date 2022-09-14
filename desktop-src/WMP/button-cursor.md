---
title: BUTTON.cursor
description: The cursor attribute specifies or retrieves the cursor that appears when the mouse pointer hovers over the BUTTON.
ms.assetid: 19bdbb23-00e2-45cf-b67d-9ada036b9c3b
keywords:
- BUTTON.cursor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.cursor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.cursor

The **cursor** attribute specifies or retrieves the cursor that appears when the mouse pointer hovers over the **BUTTON**.

``` syntax
        elementID.cursor
```

## Possible Values

This attribute is a read/write **String**.



| Value            | Description                                                                                |
|------------------|--------------------------------------------------------------------------------------------|
| system           | Default. Platform-dependent cursor (usually an arrow).                                     |
| hand             | Hand.                                                                                      |
| help             | Arrow with question mark indicating Help is available.                                     |
| sizeall          | Four-pointed arrow pointing north, south, east, and west.                                  |
| sizenesw         | Double-pointed arrow pointing northeast and southwest.                                     |
| sizens           | Double-pointed arrow pointing north and south.                                             |
| sizenwse         | Double-pointed arrow pointing northwest and southeast.                                     |
| sizewe           | Double-pointed arrow pointing west and east.                                               |
| uparrow          | Vertical arrow pointing upward.                                                            |
| \*.ani or \*.cur | Any .ani or .cur file (must be in the same directory as the .wms file or in the .wmz file) |



 

## Remarks

If the system does not recognize the cursor value specified, the cursor value remains at the previously set value.

Cursor file name paths are ignored, so the cursor file must reside in the default directory.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





