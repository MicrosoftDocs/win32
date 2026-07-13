---
title: DontRevealPermanentID (EapAka) element
description: Learn about the DontRevealPermanentID (EapAka) element. This element indicates whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. | DontRevealPermanentID (EapAka) element
ms.assetid: da0d3d69-c2e5-47a6-aa6f-56d65e9eaee7
keywords:
- DontRevealPermanentID (EapAka) element EAPHost
topic_type:
- apiref
api_name:
- DontRevealPermanentID
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# DontRevealPermanentID (EapAka) element

The **DontRevealPermanentID (EapAka)** element is an optional Boolean flag indicating whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. If set to `TRUE` or absent, the client does not send permanent identity when pseudonym identity is available, even if the server requests it. If set to `FALSE`, the client sends permanent identity when the server requests it.

``` xml
<xs:element name="DontRevealPermanentID"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **DontRevealPermanentID (EapAka)** element is defined as part of a sequence in a complex type within the **EapAka** element.

## Remarks

The **DontRevealPermanentID (EapAka)** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapAka](eapakaconnectionpropertiesv1schema-eapaka-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapakaconnectionpropertiesv1](eapakaconnectionpropertiesv1schema-schema.md)
- [eapakaconnectionpropertiesv1 Schema Elements](eapakaconnectionpropertiesv1schema-elements.md)
