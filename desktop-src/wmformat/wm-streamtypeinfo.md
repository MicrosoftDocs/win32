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
ms.date: 05/31/2018
---

# WM/StreamTypeInfo

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

 

 




