---
title: DRM_LicenseState_CopyToNonSDMIDevice
description: The DRM\_LicenseState\_CopyToNonSDMIDevice property contains a WM\_LICENSE\_STATE\_DATA structure that contains details about how this right has been applied to the content.
ms.assetid: aa0099b0-c6f8-4e27-a1f4-b98155d277aa
keywords:
- DRM_LicenseState_CopyToNonSDMIDevice windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseState_CopyToNonSDMIDevice
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_LicenseState\_CopyToNonSDMIDevice

The **DRM\_LicenseState\_CopyToNonSDMIDevice** property contains a [**WM\_LICENSE\_STATE\_DATA**](/previous-versions/windows/desktop/legacy/dd757942(v=vs.85)) structure that contains details about how this right has been applied to the content.

## Global Constant

g\_wszWMDRM\_LicenseState\_CopyToNonSDMIDevice

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 