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
ms.date: 05/31/2018
---

# WM/ASFPacketCount

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

 

 




