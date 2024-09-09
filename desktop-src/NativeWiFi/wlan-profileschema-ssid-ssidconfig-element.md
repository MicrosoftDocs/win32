---
title: SSID (SSIDConfig) element
description: Contains an SSID for a wireless LAN.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SSID
api_type: 
- Schema
api_location: 
ms.assetid: fb3466c4-a586-424b-96e2-ba287c99a1d9
---

# SSID (SSIDConfig) element

The SSID (SSIDConfig) element contains an SSID for a wireless LAN. **SSID** *maxOccurs* is 1000 in v2; in v1, it's 256.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** At most one **SSID** element can appear in a profile.

```XSD
<xs:element name="SSID"
    maxOccurs="1000"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="hex"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:hexBinary">
                        <xs:minLength value="1">
                        <xs:maxLength value="32">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="name"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:minLength value="1">
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
| [**hex**](#hex) | | Contains the SSID of a wireless LAN in hexadecimal format. |
| [**name**](#name) | | Contains the SSID for a wireless LAN. |

### hex

Contains the SSID of a wireless LAN in hexadecimal format.

### name

Contains the SSID of a wireless LAN.

A **name** is case-sensitive.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** XML escape characters, such as &, are not displayed. Avoid using XML escape characters in SSID names for profiles deployed on Windows XP with SP3 and Wireless LAN API for Windows XP with SP2.

## Remarks

Although the [**hex**](#hex) and [**name**](#name) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element.

When profile information is converted to an SSID, the **hex** element is converted to the SSID (if present), and the **name** element is ignored. If the **hex** element isn't present, then the **name** element is converted to an SSID using Unicode-to-ASCII conversion.

When an SSID is stored in a profile, the **hex** element is always generated. The **name** element is generated only if the both the ASCII-to-Unicode conversion of the SSID and the XML profile generation are successful. Some information from the original SSID might be lost when it's converted to a **name**.

## Examples

To view sample profiles that use the **SSID** element and its child elements, see [Wireless profile samples](wireless-profile-samples.md). To view a sample profile that uses the **hex** element, see [FIPS profile sample](fips-profile-sample.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
