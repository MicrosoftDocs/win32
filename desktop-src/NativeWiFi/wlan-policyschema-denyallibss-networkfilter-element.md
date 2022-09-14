---
description: Specifies if access to all ad-hoc networks is blocked.
ms.assetid: 9001ccbb-c158-44d7-8d31-38c91881886e
title: denyAllIBSS (networkFilter) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- denyAllIBSS
api_type: 
- Schema
api_location: 
---

# denyAllIBSS (networkFilter) Element

The denyAllIBSS (networkFilter) element specifies if access to all ad-hoc networks is blocked. When **denyAllIBSS** has a value of TRUE, machines cannot connect to an ad-hoc network; otherwise, machines may connect to ad-hoc networks.

The default value for this element is FALSE. If **denyAllIBSS** is not specified in a profile, then by default machines may connect to ad-hoc networks.

``` syntax
<xs:element name="denyAllIBSS"
    type="boolean"
 />
```

The **denyAllIBSS** element is defined by the [**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md) element.

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

 

 




