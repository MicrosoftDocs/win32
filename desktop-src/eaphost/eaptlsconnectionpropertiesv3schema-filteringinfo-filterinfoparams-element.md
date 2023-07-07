---
title: FilteringInfo element
description: Learn about the FilteringInfo element. This element provides filtering information for the current type. | FilteringInfo element
ms.assetid: 59c7b042-8f79-4c16-bb21-a7faca5a9a31
keywords:
- FilteringInfo element EAPHost
topic_type:
- apiref
api_name:
- FilteringInfo
api_type:
- Schema
ms.topic: reference
ms.date: 07/07/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# PerformServerValidation element

The **FilteringInfo (FilterInfoParams)** element provides filtering information for the current type.

``` xml
<xs:element name="FilteringInfo"
    type="FilterInfoParams"
 />
```

The **FilteringInfo** element is defined by the [FilterInfoParams](eaptlsconnectionpropertiesv3schema-filterinfoparams-complextype.md) complex type.

## Remarks

The **FilteringInfo** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [FilteringInfoParams](eaptlsconnectionpropertiesv3schema-filterinfoparams-complextype.md)

### Possible immediate parent element in schema instance

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Schema Elements](eaptlsconnectionpropertiesv3schema-elements.md)
- [PerformServerValidation (EapType)](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md)
