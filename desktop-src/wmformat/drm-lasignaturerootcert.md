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
ms.date: 05/31/2018
---

# DRM\_LASignatureRootCert

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

 

 




