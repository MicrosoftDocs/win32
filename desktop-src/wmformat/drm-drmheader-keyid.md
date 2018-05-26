---
title: DRM\_DRMHeader\_KeyID
description: The DRM\_DRMHeader\_KeyID attribute contains the key ID for the file.
ms.assetid: cf9fe829-8473-4dd5-9a99-48b709fec0d8
keywords:
- DRM_DRMHeader_KeyID windows Media Format
topic_type:
- apiref
api_name:
- DRM_DRMHeader_KeyID
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_DRMHeader\_KeyID

The **DRM\_DRMHeader\_KeyID** attribute contains the key ID for the file.

## Global Constant

g\_wszWMDRM\_DRMHeader\_KeyID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be retrieved with [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master). To set the key ID on the file using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master) you must use the [**DRM\_KeyID**](drm-keyid.md) property.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




