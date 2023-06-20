---
title: DRM_LASignatureRootCert
description: The DRM\_LASignatureRootCert attribute contains the root certificate in the certification chain that is used to authenticate the certificate contained in DRM\_LASignatureLicSrvCert.
ms.assetid: b1e44a80-5fff-4a6a-bacd-6384546673c6
keywords:
- DRM_LASignatureRootCert windows Media Format
topic_type:
- apiref
api_name:
- DRM_LASignatureRootCert
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_LASignatureRootCert

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LASignatureRootCert** attribute contains the root certificate in the certification chain that is used to authenticate the certificate contained in [**DRM\_LASignatureLicSrvCert**](drm-lasignaturelicsrvcert.md).

## Global Constant

g\_wszWMDRM\_LASignatureRootCert

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This property can be set with the [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) method. It is not accessible to the reader object.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




