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
ms.date: 05/31/2018
---

# WM/Track

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

 

 




