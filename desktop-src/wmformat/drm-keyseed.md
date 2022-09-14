---
title: DRM_KeySeed
description: The DRM\_KeySeed property contains the key seed that will be used in conjunction with the KeyID to create the key.
ms.assetid: 38613d50-89c2-4422-9265-5e89de030ae9
keywords:
- DRM_KeySeed windows Media Format
topic_type:
- apiref
api_name:
- DRM_KeySeed
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_KeySeed

The **DRM\_KeySeed** property contains the key seed that will be used in conjunction with the KeyID to create the key.

## Global Constant

g\_wszWMDRM\_KeySeed

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This property can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute). It is not accessible by the reader object.

A key seed is typically used to protect multiple files or sets of files, for example all the files issued by a license server, or perhaps all the files by a particular artist. The KeyID, however, is unique for each file.

The key seed must remain a secret that is shared only between the content creator and the license distributor. This value is not stored in the DRM header and it is neither needed by nor accessible to DRM player applications.

A new key seed can be generated using the [**IWMDRMWriter::GenerateKeySeed**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatekeyseed) method or by any other suitable means.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




