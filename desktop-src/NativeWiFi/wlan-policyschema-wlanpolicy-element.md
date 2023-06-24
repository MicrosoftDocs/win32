---
title: WLANPolicy element
description: Contains a wireless LAN policy.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WLANPolicy
api_type: 
- Schema
api_location: 
ms.assetid: 16ffb682-f88b-4ca1-a902-d2db5e347975
---

# WLANPolicy element

The **WLANPolicy** element contains a wireless LAN policy. This element is the unique root element for a wireless policy profile.

The target namespace for the **WLANPolicy** element is `https://www.microsoft.com/networking/WLAN/policy/v1`.

```XSD
<xs:element name="WLANPolicy">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="name"
                type="nameType"
             />
            <xs:element name="description"
                minOccurs="0"
                type="nameType"
             />
            <xs:element name="globalFlags"
                ...
             />
            <xs:element name="networkFilter"
                minOccurs="0"
                ...
             />
            <xs:element name="profileList"
                minOccurs="0"
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

None.

## Child elements

| Element | Type | Description |
| - | - | - |
| [**name**](#name) | [**nameType**](./wlan-policyschema-nametype-simpletype.md) | Contains the name of a wireless LAN policy. |
| [**description**](#description) | [**nameType**](./wlan-policyschema-nametype-simpletype.md) | Contains the description of a wireless LAN policy. |
| [**globalFlags**](./wlan-policyschema-globalflags-wlanpolicy-element.md) | | Contains the global settings for the Auto Configuration Module (ACM). |
| [**networkFilter**](./wlan-policyschema-networkfilter-wlanpolicy-element.md) | | Defines the list of allowed and denied networks for machines. |
| [**profileList**](#profilelist) | | profileList (WLANPolicy) Element - Contains a list of profiles to be applied at the domain or machine level. |

### name

The name (WLANPolicy) element contains the name of a wireless LAN policy.

Names are not case-sensitive.

### description

The description (WLANPolicy) element contains the description of a wireless LAN policy.

### profileList

The profileList (WLANPolicy) element contains a list of profiles to be applied at the domain or machine level. This element is optional. If this element is present, it must contain at least one profile.

Profiles should be based on the [WLAN\_profile schema](wlan-profileschema-schema.md), with a root element of [**WLANProfile**](wlan-profileschema-wlanprofile-element.md).

## Remarks

To view the list of child elements in a tree-like structure, see [WLAN\_policy Schema Elements](wlan-policyschema-elements.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
