---
title: allowList (networkFilter) element
description: Specifies the list of wireless LAN networks to which any machine must be allowed to connect.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- allowList
api_type: 
- Schema
api_location: 
ms.assetid: e24557d8-dedf-4381-bba0-cdb7ea26083b
---

# allowList (networkFilter) element

The allowList (networkFilter) element specifies the list of wireless LAN networks to which any machine must be allowed to connect.

```XSD
<xs:element name="allowList"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="network"
                maxOccurs="unbounded"
                type="networkItemType"
                ...
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [networkFilter (WLANPolicy)](./wlan-policyschema-networkfilter-wlanpolicy-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**network**](./wlan-policyschema-network-allowlist-element.md) | [**networkItemType**](wlan-policyschema-networkitemtype-complextype.md) | Defines an allowed network. |

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
