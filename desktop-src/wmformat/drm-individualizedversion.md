---
title: DRM\_IndividualizedVersion
description: The DRM\_IndividualizedVersion attribute is stored in the DRM header and contains the minimum individualized version required to access the content.
ms.assetid: ed3e165c-c6b0-4eea-be79-a715abd4dd0a
keywords:
- DRM_IndividualizedVersion windows Media Format
topic_type:
- apiref
api_name:
- DRM_IndividualizedVersion
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_IndividualizedVersion

The **DRM\_IndividualizedVersion** attribute is stored in the DRM header and contains the minimum individualized version required to access the content.

## Global Constant

g\_wszWMDRM\_IndividualizedVersion

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be set using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master). The same file attribute can be retrieved using [**DRM\_DRMHeader\_IndividualizedVersion**](drm-drmheader-individualizedversion.md).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




