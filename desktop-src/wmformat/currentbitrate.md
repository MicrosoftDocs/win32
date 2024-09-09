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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentBitrate

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




