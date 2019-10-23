---
title: HasImage
description: The HasImage attribute is a file-level attribute specifying whether the file contains any image streams.
ms.assetid: 3b67288f-4f04-47a4-91ca-c456107d9d7b
keywords:
- HasImage windows Media Format
topic_type:
- apiref
api_name:
- HasImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HasImage

The **HasImage** attribute is a file-level attribute specifying whether the file contains any image streams.

## Global Constant

g\_wszWMHasImage

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




