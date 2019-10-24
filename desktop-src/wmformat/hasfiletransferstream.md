---
title: HasFileTransferStream
description: The HasFileTransferStream attribute is a file-level attribute specifying whether the file contains any file transfer streams.
ms.assetid: 5a671fb7-cd79-4ea8-8aed-63402dc008d3
keywords:
- HasFileTransferStream windows Media Format
topic_type:
- apiref
api_name:
- HasFileTransferStream
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HasFileTransferStream

The **HasFileTransferStream** attribute is a file-level attribute specifying whether the file contains any file transfer streams.

## Global Constant

g\_wszWMHasFileTransferStream

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




