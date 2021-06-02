---
description: Specifies a network type.
ms.assetid: fe3044ab-6e93-48f8-b8cb-fdf984987232
title: networkType (networkItemType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- networkType
api_type: 
- Schema
api_location: 
---

# networkType (networkItemType) Element

The networkType (networkItemType) element specifies a network type. There are two types of networks: infrastructure networks (ESS) and ad-hoc networks (IBSS).

``` syntax
<xs:element name="networkType"
    type="networkTypeType"
 />
```

The **networkType** element is defined by the [**networkItemType**](wlan-policyschema-networkitemtype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**networkItemType**](wlan-policyschema-networkitemtype-complextype.md)
</dt> <dt>

**Possible immediate parent elements in schema instance**
</dt> <dt>

[**network (allowList)**](wlan-policyschema-network-allowlist-element.md)
</dt> <dt>

[**network (blockList)**](wlan-policyschema-network-blocklist-element.md)
</dt> </dl>

 

 




