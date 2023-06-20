---
title: DRM_LicenseID
description: The DRM\_LicenseID property contains a string retrieved from the license associated with the currently open file that uniquely identifies that license.
ms.assetid: d5967f5b-99b6-41ea-8494-ac4a7331bbfe
keywords:
- DRM_LicenseID windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_LicenseID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LicenseID** property contains a string retrieved from the license associated with the currently open file that uniquely identifies that license.

## Global Constant

g\_wszWMDRM\_LicenseID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

The license ID is stored in a license, not in an ASF file. Each individual license has a unique ID which is assigned by the license generator at the time the license is created. For example, if you obtain two licenses for the same content, each one will have a different LicenseID attribute. Typically, applications have no need to retrieve this value.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




