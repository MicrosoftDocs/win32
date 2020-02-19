---
title: DRM_DRMHeader_SubscriptionContentID
description: The DRM\_DRMHeader\_SubscriptionContentID attribute contains the subscription content ID.
ms.assetid: e582d841-4865-40d3-889e-847d3aac0a7c
keywords:
- DRM_DRMHeader_SubscriptionContentID windows Media Format
topic_type:
- apiref
api_name:
- DRM_DRMHeader_SubscriptionContentID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_DRMHeader\_SubscriptionContentID

The **DRM\_DRMHeader\_SubscriptionContentID** attribute contains the subscription content ID.

## Global Constant

g\_wszWMDRM\_DRMHeader\_SubscriptionContentID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is present with DRM Version 7 content only. The subscription content ID is optional and is determined solely by the content creator. The writer object does nothing with this attribute. It can be set using [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and it can be retrieved with [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




