---
title: DRM_DRMHeader_ContentDistributor
description: The DRM\_DRMHeader\_ContentDistributor attribute contains a string identifiying the content distributor.
ms.assetid: ea9ae7ba-35cc-4e86-995c-9abcdae48f9c
keywords:
- DRM_DRMHeader_ContentDistributor windows Media Format
topic_type:
- apiref
api_name:
- DRM_DRMHeader_ContentDistributor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_DRMHeader\_ContentDistributor

The **DRM\_DRMHeader\_ContentDistributor** attribute contains a string identifiying the content distributor.

## Global Constant

g\_wszWMDRM\_DRMHeader\_ContentDistributor

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

The content ID is optional and is determined solely by the content creator. The writer object does nothing with this attribute. This attribute is present with DRM Version 7 content only. It can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




