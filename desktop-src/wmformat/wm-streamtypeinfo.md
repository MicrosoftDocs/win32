---
title: WM/StreamTypeInfo
description: The WM/StreamTypeInfo attribute contains the configuration information for the specified stream in the ASF file.
ms.assetid: 4d7f18d4-d76d-4e2e-b8a9-eb96844a2fa1
keywords:
- WM/StreamTypeInfo windows Media Format
topic_type:
- apiref
api_name:
- WM/StreamTypeInfo
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/StreamTypeInfo

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/StreamTypeInfo** attribute contains the configuration information for the specified stream in the ASF file.

## Global Constant

g\_wszWMStreamTypeInfo

## Data Type

[**WM\_STREAM\_TYPE\_INFO**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_stream_type_info) (**WMT\_TYPE\_BINARY**)

## Remarks

This attribute applies to specific streams. You cannot retrieve this attribute for stream 0.

This attribute is read-only.

**WM/StreamTypeInfo** can be accessed by the metadata editor object. This is the only way to access stream configuration information without opening the file with the reader object (or the synchronous reader object).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




