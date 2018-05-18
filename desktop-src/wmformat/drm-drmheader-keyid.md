---
title: DRM\_DRMHeader\_KeyID
description: The DRM\_DRMHeader\_KeyID attribute contains the key ID for the file.
ms.assetid: 'cf9fe829-8473-4dd5-9a99-48b709fec0d8'
keywords: ["DRM_DRMHeader_KeyID windows Media Format"]
topic_type:
- apiref
api_name:
- DRM_DRMHeader_KeyID
api_type:
- NA
---

# DRM\_DRMHeader\_KeyID

The **DRM\_DRMHeader\_KeyID** attribute contains the key ID for the file.

## Global Constant

g\_wszWMDRM\_DRMHeader\_KeyID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be retrieved with [**IWMDRMReader::GetDRMProperty**](iwmdrmreader-getdrmproperty.md). To set the key ID on the file using [**IWMDRMWriter::SetDRMAttribute**](iwmdrmwriter-setdrmattribute.md) you must use the [**DRM\_KeyID**](drm-keyid.md) property.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




