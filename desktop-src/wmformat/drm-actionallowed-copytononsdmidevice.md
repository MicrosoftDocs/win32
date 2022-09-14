---
title: DRM_ActionAllowed_CopyToNonSDMIDevice
description: The DRM\_ActionAllowed\_CopyToNonSDMIDevice attribute indicates whether the content is allowed to be copied to a non-SDMI device.
ms.assetid: 517ceeb5-4979-4667-ba54-8b9b1c6069f2
keywords:
- DRM_ActionAllowed_CopyToNonSDMIDevice windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_CopyToNonSDMIDevice
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_ActionAllowed\_CopyToNonSDMIDevice

The **DRM\_ActionAllowed\_CopyToNonSDMIDevice** attribute indicates whether the content is allowed to be copied to a non-SDMI device

## Global Constant

g\_wszWMDRM\_ActionAllowed\_CopyToNonSDMIDevice

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

Windows Media DRM 10 licenses use the Copy action to restrict copying to devices. You should check the [**DRM\_ActionAllowed\_Copy**](drm-actionallowed-copy.md) property to determine whether copying is allowed.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




