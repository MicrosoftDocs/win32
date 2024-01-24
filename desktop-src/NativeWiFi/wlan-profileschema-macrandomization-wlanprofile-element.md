---
title: MacRandomization (WLANProfile) element
description: Configures the randomization of MAC addresses.
ms.topic: reference
ms.date: 06/25/2023
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

Configures the randomization of MAC addresses.

```XSD
<xs:element name="MacRandomization">
    <xs:complexType>
        <xs:sequence>
            <!-
                Flag for specifying Mac Address Randomization on this profile; default set by policy.
             ->
            <xs:element name="enableRandomization"
                minOccurs="0"
                type="boolean"
             />
            <!-
                Flag for specifying whether a new MAC shall be picked every day.
             ->
            <xs:element name="randomizeEveryday"
                minOccurs="0"
                type="boolean"
             />
            <!-
                Randomization seed is a DWORD value that differentiates various versions of the same profile.
             ->
            <xs:element name="randomizationSeed"
                minOccurs="0"
                type="integer"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**WLANProfile**](./wlan-profileschema-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**enableRandomization**](#enablerandomization) | boolean | Flag for specifying Mac Address Randomization on this profile; default set by policy. |
| [**randomizeEveryday**](#randomizeeveryday) | boolean | Flag for specifying whether a new MAC shall be picked every day. |
| [**randomizationSeed**](#randomizationseed) | integer | Randomization seed is a DWORD value that differentiates various versions of the same profile. |

### enableRandomization

Flag for specifying Mac Address Randomization on this profile; default set by policy.

### randomizeEveryday

Flag for specifying whether a new MAC shall be picked every day.

### randomizationSeed

Randomization seed is a DWORD value that differentiates various versions of the same profile.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
