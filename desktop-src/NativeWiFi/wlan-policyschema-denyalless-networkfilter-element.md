---
description: Specifies if access to all infrastructure networks is blocked.
ms.assetid: d57ae27c-3cd3-4e53-b5c9-cd3cbb91289b
title: denyAllESS (networkFilter) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- denyAllESS
api_type: 
- Schema
api_location: 
---

# denyAllESS (networkFilter) Element

The denyAllESS (networkFilter) element specifies if access to all infrastructure networks is blocked. When **denyAllESS** has a value of TRUE, machines cannot connect to an infrastructure network; otherwise, machines may connect to infrastructure networks.

The default value for this element is FALSE. If **denyAllESS** is not specified in a profile, then by default machines may connect to infrastructure networks.

``` syntax
<xs:element name="denyAllESS"
    type="boolean"
 />
```

The **denyAllESS** element is defined by the [**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**networkFilter (WLANPolicy)**](wlan-policyschema-networkfilter-wlanpolicy-element.md)
</dt> </dl>

 

 




