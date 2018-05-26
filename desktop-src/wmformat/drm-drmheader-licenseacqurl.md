---
title: DRM\_DRMHeader\_LicenseAcqURL
description: The DRM\_DRMHeader\_LicenseAcqURL attribute contains the license acquisition URL for a DRM version 7 license.
ms.assetid: 00c788b4-b291-4df5-9926-0badc7357faf
keywords:
- DRM_DRMHeader_LicenseAcqURL windows Media Format
topic_type:
- apiref
api_name:
- DRM_DRMHeader_LicenseAcqURL
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_DRMHeader\_LicenseAcqURL

The **DRM\_DRMHeader\_LicenseAcqURL** attribute contains the license acquisition URL for a DRM version 7 license.

## Global Constant

g\_wszWMDRM\_DRMHeader\_LicenseAcqURL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be retrieved with [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master). To set the license acquisition URL on the file using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master) you must use the [**DRM\_LicenseAcqURL**](drm-licenseacqurl.md) property.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




