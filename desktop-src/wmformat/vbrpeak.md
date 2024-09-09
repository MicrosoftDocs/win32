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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VBRPeak

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




