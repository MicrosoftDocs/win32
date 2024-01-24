---
title: RoamingConsortium (Hotspot2) element
description: A list of Organizationally Unique Identifiers (OUI) assigned by IEEE.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RoamingConsortium
api_type: 
- Schema
api_location: 
ms.assetid: 4a9885b6-2e57-4a16-8e1d-b5b0797e09db
---

# RoamingConsortium (Hotspot2) element

A list of Organizationally Unique Identifiers (OUI) assigned by IEEE.

```XSD
<xs:element name="RoamingConsortium"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OUI"
                minOccurs="0"
                maxOccurs="256"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:hexBinary">
                        <xs:minLength value="3">
                        <xs:maxLength value="5">
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
| [**OUI**](#oui) | | A single OUI, formatted as a variable size hexadecimal number. |

### OUI

A single OUI, formatted as a variable size hexadecimal number.

## Requirements

TBD
