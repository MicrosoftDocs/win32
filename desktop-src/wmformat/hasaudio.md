---
title: HasAudio
description: The HasAudio attribute is a file-level attribute that specifies whether the file contains any audio streams.
ms.assetid: 104c9634-611b-4cd9-8493-cfdaddd49b72
keywords:
- HasAudio windows Media Format
topic_type:
- apiref
api_name:
- HasAudio
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HasAudio

The **HasAudio** attribute is a file-level attribute that specifies whether the file contains any audio streams.

## Global Constant

g\_wszWMHasAudio

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




