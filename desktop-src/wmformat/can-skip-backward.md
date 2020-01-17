---
title: Can_Skip_Backward
description: The Can\_Skip\_Backward attribute is a file-level attribute indicating whether you can skip to the previous item in the server-side playlist.
ms.assetid: 91a8cfee-ccb6-4e0e-90f0-2e134fee56d1
keywords:
- Can_Skip_Backward windows Media Format
topic_type:
- apiref
api_name:
- Can_Skip_Backward
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Can\_Skip\_Backward

The **Can\_Skip\_Backward** attribute is a file-level attribute indicating whether you can skip to the previous item in the server-side playlist.

## Global Constant

g\_wszWMSkipBackward

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




