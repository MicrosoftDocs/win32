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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IsVBR

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




