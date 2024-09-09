---
title: WM/TrackNumber
description: The WM/TrackNumber attribute contains the track number of the content. This attribute is 1-based.
ms.assetid: cd338cd9-a5de-4311-8089-1d5d90570f69
keywords:
- WM/TrackNumber windows Media Format
topic_type:
- apiref
api_name:
- WM/TrackNumber
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/TrackNumber

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/TrackNumber** attribute contains the track number of the content. This attribute is 1-based.

## Global Constant

g\_wszWMTrackNumber

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

Many existing applications write the value for **WM/TrackNumber** as a **DWORD**. If you create an application that plays files from unknown sources, you should include code to handle both string and **DWORD** values.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




