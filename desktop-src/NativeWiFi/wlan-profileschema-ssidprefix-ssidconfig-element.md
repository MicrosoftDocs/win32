---
title: SSIDPrefix (SSIDConfig) element
description: Contains an SSID prefix for a wireless LAN.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SSIDPrefix
api_type: 
- Schema
api_location: 
---

# SSIDPrefix (SSIDConfig) element

The SSIDPrefix (SSIDConfig) element contains an SSID prefix for a wireless LAN.

```XSD
<xs:element name="SSIDPrefix">
    <xs:complexType>
        <xs:sequence>
            <!-
                Either Hex or named SSID must be present.
                Hex SSID takes precedence over named SSID.
             ->
            <xs:element name="hex"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:hexBinary">
                        <xs:minLength value="4">
                        <xs:maxLength value="32">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="name"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:minLength value="4">
                        <xs:maxLength value="32">
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

* [**SSIDConfig (WLANProfile)**](./wlan-profileschema-ssidconfig-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**hex**](#hex) | | Contains the SSID prefix of a wireless LAN in hexadecimal format. |
| [**name**](#name) | | Contains the SSID prefix for a wireless LAN. |

### hex

Contains the SSID prefix of a wireless LAN in hexadecimal format.

### name

Contains the SSID prefix of a wireless LAN.

A **name** is case-sensitive.

## Remarks

Although the [**hex**](#hex) and [**name**](#name) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element. If both are present, then **hex** takes precedence over **name**.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
