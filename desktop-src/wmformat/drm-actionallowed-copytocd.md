---
title: DRM\_ActionAllowed\_CopyToCD
description: The DRM\_ActionAllowed\_CopyToCD attribute indicates whether the content is allowed to be copied to a CD.
ms.assetid: 'c650bb2e-6cec-404a-8ece-7a5687cda99f'
keywords: ["DRM_ActionAllowed_CopyToCD windows Media Format"]
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_CopyToCD
api_type:
- NA
---

# DRM\_ActionAllowed\_CopyToCD

The **DRM\_ActionAllowed\_CopyToCD** attribute indicates whether the content is allowed to be copied to a CD.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_CopyToCD

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

Windows Media DRM 10 licenses use the Copy action to restrict copying to CD. You should check the [**DRM\_ActionAllowed\_Copy**](drm-actionallowed-copy.md) property to determine whether copying is allowed.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](iwmdrmreader-getdrmproperty.md).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




