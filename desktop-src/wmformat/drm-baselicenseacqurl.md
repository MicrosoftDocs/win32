---
title: DRM_BaseLicenseAcqURL
description: The DRM\_BaseLicenseAcqURL attribute contains a partial, base URL to which a player application must navigate to obtain a license for the content.
ms.assetid: 9acaac44-81b2-467c-9510-023fbb47dd04
keywords:
- DRM_BaseLicenseAcqURL windows Media Format
topic_type:
- apiref
api_name:
- DRM_BaseLicenseAcqURL
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_BaseLicenseAcqURL

The **DRM\_BaseLicenseAcqURL** attribute contains a partial, base URL to which a player application must navigate to obtain a license for the content.

## Global Constant

g\_wszWMDRM\_BaseLicenseAcqURL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is an optional read-write property that is set and retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty). It is provided to enable license distribution systems to use relative paths in the license acquisition URL properties.

After setting this property, all partial license acquisition URLs in content headers will have the base URL added to the front of the partial URL to form a full URL for the player application to navigate to. Calling **IWMDRMReader::GetDRMProperty** for **DRM\_BaseLicenseAcqURL** will only work only in the same session as it was set. The property is not stored in the content header; it is dynamic, and only the relative URL is stored in the content.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




