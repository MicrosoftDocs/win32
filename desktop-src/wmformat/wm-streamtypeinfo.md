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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM/StreamTypeInfo

The **WM/StreamTypeInfo** attribute contains the configuration information for the specified stream in the ASF file.

## Global Constant

g\_wszWMStreamTypeInfo

## Data Type

[**WM\_STREAM\_TYPE\_INFO**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmstreamtypeinfo?branch=master) (**WMT\_TYPE\_BINARY**)

## Remarks

This attribute applies to specific streams. You cannot retrieve this attribute for stream 0.

This attribute is read-only.

**WM/StreamTypeInfo** can be accessed by the metadata editor object. This is the only way to access stream configuration information without opening the file with the reader object (or the synchronous reader object).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




