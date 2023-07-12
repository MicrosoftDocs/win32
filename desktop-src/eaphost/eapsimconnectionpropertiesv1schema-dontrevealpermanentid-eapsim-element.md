---
title: DontRevealPermanentID (EapSim) element
description: Learn about the DontRevealPermanentID (EapSim) element. This element indicates whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. | DontRevealPermanentID (EapSim) element
ms.assetid: 5423bfff-4604-45bc-962a-aa73a680cb02
keywords:
- DontRevealPermanentID (EapSim) element EAPHost
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

# DontRevealPermanentID (EapSim) element

The **DontRevealPermanentID (EapSim)** element is an optional Boolean flag indicating whether the client is allowed to reveal permanent identity when pseudonym identity is available from previous authentications. If set to `TRUE` or absent, the client does not send permanent identity when pseudonym identity is available, even if the server requests it. If set to `FALSE`, the client sends permanent identity when the server requests it.

``` xml
<xs:element name="DontRevealPermanentID"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **DontRevealPermanentID (EapSim)** element is defined as part of a sequence in a complex type within the **EapSim** element.

## Remarks

The **DontRevealPermanentID (EapSim)** element is optional.

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
