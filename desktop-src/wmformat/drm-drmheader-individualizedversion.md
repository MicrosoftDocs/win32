---
title: DRM\_DRMHeader\_IndividualizedVersion
description: The DRM\_DRMHeaderIndividualizedVersion attribute contains the minimum individualized version required to play back the file.
ms.assetid: '2ac24660-8b7a-4dba-9f9f-ad8b13a22f5c'
keywords: ["DRM_DRMHeader_IndividualizedVersion windows Media Format"]
topic_type:
- apiref
api_name:
- DRM_DRMHeader_IndividualizedVersion
api_type:
- NA
---

# DRM\_DRMHeader\_IndividualizedVersion

The **DRM\_DRMHeaderIndividualizedVersion** attribute contains the minimum individualized version required to play back the file.

## Global Constant

g\_wszWMDRM\_DRMHeader\_IndividualizedVersion

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. It can be retrieved with [**IWMDRMReader::GetDRMProperty**](iwmdrmreader-getdrmproperty.md). To set the individualized version (also called the security version) on the file using [**IWMDRMWriter::SetDRMAttribute**](iwmdrmwriter-setdrmattribute.md) you must use the [**DRM\_IndividualizedVersion**](drm-individualizedversion.md) property.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




