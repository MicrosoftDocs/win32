---
title: HasVideo
description: The HasVideo attribute is a file-level attribute specifying whether the file contains any video streams.
ms.assetid: 206ac048-c119-4d80-97c5-1623a3d6aa5b
keywords:
- HasVideo windows Media Format
topic_type:
- apiref
api_name:
- HasVideo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HasVideo

The **HasVideo** attribute is a file-level attribute specifying whether the file contains any video streams.

## Global Constant

g\_wszWMHasVideo

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




