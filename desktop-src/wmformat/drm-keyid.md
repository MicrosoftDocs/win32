---
title: DRM_KeyID
description: The DRM\_KeyID attribute contains the key identifier.
ms.assetid: 90406809-76d9-4559-afe8-6812efbc1477
keywords:
- DRM_KeyID windows Media Format
topic_type:
- apiref
api_name:
- DRM_KeyID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_KeyID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_KeyID** attribute contains the key identifier.

## Global Constant

g\_wszWMDRM\_KeyID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present for DRM Version 7 content only. It can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty). The same file attribute can be retrieved using [**DRM\_DRMHeader\_KeyID**](drm-drmheader-keyid.md).

The key ID is used in conjunction with the key seed to create the content key which is used to encrypt and decrypt the file. The writer application uses the key ID to encrypt the file and then it stores the key ID in the file header. When a player application requests a license for a file, the DRM component sends the key ID (along with the rest of the DRM header) to the license server. The license server, which has the secret key seed, uses it and the key ID to create a key for the file, which it then inserts into a license along with the various rights that will be applied to the file.

Typically, one key seed is used with many key IDs. The key seed is a secret shared only by the content creator and the license distributor. The key ID is used by DRM client applications and is stored in the DRM header in the clear.

This attribute is the same as [**DRM\_DRMHeader\_KeyID**](drm-drmheader-keyid.md).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




