---
description: Specifies the authentication and encryption pair to be used for this profile.
ms.assetid: d7a69b82-3f04-49eb-80cc-675d5a0a559a
title: authEncryption (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authEncryption
api_type: 
- Schema
api_location: 
---

# authEncryption (security) Element

The authEncryption (security) element specifies the authentication and encryption pair to be used for this profile.

``` syntax
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
```

The element is defined by the [**security**](wlan-profileschema-security-msm-element.md) element.

## Child elements



| Element                                                                            | Type                                                              | Description                                                                                      |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**authentication**](wlan-profileschema-authentication-authencryption-element.md) |                                                                   | Specifies the authentication method that must be used to connect to the wireless LAN.<br/> |
| [**encryption**](wlan-profileschema-encryption-authencryption-element.md)         |                                                                   | Sets the data encryption to use to connect to the wireless LAN.<br/>                       |
| [**useOneX**](wlan-profileschema-useonex-authencryption-element.md)               | [boolean](/dotnet/api/system.boolean) | Indicates whether 802.1X is used.<br/>                                                     |



## Remarks

The [**FIPSMode**](wlan-profileschema-fipsmode-authencryption-element.md) element can be inserted as a child of the **authEncryption** element.

## Examples

To view sample profiles that use the **authEncryption** element, see [Wireless Profile Samples](wireless-profile-samples.md). To view a sample profile that uses the [**FIPSMode**](wlan-profileschema-fipsmode-authencryption-element.md) element, see [FIPS Profile Sample](fips-profile-sample.md).

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

[**security**](wlan-profileschema-security-msm-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**security (MSM)**](wlan-profileschema-security-msm-element.md)
</dt> </dl>

 

 
