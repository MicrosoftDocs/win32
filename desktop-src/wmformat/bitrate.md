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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Bitrate

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




