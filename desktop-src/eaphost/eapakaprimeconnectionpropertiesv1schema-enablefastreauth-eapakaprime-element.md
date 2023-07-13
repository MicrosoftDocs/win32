---
title: EnableFastReauth (EapAkaPrime) element
description: Learn about the EnableFastReauth (EapAkaPrime) element. This element indicates whether the client can perform fast re-authentication when possible. | EnableFastReauth (EapAkaPrime) element
ms.assetid: 182b1de4-062a-46be-80c1-7927fd3be3ce
keywords:
- EnableFastReauth (EapAkaPrime) element EAPHost
topic_type:
- apiref
api_name:
- EnableFastReauth
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EnableFastReauth (EapAkaPrime) element

The **EnableFastReauth (EapAkaPrime)** element is an optional Boolean flag indicating whether the client can perform fast re-authentication when possible. If set to `TRUE`, the fast re-authentication is performed. If set to `FALSE` or absent, full authentication is performed.

``` xml
<xs:element name="EnableFastReauth"
    type="xs:boolean" minOccurs="0" maxOccurs="1"/>
```

The **EnableFastReauth (EapAkaPrime)** element is defined as part of a sequence in a complex type within the **EapAkaPrime** element.

## Remarks

The **EnableFastReauth (EapAkaPrime)** element is optional.

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
