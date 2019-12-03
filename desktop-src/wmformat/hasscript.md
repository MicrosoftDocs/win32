---
title: HasScript
description: The HasScript attribute is a file-level attribute specifying whether the file contains any script streams.
ms.assetid: e94c37ea-e11c-4abd-91d1-8f82612d8cba
keywords:
- HasScript windows Media Format
topic_type:
- apiref
api_name:
- HasScript
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HasScript

The **HasScript** attribute is a file-level attribute specifying whether the file contains any script streams.

## Global Constant

g\_wszWMHasScript

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




