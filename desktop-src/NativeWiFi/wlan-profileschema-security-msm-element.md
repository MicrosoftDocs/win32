---
title: security (MSM) Element (LAN_policy) (WLAN)
description: Contains various security settings.
ms.topic: reference
ms.date: 05/25/2023
ms.assetid: 1d912fb1-8fb4-4761-8991-5a50ffb0399e
topic_type: 
- APIRef
- kbSyntax
api_name: 
- security
api_type: 
- Schema
api_location: 
---

# security (MSM) element (LAN_policy) for WLAN

The security (MSM) element contains various security settings.

``` syntax
<xs:element name="security"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="authEncryption"
                ...
            />
            <xs:element name="sharedKey"
                ...
            />
            <xs:element name="keyIndex"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:minInclusive
                            value="0"
                         />
                        <xs:maxInclusive
                            value="3"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="PMKCacheMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="disabled"
                         />
                        <xs:enumeration
                            value="enabled"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="PMKCacheTTL"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:minInclusive
                            value="5"
                         />
                        <xs:maxInclusive
                            value="1400"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="PMKCacheSize"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:minInclusive
                            value="1"
                         />
                        <xs:maxInclusive
                            value="255"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="preAuthMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="disabled"
                         />
                        <xs:enumeration
                            value="enabled"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="preAuthThrottle"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:minInclusive
                            value="1"
                         />
                        <xs:maxInclusive
                            value="16"
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

## Parent elements

* [**MSM (WLANProfile)**](wlan-profileschema-msm-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
|-|-|-|
| [**authEncryption**](wlan-profileschema-authencryption-security-element.md) | | Specifies the authentication and encryption pair to be used for this profile. |
| [**keyIndex**](#keyindex) | | Specifies which key index should be used to encrypt wireless traffic. This is used only when [**keyType**](wlan-profileschema-sharedkey-security-element.md#keytype) is set to "networkKey". |
| [**PMKCacheMode**](#pmkcachemode) | | Indicates whether PMK caching will be used. This element is valid only for WPA2-defined networks.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**PMKCacheSize**](#pmkcachesize) | | Specifies the number of entries in the PMK cache on the client. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the size of the cache defaults to 128 entries.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**PMKCacheTTL**](#pmkcachettl) | | Indicates the length of time, in minutes, that a PMK cache will be kept. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**preAuthMode**](#preauthmode) | | Determines if pre-authentication will be used by the client. Pre-authentication enables WPA2 secure fast roaming. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the default value is disabled.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**preAuthThrottle**](#preauththrottle) | | Indicates the number of tries when preauthenticating to neighboring APs. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the number of tries defaults to 3.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) | | Contains the shared key information. This element is only required if WEP or PSK keys are required for the authentication and encryption pair. |

### keyIndex

Specifies which key index should be used to encrypt wireless traffic. This is used only when [**keyType**](wlan-profileschema-sharedkey-security-element.md#keytype) is set to "networkKey".

### PMKCacheMode

Specifies whether PMK caching will be used. This element is valid only for WPA2-defined networks. PMK caching is described in the [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specification.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### PMKCacheSize

Specifies the number of entries in the PMK cache on the client. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-security-msm-element.md#pmkcachemode) set to "enabled". If **PMKCacheMode** is enabled, and **PMKCacheSize** is absent, then the size of the cache defaults to 128 entries.

PMK caching is described in the [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specification.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### PMKCacheTTL

Specifies the length of time, in minutes, that a PMK cache will be kept. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-security-msm-element.md#pmkcachemode) set to "enabled".

PMK caching is described in the [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specification.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### preAuthMode

Specifies whether pre-authentication will be used by the client. Pre-authentication is necessary for WPA2 secure fast roaming. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-security-msm-element.md#pmkcachemode) set to "enabled". If **PMKCacheMode** is enabled, and **preAuthMode** is absent, then the default value is "disabled".

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### preAuthThrottle

Specifies the number of pre-authentication attempts to try on neighboring APs. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-security-msm-element.md#pmkcachemode) set to "enabled". If **PMKCacheMode** is enabled, and **preAuthThrottle** is absent, then the number of tries defaults to 3.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

## Examples

To view sample profiles that use the **security** element, see [Wireless profile samples](wireless-profile-samples.md).

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
