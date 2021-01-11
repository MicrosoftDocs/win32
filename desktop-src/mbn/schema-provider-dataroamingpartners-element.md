---
description: Identifies the name and provider ID for a cellular network.
ms.assetid: 007ecad9-23a3-4352-b3e2-c22d0f3f449d
title: Provider (DataRoamingPartners) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Provider
api_type: 
- Schema
---

# Provider (DataRoamingPartners) Element

The **Provider (DataRoamingPartners)** element identifies the name and provider ID for a cellular network.

This element has the following child elements.

-   [**ProviderID**](schema-providerid-providertype-element.md)
-   [**ProviderName**](schema-providername-providertype-element.md)

This element can be defined multiple times within the [**DataRoamingPartners**](schema-dataroamingpartners-mbnprofile-element.md) element. It must be defined at least once.

``` syntax
<xs:element name="Provider"
    type="providerType"
 />
```

The **Provider** element is defined by the [**DataRoamingPartners**](schema-dataroamingpartners-mbnprofile-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**DataRoamingPartners**](schema-dataroamingpartners-mbnprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**DataRoamingPartners (MBNProfile)**](schema-dataroamingpartners-mbnprofile-element.md)
</dt> </dl>

 

 




