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
ms.date: 05/31/2018
---

# WM/TrackNumber

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

 

 




