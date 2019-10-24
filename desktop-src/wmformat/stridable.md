---
title: Stridable
description: The Stridable attribute is a file-level attribute that specifies whether a reading application can fast forward and rewind the content.
ms.assetid: 9e03025a-e2ab-47ba-8426-a573d85be6f6
keywords:
- Stridable windows Media Format
topic_type:
- apiref
api_name:
- Stridable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Stridable

The **Stridable** attribute is a file-level attribute that specifies whether a reading application can fast forward and rewind the content.

## Global Constant

g\_wszWMStridable

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




