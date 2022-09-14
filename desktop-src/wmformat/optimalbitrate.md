---
title: OptimalBitrate
description: The OptimalBitrate attribute contains the bit rate at which the file is best played.
ms.assetid: cd13b9b5-34d2-4ebb-9f10-3bf42dd9de81
keywords:
- OptimalBitrate windows Media Format
topic_type:
- apiref
api_name:
- OptimalBitrate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# OptimalBitrate

The **OptimalBitrate** attribute contains the bit rate at which the file is best played.

## Global Constant

g\_wszWMOptimalBitrate

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

This is a coded attribute.

For files that contain variable bit rate (VBR) streams, this value is the peak bit rate for the streams in the file. For files without VBR, this value is the same as [**Bitrate**](bit-rate.md).

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




