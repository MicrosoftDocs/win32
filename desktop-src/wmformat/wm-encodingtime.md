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
ms.date: 05/31/2018
---

# WM/EncodingTime

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

 

 




