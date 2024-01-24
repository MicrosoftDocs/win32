---
title: networkFilter (WLANPolicy) element
description: Defines the list of allowed and denied networks for machines.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- networkFilter
api_type: 
- Schema
api_location: 
ms.assetid: 21502c97-36a4-4cd6-9dd0-ee44c4cc522f
---

# networkFilter (WLANPolicy) element

The networkFilter (WLANPolicy) element defines the list of allowed and denied networks for machines.

```XSD
<xs:element name="networkFilter"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="allowList"
                minOccurs="0"
                ...
             />
            <xs:element name="blockList"
                minOccurs="0"
                ...
             />
            <xs:element name="denyAllIBSS"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="denyAllESS"
                minOccurs="0"
                type="boolean"
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

* [WLANPolicy](./wlan-policyschema-wlanpolicy-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**allowList**](./wlan-policyschema-allowlist-networkfilter-element.md) | | Specifies the list of wireless LAN networks to which any machine must be allowed to connect. |
| [**blockList**](./wlan-policyschema-blocklist-networkfilter-element.md) | | Specifies the list of wireless LAN networks to which a machine must not connect. |
| [**denyAllIBSS**](#denyallibss) | boolean | Specifies if access to all ad-hoc networks is blocked. |
| [**denyAllESS**](#denyalless) | boolean | Specifies if access to all infrastructure networks is blocked. |

### denyAllIBSS

The denyAllIBSS (networkFilter) element specifies if access to all ad-hoc networks is blocked. When **denyAllIBSS** has a value of TRUE, machines cannot connect to an ad-hoc network; otherwise, machines may connect to ad-hoc networks.

The default value for this element is FALSE. If **denyAllIBSS** is not specified in a profile, then by default machines may connect to ad-hoc networks.

### denyAllESS

The denyAllESS (networkFilter) element specifies if access to all infrastructure networks is blocked. When **denyAllESS** has a value of TRUE, machines cannot connect to an infrastructure network; otherwise, machines may connect to infrastructure networks.

The default value for this element is FALSE. If **denyAllESS** is not specified in a profile, then by default machines may connect to infrastructure networks.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
