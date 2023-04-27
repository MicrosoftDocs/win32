---
title: SSIDPrefix (SSIDConfig) element
description: Contains an SSID prefix for a wireless LAN.
ms.topic: reference
ms.date: 04/26/2023
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

``` syntax
<xs:element name="SSIDPrefix"
>
    <xs:complexType>
        <xs:sequence>
            <!-- Either Hex or named SSID must be present. -->
            <!-- Hex SSID takes precedence over named SSID. -->
            <xs:element name="hex"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="hexBinary"
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
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **SSIDPrefix** element is defined by the [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) element.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**hex**](wlan-profileschema-hex-ssidprefix-element.md) | | Contains the SSID prefix of a wireless LAN in hexadecimal format.|
| [**name**](wlan-profileschema-name-ssidprefix-element.md) | | Contains the SSID prefix for a wireless LAN.|

## Remarks

Although the [**hex**](wlan-profileschema-hex-ssidprefix-element.md) and [**name**](wlan-profileschema-name-ssidprefix-element.md) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element. If both are present, then **hex** takes precedence over **name**.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |

## See also

**Definition context of element in schema**

* [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md)

**Possible immediate parent element in schema instance**

* [**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
