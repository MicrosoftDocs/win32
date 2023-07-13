---
title: DontRevealPermanentID (EapAkaPrime) element
description: Learn about the DontRevealPermanentID (EapAkaPrime) element. This element indicates whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. | DontRevealPermanentID (EapAkaPrime) element
ms.assetid: 28f56014-d05f-4863-93b3-cd30f883ed51
keywords:
- DontRevealPermanentID (EapAkaPrime) element EAPHost
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

# DontRevealPermanentID (EapAkaPrime) element

The **DontRevealPermanentID (EapAkaPrime)** element is an optional Boolean flag indicating whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. If set to `TRUE` or absent, the client does not send permanent identity when pseudonym identity is available, even if the server requests it. If set to `FALSE`, the client sends permanent identity when the server requests it.

``` xml
<xs:element name="DontRevealPermanentID"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **DontRevealPermanentID (EapAkaPrime)** element is defined as part of a sequence in a complex type within the **EapAkaPrime** element.

## Remarks

The **DontRevealPermanentID (EapAkaPrime)** element is optional.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapAkaPrime](eapakaprimeconnectionpropertiesv1schema-eapakaprime-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapakaprimeconnectionpropertiesv1](eapakaprimeconnectionpropertiesv1schema-schema.md)
- [eapakaprimeconnectionpropertiesv1 Schema Elements](eapakaprimeconnectionpropertiesv1schema-elements.md)
