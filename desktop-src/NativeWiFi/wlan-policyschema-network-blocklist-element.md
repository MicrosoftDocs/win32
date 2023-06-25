---
title: network (blockList) element
description: Defines a blocked network.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- network
api_type: 
- Schema
api_location: 
ms.assetid: ccf24d45-cae0-4eb7-951a-004a5f71e04a
---

# network (blockList) element

The network (blockList) element defines a blocked network. A machine cannot connect to a blocked network.

```XSD
<xs:element name="network"
    maxOccurs="unbounded"
    type="networkItemType"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="networkName"
                type="networkNameType"
             />
            <xs:element name="networkType"
                type="networkTypeType"
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

* [blockList (networkFilter)](./wlan-policyschema-blocklist-networkfilter-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**networkName**](#networkname) | [networkNameType](./wlan-policyschema-networkname-networkitemtype-element.md) | Specifies the service set identifier (SSID) of the wireless network. |
| [**networkType**](#networktype) | [networkTypeType](./wlan-policyschema-networktype-networkitemtype-element.md) | Specifies a network type. |

### networkName

Specifies the service set identifier (SSID) of the wireless network.

### networkType

Specifies a network type. There are two types of networks: infrastructure networks (ESS) and ad-hoc networks (IBSS).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
