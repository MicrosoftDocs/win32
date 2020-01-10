---
title: Duration
description: The Duration attribute contains the playing duration of the file, in 100-nanosecond units.
ms.assetid: 1d72f826-4087-45f5-a5b9-f31c4e98e9b1
keywords:
- Duration windows Media Format
topic_type:
- apiref
api_name:
- Duration
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Duration

The **Duration** attribute contains the playing duration of the file, in 100-nanosecond units.

## Global Constant

g\_wszWMDuration

## Data Type

**WMT\_TYPE\_QWORD**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




