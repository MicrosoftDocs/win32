---
title: IsVBR
description: The IsVBR attribute specifies whether the content in a stream was encoded using variable bit rate (VBR) encoding.
ms.assetid: 13bd2400-c8f8-4074-8702-498543e42a63
keywords:
- IsVBR windows Media Format
topic_type:
- apiref
api_name:
- IsVBR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# IsVBR

The **IsVBR** attribute specifies whether the content in a stream was encoded using variable bit rate (VBR) encoding.

## Global Constant

g\_wszWMIsVBR

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

When accessing the **IWMHeaderInfo3** interface of the writer object, you can add or change this value. In other objects (metadata editor, reader, and synchronous reader), this value is read-only.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**Multicast Station Attributes**](multicast-station-attributes.md)
</dt> </dl>

 

 




