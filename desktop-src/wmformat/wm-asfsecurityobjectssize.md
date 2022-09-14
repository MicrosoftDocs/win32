---
title: WM/ASFSecurityObjectsSize
description: The WM/ASFSecurityObjectsSize attribute contains the size, in bytes, of the DRM-related objects in the header of the ASF file.
ms.assetid: 40ea619a-1042-4d1b-a855-d80c93202765
keywords:
- WM/ASFSecurityObjectsSize windows Media Format
topic_type:
- apiref
api_name:
- WM/ASFSecurityObjectsSize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ASFSecurityObjectsSize

The **WM/ASFSecurityObjectsSize** attribute contains the size, in bytes, of the DRM-related objects in the header of the ASF file.

## Global Constant

g\_wszWMASFSecurityObjectsSize

## Data Type

**WMT\_TYPE\_QWORD**

## Remarks

This attribute is read-only, and applies to the entire file (stream 0).

You can only retrieve this attribute by using the methods of the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface from the metadata editor object.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




