---
title: DRM\_ActionAllowed\_CopyToSDMIDevice
description: The DRM\_ActionAllowed\_CopyToSDMIDevice attribute indicates whether the content is allowed to be copied to an SDMI device.
ms.assetid: 3ffb9c8f-5640-4ab5-9939-f9525ab960c6
keywords:
- DRM_ActionAllowed_CopyToSDMIDevice windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_CopyToSDMIDevice
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_ActionAllowed\_CopyToSDMIDevice

The **DRM\_ActionAllowed\_CopyToSDMIDevice** attribute indicates whether the content is allowed to be copied to an SDMI device.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_CopyToSDMIDevice

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

Windows Media DRM 10 licenses use the Copy action to restrict copying to devices. You should check the [**DRM\_ActionAllowed\_Copy**](drm-actionallowed-copy.md) property to determine whether copying is allowed.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




