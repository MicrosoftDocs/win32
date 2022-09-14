---
title: COLUMN.columnResizeMode
description: The columnResizeMode attribute specifies or retrieves the resize mode for this column.
ms.assetid: 95ece2a3-20a6-4b9d-a2eb-fc69fc612f29
keywords:
- COLUMN.columnResizeMode Windows Media Player
topic_type:
- apiref
api_name:
- COLUMN.columnResizeMode
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# COLUMN.columnResizeMode

The **columnResizeMode** attribute specifies or retrieves the resize mode for this column.

``` syntax
        elementID.columnResizeMode
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value          | Description                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------|
| AutosizeHeader | Default. The column resizes to accommodate all data in both the column and the header.                         |
| AutosizeData   | The column resizes to accommodate all data in the column only.                                                 |
| Fixed          | The column is a fixed size.                                                                                    |
| Stretches      | The column resizes to use the remaining space in the **PLAYLIST** control after all other columns are resized. |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**COLUMN Element**](column-element.md)
</dt> </dl>

 

 





