---
title: blockList (networkFilter) element
description: Specifies the list of wireless LAN networks to which a machine must not connect.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- blockList
api_type: 
- Schema
api_location: 
ms.assetid: 01db3f7e-1e27-4378-9c42-bc38192f9507
---

# blockList (networkFilter) element

The blockList (networkFilter) element specifies the list of wireless LAN networks to which a machine must not connect.

```XSD
<xs:element name="blockList"
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
| [**network**](./wlan-policyschema-network-blocklist-element.md) | | Defines a blocked network. |

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
