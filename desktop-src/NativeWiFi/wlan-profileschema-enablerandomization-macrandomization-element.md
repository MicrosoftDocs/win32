---
title: enableRandomization (MacRandomization) element
description: Flag for specifying Mac Address Randomization on this profile, default set by policy.
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- enableRandomization
api_type: 
- Schema
api_location: 
---

# enableRandomization (MacRandomization) element

Flag for specifying Mac Address Randomization on this profile, default set by policy.

``` syntax
<!-- Flag for specifying Mac Address Randomization on this profile, default set by policy -->
<xs:element name="enableRandomization"
    type="boolean"
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
