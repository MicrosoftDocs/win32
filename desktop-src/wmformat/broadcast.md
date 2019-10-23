---
title: Broadcast
description: The Broadcast attribute is a file-level attribute indicating whether the content can be broadcast. It is assumed that any content for which no copyright has been assigned can be legally broadcast.
ms.assetid: da2adf16-a9b5-4678-896e-2be8f5ca27e4
keywords:
- Broadcast windows Media Format
topic_type:
- apiref
api_name:
- Broadcast
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Broadcast

The **Broadcast** attribute is a file-level attribute indicating whether the content can be broadcast. It is assumed that any content for which no copyright has been assigned can be legally broadcast.

## Global Constant

g\_wszWMBroadcast

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




