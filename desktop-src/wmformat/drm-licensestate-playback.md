---
title: DRM\_LicenseState\_Playback
description: The DRM\_LicenseState\_Playback property contains a WM\_LICENSE\_STATE\_DATA structure that contains details about how this right has been applied to the content.
ms.assetid: deb559e6-1854-4ac7-bc77-c641e9579fde
keywords:
- DRM_LicenseState_Playback windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseState_Playback
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_LicenseState\_Playback

The **DRM\_LicenseState\_Playback** property contains a [**WM\_LICENSE\_STATE\_DATA**](/windows/win32/Wmsdkidl/?branch=master) structure that contains details about how this right has been applied to the content.

## Global Constant

g\_wszWMDRM\_LicenseState\_Playback

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




