---
title: ProviderName (EapAkaPrime) element
description: Learn about the ProviderName (EapAkaPrime) element. This element indicates the provider name that will be used while determining the list to be allowed for authentication. | ProviderName (EapAkaPrime) element
ms.assetid: 91f5b1aa-854f-459e-83c5-5a53dea8448b
keywords:
- ProviderName (EapAkaPrime) element EAPHost
topic_type:
- apiref
api_name:
- ProviderName
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# ProviderName (EapAkaPrime) element

The **ProviderName (EapAkaPrime)** element is an optional string element indicating the provider name that will be used while determining the list to be allowed for authentication. Only the items matching the specified provider name will be allowed for authentication.

``` xml
<xs:element name="ProviderName"
    type="xs:string" minOccurs="0" maxOccurs="1"/>
```

The **ProviderName (EapAkaPrime)** element is defined as part of a sequence in a complex type within the **EapAkaPrime** element.

## Remarks

The **ProviderName (EapAkaPrime)** element is optional.

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
