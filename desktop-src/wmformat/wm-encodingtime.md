---
title: WM/EncodingTime
description: The WM/EncodingTime attribute contains a time stamp of the time at which the content was encoded.
ms.assetid: 63da9392-264d-40bb-99fd-56db93801941
keywords:
- WM/EncodingTime windows Media Format
topic_type:
- apiref
api_name:
- WM/EncodingTime
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/EncodingTime

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/EncodingTime** attribute contains a time stamp of the time at which the content was encoded.

## Global Constant

g\_wszWMEncodingTime

## Data Type

**FILETIME** (**WMT\_TYPE\_QWORD**)

## Remarks

This attribute uses a FILETIME value, which is a 64-bit value representing the number of 100-nanosecond time units elapsed since January 1, 1601. For more information about the FILETIME, see the Windows System Information section of the Platform SDK.

This is not a coded attribute. You must set it manually if you want to include it in your files.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




