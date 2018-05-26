---
title: DRM\_LASignatureLicSrvCert
description: The DRM\_LASignatureLicSrvCert attribute contains the certificate that verifies the certificate contained in DRM\_LASignatureCert.
ms.assetid: 1c22c010-f344-4dcf-a3d1-f852a65bd772
keywords:
- DRM_LASignatureLicSrvCert windows Media Format
topic_type:
- apiref
api_name:
- DRM_LASignatureLicSrvCert
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_LASignatureLicSrvCert

The **DRM\_LASignatureLicSrvCert** attribute contains the certificate that verifies the certificate contained in [**DRM\_LASignatureCert**](drm-lasignaturecert.md).

## Global Constant

g\_wszWMDRM\_LASignatureLicSrvCert

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This property can be set with the [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master) method. It is not accessible to the reader object.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




