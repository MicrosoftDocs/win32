---
description: Specifies the authentication method to be used to connect to the wireless LAN.
ms.assetid: fb6c5cce-05d6-41a2-acf4-9ae2713079dd
title: authentication (authEncryption) Element
ms.topic: reference
ms.date: 04/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authentication
api_type: 
- Schema
api_location: 
---

# authentication (authEncryption) Element

The authentication (authEncryption) element specifies the authentication method to be used to connect to the wireless LAN.

``` syntax
<xs:element name="authentication">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="open"
             />
            <xs:enumeration
                value="shared"
             />
            <xs:enumeration
                value="WPA"
             />
            <xs:enumeration
                value="WPAPSK"
             />
            <xs:enumeration
                value="WPA2"
             />
            <xs:enumeration
                value="WPA2PSK"
             />
            <xs:enumeration
                value="WPA3"
             />
            <xs:enumeration
                value="WPA3ENT192"
             />
            <xs:enumeration
                value="WPA3ENT"
             />
            <xs:enumeration
                value="WPA3SAE"
             />
            <xs:enumeration
                value="OWE"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element.

## Remarks

The following table describes the enumeration values.

| Value   | Description                            |
|---------|----------------------------------------|
| open    | Open 802.11 authentication.            |
| shared  | Shared 802.11 authentication.          |
| WPA     | WPA-Enterprise 802.11 authentication.  |
| WPAPSK  | WPA-Personal 802.11 authentication.    |
| WPA2    | WPA2-Enterprise 802.11 authentication. |
| WPA2PSK | WPA2-Personal 802.11 authentication.   |
| WPA3 | Deprecated (and synonymous with WPA3ENT192). Use WPA3ENT192 instead. |
| WPA3ENT192 | WPA3-Enterprise 192-bit mode authentication. |
| WPA3ENT | WPA3-Enterprise authentication. |
| WPA3SAE | WPA3-Simultaneous Authentication of Equals (WPA3-SAE) authentication. |
| OWE | Opportunistic wireless encryption (OWE) authentication. |

For more information about 802.11 authentication methods, see the [WPA](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access), [802.1X](https://ieeexplore.ieee.org/document/1438730), and [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specifications.

## Examples

To view sample profiles that use the **authentication** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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

[**authEncryption**](wlan-profileschema-authencryption-security-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**authEncryption (security)**](wlan-profileschema-authencryption-security-element.md)
</dt> </dl>
