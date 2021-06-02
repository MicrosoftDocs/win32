---
title: WM/WMShadowFileSourceFileType (Windows Media Format 11 SDK)
description: The WM/WMShadowFileSourceFileType contains the file type of the original file that the ASF file is derived from.
ms.assetid: e6543f07-b1dd-4a3d-9472-ebedf42e9599
keywords:
- WM/WMShadowFileSourceFileType windows Media Format
topic_type:
- apiref
api_name:
- WM/WMShadowFileSourceFileType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMShadowFileSourceFileType (Windows Media Format 11 SDK)

The **WM/WMShadowFileSourceFileType** contains the file type of the original file that the ASF file is derived from.

## Global Constant

g\_wszWMWMShadowFileSourceFileType

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

Content that exists in a file format other than ASF and is protected with some sort of rights management can be converted to a Windows Media file protected by Windows Media DRM through a process called license importing. Such an ASF file should contain this attribute as well as WM/WMShadowFileSourceDRMType to track where the content came from.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




