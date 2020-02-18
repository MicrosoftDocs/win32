---
title: DRM_LASignaturePrivKey
description: The DRM\_LASignaturePrivKey property contains the private key that is used to encrypt the DRM header.
ms.assetid: b7083237-da11-4f31-a143-c0278a54b5a6
keywords:
- DRM_LASignaturePrivKey windows Media Format
topic_type:
- apiref
api_name:
- DRM_LASignaturePrivKey
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_LASignaturePrivKey

The **DRM\_LASignaturePrivKey** property contains the private key that is used to encrypt the DRM header.

## Global Constant

g\_wszWMDRM\_LASignaturePrivKey

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This property can be generated using the [**IWMDRMWriter::GenerateSigningKeyPair**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatesigningkeypair) method. This property should remain a secret known only by the content creator. This property can be set with the [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) method. It is not accessible to the reader object.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




