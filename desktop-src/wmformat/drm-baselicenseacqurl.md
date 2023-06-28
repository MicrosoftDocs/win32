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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_BaseLicenseAcqURL

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




