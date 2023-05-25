---
title: WM/ASFPacketCount
description: The WM/ASFPacketCount attribute contains a count of the packets in the data section of the ASF file.
ms.assetid: 97035a4e-4de9-4c9e-9288-addf6eccddc7
keywords:
- WM/ASFPacketCount windows Media Format
topic_type:
- apiref
api_name:
- WM/ASFPacketCount
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/ASFPacketCount

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/ASFPacketCount** attribute contains a count of the packets in the data section of the ASF file.

## Global Constant

g\_wszWMASFPacketCount

## Data Type

**WMT\_TYPE\_QWORD**

## Remarks

This attribute is read-only, and applies to the entire file (stream 0).

You can only retrieve this attribute by using the methods of the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface from the metadata editor object.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




