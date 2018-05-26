---
title: DRM\_ActionAllowed\_Copy
description: The DRM\_ActionAllowed\_Copy attribute indicates whether the content is allowed to be copied to a device, such as a portable player.
ms.assetid: 3a391a14-ccbb-43c6-b362-0db53d93ab79
keywords:
- DRM_ActionAllowed_Copy windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_Copy
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_ActionAllowed\_Copy

The **DRM\_ActionAllowed\_Copy** attribute indicates whether the content is allowed to be copied to a device, such as a portable player.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_Copy

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

In Windows Media DRM 10, all copy operations are restricted using the Copy action.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




