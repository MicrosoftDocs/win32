---
title: FileSize
description: The FileSize attribute contains the size of the file in bytes.
ms.assetid: 524843f7-40b4-40a9-928a-fa0aa00f31ac
keywords:
- FileSize windows Media Format
topic_type:
- apiref
api_name:
- FileSize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# FileSize

The **FileSize** attribute contains the size of the file in bytes.

## Global Constant

g\_wszWMFileSize

## Data Type

**WMT\_TYPE\_QWORD**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




