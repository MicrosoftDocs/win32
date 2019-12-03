---
title: Bitrate
description: The Bitrate attribute is a file-level attribute containing the bit rate of the file in bits per second.
ms.assetid: 35da0735-db39-4463-8dad-451a77a171b6
keywords:
- Bitrate windows Media Format
topic_type:
- apiref
api_name:
- Bitrate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Bitrate

The **Bitrate** attribute is a file-level attribute containing the bit rate of the file in bits per second.

## Global Constant

g\_wszWMBitrate

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




