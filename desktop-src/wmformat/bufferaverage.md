---
title: BufferAverage
description: The BufferAverage attribute contains the average buffer size needed for a variable bit rate (VBR) stream.
ms.assetid: 5fd69534-6655-4c98-bf07-a694585fc9ae
keywords:
- BufferAverage windows Media Format
topic_type:
- apiref
api_name:
- BufferAverage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BufferAverage

The **BufferAverage** attribute contains the average buffer size needed for a variable bit rate (VBR) stream.

## Global Constant

g\_wszBufferAverage

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

When accessing the **IWMHeaderInfo3** interface of the writer object, you can add or change this value. In other objects (metadata editor, reader, and synchronous reader), this value is read-only.

The writer automatically writes a **BufferAverage** value for each VBR stream.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




