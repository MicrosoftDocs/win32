---
title: UseStrongCipherKeys (EapSim) element
description: Learn about the UseStrongCipherKeys (EapSim) element. This element indicates whether the client accepts only three random numbers. | UseStrongCipherKeys (EapSim) element
ms.assetid: 18f72590-51d9-41cc-8f78-631d8414a374
keywords:
- UseStrongCipherKeys (EapSim) element EAPHost
topic_type:
- apiref
api_name:
- UseStrongCipherKeys
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# UseStrongCipherKeys (EapSim) element

The **UseStrongCipherKeys (EapSim)** element is an optional Boolean flag indicating whether the client accepts only three random numbers. If set to `TRUE`, the client accepts only three RANDs from the server. If set to `FALSE` or absent, the client accepts either two or three RANDs from the server.

``` xml
<xs:element name="UseStrongCipherKeys"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **UseStrongCipherKeys (EapSim)** element is defined as part of a sequence in a complex type within the **EapSim** element.

## Remarks

The **UseStrongCipherKeys (EapSim)** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapSim](eapsimconnectionpropertiesv1schema-eapsim-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Schema Elements](eapteapconnectionpropertiesv1schema-elements.md)
