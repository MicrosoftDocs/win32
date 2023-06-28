---
title: WM/WMADRCPeakReference
description: The WM/WMADRCPeakReference attribute contains the maximum volume level of the file as encoded. This value is used by Windows Media Player for dynamic range control. This value is set by the codec and is read-only.
ms.assetid: c732ee88-437b-4970-8f17-61aed2d91022
keywords:
- WM/WMADRCPeakReference windows Media Format
topic_type:
- apiref
api_name:
- WM/WMADRCPeakReference
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/WMADRCPeakReference

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/WMADRCPeakReference** attribute contains the maximum volume level of the file as encoded. This value is used by Windows Media Player for dynamic range control. This value is set by the codec and is read-only.

## Global Constant

g\_wszWMWMADRCPeakReference

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

[**WM/WMADRCPeakTarget**](wm-wmadrcpeaktarget.md)
</dt> </dl>

 

 




