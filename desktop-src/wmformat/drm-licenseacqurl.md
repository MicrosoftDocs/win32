---
title: DRM_LicenseAcqURL
description: The DRM\_LicenseAcqURL attribute contains the address of a Web page that the client application can navigate to in order to obtain a content license for DRM version 7 content.
ms.assetid: bee29e39-ded8-439d-9164-fc318cb535c0
keywords:
- DRM_LicenseAcqURL windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseAcqURL
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_LicenseAcqURL

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LicenseAcqURL** attribute contains the address of a Web page that the client application can navigate to in order to obtain a content license for DRM version 7 content.

## Global Constant

g\_wszWMDRM\_LicenseAcqURL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty). The same file attribute can be retrieved using [**DRM\_DRMHeader\_LicenseAcqURL**](drm-drmheader-licenseacqurl.md).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




