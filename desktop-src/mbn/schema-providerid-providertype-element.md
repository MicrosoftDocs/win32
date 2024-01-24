---
description: Specifies the provider ID of the cellular network.
ms.assetid: 5528dfec-eb1b-4af3-8d7d-03b458e5ae75
title: ProviderID (providerType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ProviderID
api_type: 
- Schema
---

# ProviderID (providerType) Element

The **ProviderID (providerType)** element specifies the provider ID of the cellular network.

The element is a sequence of digits with a maximum of 6 digits.

This element is required within the [**Provider**](schema-provider-dataroamingpartners-element.md) element.

``` syntax
<xs:element name="ProviderID"
    type="providerType"
 />
```

The **ProviderID** element is defined by the [**providerType**](schema-providertype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**providerType**](schema-providertype-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Provider (DataRoamingPartners)**](schema-provider-dataroamingpartners-element.md)
</dt> </dl>

 

 




