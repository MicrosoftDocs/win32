---
title: SSID (SSIDConfig) element
description: Contains an SSID for a wireless LAN.
ms.assetid: fb3466c4-a586-424b-96e2-ba287c99a1d9
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SSID
api_type: 
- Schema
api_location: 
---

# SSID (SSIDConfig) element

The SSID (SSIDConfig) element contains an SSID for a wireless LAN.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** At most one **SSID** element can appear in a profile.

``` syntax
<xs:element name="SSID"
    maxOccurs="256"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="hex"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="hexBinary"
                    >
                        <xs:minLength
                            value="1"
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
                            value="1"
                         />
                        <xs:maxLength
                            value="32"
                         />
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

The **SSID** element is defined by the [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) element.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**hex**](wlan-profileschema-hex-ssid-element.md) | | Contains the SSID of a wireless LAN in hexadecimal format.|
| [**name**](wlan-profileschema-name-ssid-element.md) | | Contains the SSID for a wireless LAN.|

## Remarks

Although the [**hex**](wlan-profileschema-hex-ssid-element.md) and [**name**](wlan-profileschema-name-ssid-element.md) elements are optional, at least one **hex** or [**name**](wlan-profileschema-name-ssid-element.md) element must appear as a child of the **SSID** element.

When profile information is converted to an SSID, the [**hex**](wlan-profileschema-hex-ssid-element.md) element is converted to the SSID (if present) and the [**name**](wlan-profileschema-name-ssid-element.md) element is ignored. If the **hex** element is not present, the [**name**](wlan-profileschema-name-ssid-element.md) element is converted to an SSID using Unicode to ASCII conversion.

When an SSID is stored in a profile, the [**hex**](wlan-profileschema-hex-ssid-element.md) element is always generated. The [**name**](wlan-profileschema-name-ssid-element.md) element is only generated if the both the ASCII to Unicode conversion of the SSID and the XML profile generation are successful. Some information from the original SSID may be lost when it is converted to a [**name**](wlan-profileschema-name-ssid-element.md).

## Examples

To view sample profiles that use the **SSID** element, see [Wireless Profile Samples](wireless-profile-samples.md).

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |

## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
</dt> </dl>
