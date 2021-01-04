---
title: WM/WMShadowFileSourceDRMType (Windows Media Format 11 SDK)
description: The WM/WMShadowFileSourceDRMType attribute contains the type of rights management that is used to protect the original file that the ASF file is derived from.
ms.assetid: 58e7a383-6e80-42fc-bc75-5920dbe67a40
keywords:
- WM/WMShadowFileSourceDRMType windows Media Format
topic_type:
- apiref
api_name:
- WM/WMShadowFileSourceDRMType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMShadowFileSourceDRMType (Windows Media Format 11 SDK)

The **WM/WMShadowFileSourceDRMType** attribute contains the type of rights management that is used to protect the original file that the ASF file is derived from.

## Global Constant

g\_wszWMWMShadowFileSourceDRMType

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

Content that exists in a file format other than ASF and is protected with some sort of rights management can be converted to a Windows Media file protected by Windows Media DRM through a process called license importing. Such an ASF file should contain this attribute as well as WM/WMShadowFileSourceFileType to track where the content came from.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




