---
title: IgnoreNetworkNameMismatch (EapAkaPrime) element
description: Learn about the IgnoreNetworkNameMismatch (EapAkaPrime) element. This element indicates whether the client is to validate its network name against the network name received from the server. | IgnoreNetworkNameMismatch (EapAkaPrime) element
ms.assetid: c2fa4a57-3b20-42d1-b989-e68b713f9c53
keywords:
- IgnoreNetworkNameMismatch (EapAkaPrime) element EAPHost
topic_type:
- apiref
api_name:
- IgnoreNetworkNameMismatch
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# IgnoreNetworkNameMismatch (EapAkaPrime) element

The **IgnoreNetworkNameMismatch (EapAkaPrime)** element is an optional Boolean flag indicating whether the client is to validate its network name against the network name received from the server. If set to `TRUE` or absent, the network name is not validated. If set to `FALSE`, the network name validation is performed.

``` xml
<xs:element name="IgnoreNetworkNameMismatch"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **IgnoreNetworkNameMismatch (EapAkaPrime)** element is defined as part of a sequence in a complex type within the **EapAkaPrime** element.

## Remarks

The **IgnoreNetworkNameMismatch (EapAkaPrime)** element is optional.

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
