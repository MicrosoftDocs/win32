---
title: WM/WMADRCPeakTarget
description: The WM/WMADRCPeakTarget attribute contains the maximum volume level requested by the user. This value is used by Windows Media Player for dynamic range control.
ms.assetid: 94ef5db1-34f4-4cf8-ac56-c85cca10536b
keywords:
- WM/WMADRCPeakTarget windows Media Format
topic_type:
- apiref
api_name:
- WM/WMADRCPeakTarget
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMADRCPeakTarget

The **WM/WMADRCPeakTarget** attribute contains the maximum volume level requested by the user. This value is used by Windows Media Player for dynamic range control.

## Global Constant

g\_wszWMWMADRCPeakTarget

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

There are four attributes used by Windows Media Player for dynamic range control: **WM/WMADRCAverageReference**, **WM/WMADRCPeakReference**, **WM/WMADRCAverageTarget**, and **WM/WMADRCPeakTarget**. All of these values are set by the writer based on information from the codec when writing streams with the Windows Media Audio 9 codec or Windows Media Audio 9 Professional codec. The average values are set to the average volume level of the stream, and the peak values are set to the maximum volume level in the stream. The reference values are read-only. The target values are set by Windows Media Player when the file is being played to record the dynamic range control preferences of the user.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**WM/WMADRCAverageReference**](wm-wmadrcaveragereference.md)
</dt> <dt>

[**WM/WMADRCAverageTarget**](wm-wmadrcaveragetarget.md)
</dt> <dt>

[**WM/WMADRCPeakReference**](wm-wmadrcpeakreference.md)
</dt> </dl>

 

 




