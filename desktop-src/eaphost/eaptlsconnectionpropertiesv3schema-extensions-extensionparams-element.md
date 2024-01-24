---
title: Extensions element
description: Learn about the Extensions element. This element is an optional container for elements of other namespaces that enables future enhancements to the schema. | Extensions element
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

# Extensions (ExtensionParams) element

**Extensions (ExtensionParams)** is a container for elements of other namespaces that enables future enhancements to the schema.

``` xml
<xs:element name="Extensions"
    type="ExtensionParams"
 />
```

The **Extensions** element is defined by the [ExtensionParams](eaptlsconnectionpropertiesv3schema-extensionparams-complextype.md) complex type.

## Remarks

The **Extensions** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [ExtensionParams](eaptlsconnectionpropertiesv3schema-extensionparams-complextype.md)

### Possible immediate parent element in schema instance

- [EapType](eaptlsconnectionpropertiesv1schema-eaptype-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Schema Elements](eaptlsconnectionpropertiesv3schema-elements.md)
- [PerformServerValidation (EapType)](eaptlsconnectionpropertiesv1schema-performservervalidation-peapextensionstype-element.md)
