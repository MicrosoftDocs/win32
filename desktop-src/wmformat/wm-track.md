---
title: WM/Track
description: The WM/Track attribute contains the track number of the content. This attribute is zero-based and is supported for backward compatibility. New content should use the WM/TrackNumber attribute instead.
ms.assetid: c763d7b0-9d12-4a4e-8c9f-9cf67bd2a02b
keywords:
- WM/Track windows Media Format
topic_type:
- apiref
api_name:
- WM/Track
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/Track

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/Track** attribute contains the track number of the content. This attribute is zero-based and is supported for backward compatibility. New content should use the [**WM/TrackNumber**](wm-tracknumber.md) attribute instead.

## Global Constant

g\_wszWMTrack

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

Many existing applications write the value for **WM/Track** as a **DWORD**. If you create an application that plays files from unknown sources, you should include code to handle both string and **DWORD** values.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




