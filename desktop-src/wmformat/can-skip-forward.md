---
title: Can_Skip_Forward
description: The Can\_Skip\_Forward attribute is a file-level attribute indicating whether you can skip to the next item in the server-side playlist.
ms.assetid: f84f0a6a-1a52-4189-9e65-e0103f98f7ed
keywords:
- Can_Skip_Forward windows Media Format
topic_type:
- apiref
api_name:
- Can_Skip_Forward
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Can\_Skip\_Forward

The **Can\_Skip\_Forward** attribute is a file-level attribute indicating whether you can skip to the next item in the server-side playlist.

## Global Constant

g\_wszWMSkipForward

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




