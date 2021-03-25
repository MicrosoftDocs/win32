---
title: COLUMN.columnID
description: The columnID attribute specifies or retrieves a column ID in the PLAYLIST control.
ms.assetid: c7b51f0b-e347-46be-a26d-aaa0bce83e0c
keywords:
- COLUMN.columnID Windows Media Player
topic_type:
- apiref
api_name:
- COLUMN.columnID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# COLUMN.columnID

The **columnID** attribute specifies or retrieves a column ID in the **PLAYLIST** control.

``` syntax
        elementID.columnID
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

The **columnID** values are the same values used with the **getItemInfo** method on a **Media** object. A list can be obtained by using the *Media*.**attributeCount** property to determine the number of attributes available for a given **Media** object. Index numbers can then be used with the *Media*.**getAttributeName** method to determine the names of the attributes, which can in turn be passed to *Media*.**getItemInfo**. The **columnID** property can only be set to these values, with the exception of some values that may not be returned by *Media*.**getAttributeName**. These values are listed below.



| Value     | Description                                                                        |
|-----------|------------------------------------------------------------------------------------|
| name      | Displays the name of the **Media** object.                                         |
| duration  | Displays the duration of the **Media** object.                                     |
| sourceURL | Displays the URL of the **Media** object.                                          |
| status    | Displays the status of copying files.                                              |
| size      | Displays the size of the file that the **Media** object represents.                |
| extension | Displays the file name extension of the file that the **Media** object represents. |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**COLUMN Element**](column-element.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.attributeCount**](media-attributecount.md)
</dt> <dt>

[**Media.getAttributeName**](media-getattributename.md)
</dt> <dt>

[**Media.getItemInfo**](media-getiteminfo.md)
</dt> </dl>

 

 





