---
description: Contains various media-specific module (MSM) settings.
ms.assetid: 31f98af8-a577-4f6a-9a0a-b182b5a89cc3
title: MSM (WLANProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSM
api_type: 
- Schema
api_location: 
---

# MSM (WLANProfile) Element

The MSM (WLANProfile) element contains various media-specific module (MSM) settings.

``` syntax
<xs:element name="MSM"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="connectivity"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="phyType"
                            minOccurs="0"
                            maxOccurs="4"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="string"
                                >
                                    <xs:enumeration
                                        value="a"
                                     />
                                    <xs:enumeration
                                        value="b"
                                     />
                                    <xs:enumeration
                                        value="g"
                                     />
                                    <xs:enumeration
                                        value="n"
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
            <xs:element name="security"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="authEncryption">
                            <xs:complexType>
                                <xs:sequence>
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
                                            </xs:restriction>
                                        </xs:simpleType>
                                    </xs:element>
                                    <xs:element name="encryption">
                                        <xs:simpleType>
                                            <xs:restriction
                                                base="string"
                                            >
                                                <xs:enumeration
                                                    value="none"
                                                 />
                                                <xs:enumeration
                                                    value="WEP"
                                                 />
                                                <xs:enumeration
                                                    value="TKIP"
                                                 />
                                                <xs:enumeration
                                                    value="AES"
                                                 />
                                            </xs:restriction>
                                        </xs:simpleType>
                                    </xs:element>
                                    <xs:element name="useOneX"
                                        type="boolean"
                                        minOccurs="0"
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
                        <xs:element name="sharedKey"
                            minOccurs="0"
                        >
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="keyType">
                                        <xs:simpleType>
                                            <xs:restriction
                                                base="string"
                                            >
                                                <xs:enumeration
                                                    value="networkKey"
                                                 />
                                                <xs:enumeration
                                                    value="passPhrase"
                                                 />
                                            </xs:restriction>
                                        </xs:simpleType>
                                    </xs:element>
                                    <xs:element name="protected"
                                        type="boolean"
                                     />
                                    <xs:element name="keyMaterial"
                                        type="string"
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

The element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Child elements



| Element                                                                            | Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**authEncryption**](wlan-profileschema-authencryption-security-element.md)       |                                                                   | Specifies the authentication and encryption pair to be used for this profile.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**authentication**](wlan-profileschema-authentication-authencryption-element.md) |                                                                   | Specifies the authentication and encryption pair to be used for this profile.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**connectivity**](wlan-profileschema-connectivity-msm-element.md)                |                                                                   | Contains various connectivity settings. This element is optional.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**encryption**](wlan-profileschema-encryption-authencryption-element.md)         |                                                                   | Sets the data encryption to use to connect to the wireless LAN.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| [**keyIndex**](wlan-profileschema-keyindex-security-element.md)                   |                                                                   | Specifies which key index must be used to encrypt wireless traffic. This is only used when keyType is set to networkKey.<br/>                                                                                                                                                                                                                                                                                          |
| [**keyMaterial**](wlan-profileschema-keymaterial-sharedkey-element.md)            | [string](/dotnet/api/system.string)   | Contains the network key or passphrase.<br/>                                                                                                                                                                                                                                                                                                                                                                           |
| [**keyType**](wlan-profileschema-keytype-sharedkey-element.md)                    |                                                                   | Type of key.<br/>                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**phyType**](wlan-profileschema-phytype-connectivity-element.md)                 |                                                                   | Specifies the 802.11 wireless LAN standard used on the wireless LAN. The value "n" is only supported on Windows Vista with SP1 and later versions of the operating system.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/>                                                                                                                        |
| [**PMKCacheMode**](wlan-profileschema-pmkcachemode-security-element.md)           |                                                                   | Indicates whether PMK caching will be used. This element is valid only for WPA2-defined networks.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/>                                                                                                                                                                                                 |
| [**PMKCacheSize**](wlan-profileschema-pmkcachesize-security-element.md)           |                                                                   | Specifies the number of entries in the OMK cache on the client. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the size of the cache defaults to 128 entries.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/>                                   |
| [**PMKCacheTTL**](wlan-profileschema-pmkcachettl-security-element.md)             |                                                                   | Indicates the length of time, in minutes, that a PMK cache will be kept. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/>                                                                                                                                  |
| [**preAuthMode**](wlan-profileschema-preauthmode-security-element.md)             |                                                                   | Determines if pre-authentication will be used by the client. Pre-authentication enables WPA2 secure fast roaming. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the default value is disabled.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/> |
| [**preAuthThrottle**](wlan-profileschema-preauththrottle-security-element.md)     |                                                                   | Indicates the number of tries when preauthenticating to neighboring APs. This element is valid only for WPA2-defined networks with PMKCache mode set to enabled. If PMKCache mode is enabled, and this element is absent, the number of tries defaults to 3.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.<br/>                                      |
| [**protected**](wlan-profileschema-protected-sharedkey-element.md)                | [boolean](/dotnet/api/system.boolean) | Indicates whether the key is encrypted.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element must have a value of FALSE.<br/>                                                                                                                                                                                                                                                 |
| [**security**](wlan-profileschema-security-msm-element.md)                        |                                                                   | Contains various security settings. This element is optional.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| [**sharedKey**](wlan-profileschema-sharedkey-security-element.md)                 |                                                                   | Contains the shared key information. This element is only required if WEP or PSK keys are required for the authentication and encryption pair.<br/>                                                                                                                                                                                                                                                                    |
| [**useOneX**](wlan-profileschema-useonex-authencryption-element.md)               | [boolean](/dotnet/api/system.boolean) | Indicates whether 802.1X is used. This flag is optional.<br/>                                                                                                                                                                                                                                                                                                                                                          |



## Remarks

The [**FIPSMode**](wlan-profileschema-fipsmode-authencryption-element.md) element can be inserted as a child of the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element. The [**OneX**](onexschema-onex-element.md) element can be inserted as a child of the [**security (MSM)**](wlan-profileschema-security-msm-element.md) element.

## Examples

To view sample profiles that use the **MSM** element, see [Wireless Profile Samples](wireless-profile-samples.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

[Wireless Profile Samples](wireless-profile-samples.md)
</dt> <dt>

**Definition context of element in schema**
</dt> <dt>

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> </dl>

 

 
