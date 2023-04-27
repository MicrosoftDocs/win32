---
title: MacRandomization (WLANProfile) element
description: The MacRandomization (WLANProfile) element configures the randomization of MAC addresses.
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MacRandomization
api_type: 
- Schema
api_location: 
---

# MacRandomization (WLANProfile) element

The MacRandomization (WLANProfile) element configures the randomization of MAC addresses.

``` syntax
<xs:element name="MacRandomization"
>
    <xs:complexType>
        <xs:sequence>
            <!-- Flag for specifying Mac Address Randomization on this profile, default set by policy -->
            <xs:element name="enableRandomization"
                type="boolean"
                minOccurs="0"
             />
            <!-- Flag for specifying whether a new MAC shall be picked every day -->
            <xs:element name="randomizeEveryday"
                type="boolean"
                minOccurs="0"
             />
            <!-- Randomization seed is a DWORD value that differentiates various versions of the same profile -->
            <xs:element name="randomizationSeed"
                type="integer"
                minOccurs="0"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **MacRandomization** element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**enableRandomization**](wlan-profileschema-enablerandomization-macrandomization-element.md) | | Flag for specifying Mac Address Randomization on this profile, default set by policy.|
| [**randomizeEveryday**](wlan-profileschema-randomizeeveryday-macrandomization-element.md) | | Flag for specifying whether a new MAC shall be picked every day.|
| [**randomizationSeed**](wlan-profileschema-randomizationseed-macrandomization-element.md) | | Randomization seed is a DWORD value that differentiates various versions of the same profile.|

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |

## See also

**Definition context of element in schema**

* [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)

**Possible immediate parent element in schema instance**

* [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
