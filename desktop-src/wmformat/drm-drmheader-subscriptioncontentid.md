---
title: DRM\_DRMHeader\_SubscriptionContentID
description: The DRM\_DRMHeader\_SubscriptionContentID attribute contains the subscription content ID.
ms.assetid: 'e582d841-4865-40d3-889e-847d3aac0a7c'
keywords: ["DRM_DRMHeader_SubscriptionContentID windows Media Format"]
topic_type:
- apiref
api_name:
- DRM_DRMHeader_SubscriptionContentID
api_type:
- NA
---

# DRM\_DRMHeader\_SubscriptionContentID

The **DRM\_DRMHeader\_SubscriptionContentID** attribute contains the subscription content ID.

## Global Constant

g\_wszWMDRM\_DRMHeader\_SubscriptionContentID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. The subscription content ID is optional and is determined solely by the content creator. The writer object does nothing with this attribute. It can be set using [**IWMDRMWriter::SetDRMAttribute**](iwmdrmwriter-setdrmattribute.md) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](iwmdrmreader-getdrmproperty.md).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




