---
title: name (SSIDPrefix) element
description: Contains the SSID prefix of a wireless LAN.
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- name
api_type: 
- Schema
api_location: 
---

# name (SSIDPrefix) element

The name (SSIDPrefix) element contains the SSID prefix of a wireless LAN.

``` syntax
<xs:element name="name"
    minOccurs="0"
>
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:minLength
                value="4"
                />
            <xs:maxLength
                value="32"
                />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**SSIDPrefix**](wlan-profileschema-ssidprefix-ssidconfig-element.md) element.

## Remarks

Names are case-sensitive.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |

## See also

**Definition context of element in schema**

* [**SSIDPrefix**](wlan-profileschema-ssidprefix-ssidconfig-element.md)

**Possible immediate parent element in schema instance**

* [**SSIDPrefix (SSIDConfig)**](wlan-profileschema-ssidprefix-ssidconfig-element.md)
