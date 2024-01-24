---
title: ProviderName (EapAka) element
description: Learn about the ProviderName (EapAka) element. This element indicates the provider name that will be used while determining the list to be allowed for authentication. | ProviderName (EapAka) element
ms.assetid: 60b50cdb-3f31-4e20-933c-a5e4718df2a3
keywords:
- ProviderName (EapAka) element EAPHost
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

# ProviderName (EapAka) element

The **ProviderName (EapAka)** element is an optional string element indicating the provider name that will be used while determining the list to be allowed for authentication. Only the items matching the specified provider name will be allowed for authentication.

``` xml
<xs:element name="ProviderName"
    type="xs:string" minOccurs="0" maxOccurs="1"/>
```

The **ProviderName (EapAka)** element is defined as part of a sequence in a complex type within the **EapAka** element.

## Remarks

The **ProviderName (EapAka)** element is optional.

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
