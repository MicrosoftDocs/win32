---
title: authEncryption (security) element
description: Specifies the authentication and encryption pair to be used for this profile.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authEncryption
api_type: 
- Schema
api_location: 
ms.assetid: d7a69b82-3f04-49eb-80cc-675d5a0a559a
---

# authEncryption (security) element

The authEncryption (security) element specifies the authentication and encryption pair to be used for this profile.

```XSD
<xs:element name="authEncryption"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="authentication">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="open">
                        <xs:enumeration value="shared">
                        <xs:enumeration value="WPA">
                        <xs:enumeration value="WPAPSK">
                        <xs:enumeration value="WPA2">
                        <xs:enumeration value="WPA2PSK">
                        <xs:enumeration value="WPA3">
                        <xs:enumeration value="WPA3ENT192">
                        <xs:enumeration value="WPA3ENT">
                        <xs:enumeration value="WPA3SAE">
                        <xs:enumeration value="OWE">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="encryption">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="none">
                        <xs:enumeration value="WEP">
                        <xs:enumeration value="TKIP">
                        <xs:enumeration value="AES">
                        <xs:enumeration value="GCMP256">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="useOneX"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="FIPSMode"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="transitionMode"
                type="boolean"
             />
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

* [**security (MSM)**](./wlan-profileschema-security-msm-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**authentication**](#authentication) | | Specifies the authentication method to be used to connect to the wireless LAN. |
| [**encryption**](#encryption) | | Specifies the type of data encryption to use to connect to a wireless LAN. |
| [**useOneX**](#useonex) | boolean | Indicates whether 802.1X authentication is used. |
| [**FIPSMode**](#fipsmode) | boolean | Indicates whether Federal Information Processing Standards (FIPS) mode is enabled. |
| [**transitionMode**](#transitionmode) | boolean | Transition mode configuration. |

### authentication

Specifies the authentication method to be used to connect to the wireless LAN.

| Value | Description |
|-|-|
| open | Open 802.11 authentication. |
| shared | Shared 802.11 authentication. |
| WPA | WPA-Enterprise 802.11 authentication. |
| WPAPSK | WPA-Personal 802.11 authentication. |
| WPA2 | WPA2-Enterprise 802.11 authentication. |
| WPA2PSK | WPA2-Personal 802.11 authentication. |
| WPA3 | Deprecated (and synonymous with WPA3ENT192). Use WPA3ENT192 instead. |
| WPA3ENT192 | WPA3-Enterprise 192-bit mode authentication. |
| WPA3ENT | WPA3-Enterprise authentication. |
| WPA3SAE | WPA3-Simultaneous Authentication of Equals (WPA3-SAE) authentication. |
| OWE | Opportunistic wireless encryption (OWE) authentication. |

For more information about 802.11 authentication methods, see the [WPA](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access), [802.1X](https://ieeexplore.ieee.org/document/1438730), and [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specifications.

### encryption

Specifies the type of data encryption to use to connect to a wireless LAN.

When the **encryption** element has a value of WEP, [**keyType**](wlan-profileschema-sharedkey-security-element.md#keytype) must be set to **networkKey**.

The AES encryption method is as specified in the [802.1X](https://ieeexplore.ieee.org/document/1438730) and [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specifications.

### useOneX

Indicates whether 802.1X authentication is used.

### FIPSMode

Indicates whether Federal Information Processing Standards (FIPS) mode is enabled. When a wireless connection is operating in FIPS mode, the security level of the connection complies with the FIPS 140-2 standard. For more info about FIPS, see the [FIPS Home Page](https://www.itl.nist.gov/fipspubs/).

This element is optional. If this element isn't specified in a profile, then FIPS mode isn't enabled.

**FIPSMode** can be set to TRUE only when the following conditions are met:

- The [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) element has a value of `ESS` (that is, the connection is an infrastructure connection).
- The [**authentication**](wlan-profileschema-authencryption-security-element.md#authentication) element has a value of `WPA2` or `WPA2PSK`.
- The [**encryption**](wlan-profileschema-authencryption-security-element.md#encryption) element has a value of `AES`.

Unlike most elements in the WLAN\_profile schema, this element is in the `https://www.microsoft.com/networking/WLAN/profile/v2` namespace.

The value of the **FIPSMode** element is ignored if the miniport driver for the wireless interface doesn't support FIPS mode.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. If **FIPSMode** is present in a profile, then the element is ignored.

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

### transitionMode

Transition mode configuration.

## Examples

To view sample profiles that use the **authEncryption** element and its child elements, see [Wireless profile samples](wireless-profile-samples.md). To view a sample profile that uses the [**FIPSMode**](wlan-profileschema-authencryption-security-element.md#fipsmode) element, see [FIPS profile sample](fips-profile-sample.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
