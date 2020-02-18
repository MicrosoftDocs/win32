---
title: DRM_IsDRMCached
description: The DRM\_IsDRMCached property indicates whether DRM version 1 license information has been stored on the local machine.
ms.assetid: 868e3ada-d608-41d6-93d7-0b7930cbf2f9
keywords:
- DRM_IsDRMCached windows Media Format
topic_type:
- apiref
api_name:
- DRM_IsDRMCached
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_IsDRMCached

The **DRM\_IsDRMCached** property indicates whether DRM version 1 license information has been stored on the local machine.

## Global Constant

g\_wszWMDRM\_IsDRMCached

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty). It is **TRUE** when the license acquisition URL matches one of two know URLs used for local license acquisition in DRM version 1.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




