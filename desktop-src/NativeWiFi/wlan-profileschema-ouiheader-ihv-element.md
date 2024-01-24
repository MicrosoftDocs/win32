---
title: OUIHeader (IHV) element
description: Identifies the IHV.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OUIHeader
api_type: 
- Schema
api_location: 
ms.assetid: a99c231c-afd7-44e6-81af-3d49ffef8714
---

# OUIHeader (IHV) element

The OUIHeader (IHV) element identifies the IHV.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

```XSD
<xs:element name="OUIHeader">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OUI">
                <xs:simpleType>
                    <xs:restriction base="xs:hexBinary">
                        <xs:length value="3">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="type">
                <xs:simpleType>
                    <xs:restriction base="xs:hexBinary">
                        <xs:length value="1">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
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

* [**IHV (WLANProfile)**](./wlan-profileschema-ihv-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**OUI**](#oui) | | Contains a 3 byte hexBinary that identifies the IHV. |
| [**type**](#type) | | Contains a 1 byte hexBinary that is used to differentiate NICs by the same IHV. |

### OUI

Contains a 3-byte hexBinary that identifies the IHV.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### type

Contains a 1-byte hexBinary that's used to differentiate between NICs made by the same IHV.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
