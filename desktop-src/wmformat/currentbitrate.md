---
title: CurrentBitrate
description: The CurrentBitrate attribute contains the current total bit rate of the active streams in the file.
ms.assetid: 961f36d5-a408-40d9-9ca1-0ed7c484858f
keywords:
- CurrentBitrate windows Media Format
topic_type:
- apiref
api_name:
- CurrentBitrate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentBitrate

The CurrentBitrate attribute contains the current total bit rate of the active streams in the file.

## Global Constant

g\_wszWMCurrentBitrate

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

This is a coded attribute.

The value retrieved for **CurrentBitrate** is different depending upon the object used. In the reader or synchronous reader object, the value is the actual bit rate at the time of the call. In the metadata editor object, the value is the average bit rate of the file.

The actual bit rate of a file is equal to the bit rates of all active streams plus some overhead. This is the value that is, for example, displayed when playing a file with the Windows Media Player.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




