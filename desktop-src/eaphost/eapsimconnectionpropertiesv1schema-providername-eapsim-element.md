---
title: ProviderName (EapSim) element
description: Learn about the ProviderName (EapSim) element. This element indicates the provider name that will be used while determining the list of SIMs to be allowed for authentication. | ProviderName (EapSim) element
ms.assetid: fc20cfaa-b177-4558-bdef-0f711d91291b
keywords:
- ProviderName (EapSim) element EAPHost
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

# ProviderName (EapSim) element

The **ProviderName (EapSim)** element is an optional string element indicating the provider name that will be used while determining the list of SIMs to be allowed for authentication. Only the SIMs matching the specified provider name will be allowed for authentication.

``` xml
<xs:element name="ProviderName"
    type="xs:string" minOccurs="0" maxOccurs="1"/>
```

The **ProviderName (EapSim)** element is defined as part of a sequence in a complex type within the **EapSim** element.

## Remarks

The **ProviderName (EapSim)** element is optional.

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
