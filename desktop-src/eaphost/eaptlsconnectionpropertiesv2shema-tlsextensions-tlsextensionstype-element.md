---
title: PerformServerValidation element
description: Learn about the PerformServerValidation element. This element indicates whether server validation is performed. | PerformServerValidation element
ms.assetid: c1dd1af1-63a0-48f7-8da5-860c50d73259
keywords:
- PerformServerValidation element EAPHost
topic_type:
- apiref
api_name:
- PerformServerValidation
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# PerformServerValidation element

The **PerformServerValidation (EapType)** element indicates whether server validation is performed.

``` syntax
<xs:element name="PerformServerValidation"
    type="xs:boolean"
 />
```

The **PerformServerValidation** element is defined by the [**EapType**](eaptlsconnectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

The **PerformServerValidation** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 7 \[desktop apps only\] |
| Server | Windows Server 2008 R2 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [**EapType**](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Possible immediate parent element in schema instance

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv2](eaptlsconnectionpropertiesv2schema-schema.md)
- [eaptlsconnectionpropertiesv2 Schema Elements](eaptlsconnectionpropertiesv2schema-elements.md)
- [PerformServerValidation (EapType)](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md)
