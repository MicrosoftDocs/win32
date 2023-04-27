---
title: randomizationSeed (MacRandomization) element
description: Randomization seed is a DWORD value that differentiates various versions of the same profile.
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- nonBroadcast
api_type: 
- Schema
api_location: 
---

# randomizationSeed (MacRandomization) element

Randomization seed is a DWORD value that differentiates various versions of the same profile.

``` syntax
<!-- Randomization seed is a DWORD value that differentiates various versions of the same profile -->
<xs:element name="randomizationSeed"
    type="integer"
    minOccurs="0"
    />
```

The element is defined by the [**MacRandomization**](wlan-profileschema-macrandomization-wlanprofile-element.md) element.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |

## See also

**Definition context of element in schema**

* [**MacRandomization**](wlan-profileschema-macrandomization-wlanprofile-element.md)

**Possible immediate parent element in schema instance**

* [**MacRandomization (WLANProfile)**](wlan-profileschema-macrandomization-wlanprofile-element.md)
