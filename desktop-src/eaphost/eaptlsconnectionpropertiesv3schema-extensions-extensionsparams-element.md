---
title: Extensions element
description: Learn about the Extensions element. This element provides extension parameters for the current type. | Extensions element
ms.assetid: 867ec85f-014d-4820-a17a-f864fe28c24e
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

The **Extensions (ExtensionsParams)** element provides extension parameters for the current type.

``` xml
<xs:element name="Extensions"
    type="ExtensionsParams"
 />
```

The **Extensions** element is defined by the [ExtensionsParams](eaptlsconnectionpropertiesv3schema-extensionparams-complextype.md) complex type.

## Remarks

The **Extensions** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [ExtensionsParams](eaptlsconnectionpropertiesv3schema-extensionparams-complextype.md)

### Possible immediate parent element in schema instance

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Schema Elements](eaptlsconnectionpropertiesv3schema-elements.md)
- [PerformServerValidation (EapType)](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md)
