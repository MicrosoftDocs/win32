---
title: DRM_V1LicenseAcqURL
description: The DRM\_V1LicenseAcqURL attribute contains the address of a Web site where a user can obtain a DRM version 1 license.
ms.assetid: 7bfc3a6a-6d22-447b-9dc2-fc3563f23f7d
keywords:
- DRM_V1LicenseAcqURL windows Media Format
topic_type:
- apiref
api_name:
- DRM_V1LicenseAcqURL
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_V1LicenseAcqURL

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_V1LicenseAcqURL** attribute contains the address of a Web site where a user can obtain a DRM version 1 license.

## Global Constant

g\_wszWMDRM\_V1LicenseAcqURL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




