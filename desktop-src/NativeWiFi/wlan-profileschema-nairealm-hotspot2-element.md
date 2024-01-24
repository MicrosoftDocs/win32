---
title: NAIRealm (Hotspot2) element
description: A list of Network Access Identifier (NAI) Realm identifiers.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NAIRealm
api_type: 
- Schema
api_location: 
ms.assetid: e77802ee-4017-4f04-ae71-5d6d0de8fcf3
---

# NAIRealm (Hotspot2) element

A list of Network Access Identifier (NAI) Realm identifiers. Entries in this list are usually of the form `user@domain`. The NAI Realm list is the preferred method to identify most non-mobile operators like MSOs, wireline operators, and public venues.

```XSD
<xs:element name="NAIRealm"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="name"
                minOccurs="0"
                maxOccurs="256"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:minLength value="1">
                        <xs:maxLength value="255">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**Hotspot2 (WLANProfile)**](./wlan-profileschema-hotspot2-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**name**](#name) | | A single realm identifier. Usually of the form `user@domain`. |

### name

A single realm identifier. Usually of the form `user@domain`.

## Requirements

TBD
