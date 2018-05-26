---
title: DRM\_HeaderSignPrivKey
description: The DRM\_HeaderSignPrivKey property contains the private key used to sign the ASF header.
ms.assetid: 0f32e63d-d416-4a1d-b10c-2534b747adf3
keywords:
- DRM_HeaderSignPrivKey windows Media Format
topic_type:
- apiref
api_name:
- DRM_HeaderSignPrivKey
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRM\_HeaderSignPrivKey

The **DRM\_HeaderSignPrivKey** property contains the private key used to sign the ASF header.

## Global Constant

g\_wszWMDRM\_HeaderSignPrivKey

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This property is generated using the [**IWMDRMWriter::GenerateSigningKeyPair**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatesigningkeypair?branch=master). Keep this key secret and share the public key only with the license service. After you set this key, the DRM component will use it to sign the ASF file header (not the DRM header which is signed with the digital signature object values such as DRM\_LASignaturePrivKey). Obviously, **DRM\_HeaderSignPrivKey** is not included in the file headert.

This property is not accessible from the reader object. It can be set from the writer object using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




