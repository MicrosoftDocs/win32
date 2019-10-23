---
title: VBRPeak
description: The VBRPeak attribute contains the highest momentary bit rate in a variable bit rate (VBR) encoded stream.
ms.assetid: 7b735145-8235-4efb-986f-952989b739bc
keywords:
- VBRPeak windows Media Format
topic_type:
- apiref
api_name:
- VBRPeak
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VBRPeak

The **VBRPeak** attribute contains the highest momentary bit rate in a variable bit rate (VBR) encoded stream.

## Global Constant

g\_wszVBRPeak

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

When accessing the **IWMHeaderInfo3** interface of the writer object, you can add or change this value. In other objects (metadata editor, reader, and synchronous reader), this value is read-only.

The writer automatically writes a **VBRPeak** value for each VBR stream.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




