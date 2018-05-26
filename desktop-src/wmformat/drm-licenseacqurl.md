---
title: DRM\_LicenseAcqURL
description: The DRM\_LicenseAcqURL attribute contains the address of a Web page that the client application can navigate to in order to obtain a content license for DRM version 7 content.
ms.assetid: bee29e39-ded8-439d-9164-fc318cb535c0
keywords:
- DRM_LicenseAcqURL windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseAcqURL
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_LicenseAcqURL

The **DRM\_LicenseAcqURL** attribute contains the address of a Web page that the client application can navigate to in order to obtain a content license for DRM version 7 content.

## Global Constant

g\_wszWMDRM\_LicenseAcqURL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute can be set using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master). The same file attribute can be retrieved using [**DRM\_DRMHeader\_LicenseAcqURL**](drm-drmheader-licenseacqurl.md).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




