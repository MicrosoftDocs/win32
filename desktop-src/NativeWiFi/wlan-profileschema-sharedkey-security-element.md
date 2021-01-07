---
description: Contains shared key information.
ms.assetid: 9f401441-256c-4702-9503-f87b2b9cf0ee
title: sharedKey (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- sharedKey
api_type: 
- Schema
api_location: 
---

# sharedKey (security) Element

The sharedKey (security) element contains shared key information. This element is only required if WEP or PSK keys are required for the authentication and encryption pair.

``` syntax
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
```

The element is defined by the [**security**](wlan-profileschema-security-msm-element.md) element.

## Child elements



| Element                                                                 | Type                                                              | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**keyMaterial**](wlan-profileschema-keymaterial-sharedkey-element.md) | [string](/dotnet/api/system.string)   | Contains the network key or passphrase.<br/>                                                                                                                           |
| [**keyType**](wlan-profileschema-keytype-sharedkey-element.md)         |                                                                   | Type of key.<br/>                                                                                                                                                      |
| [**protected**](wlan-profileschema-protected-sharedkey-element.md)     | [boolean](/dotnet/api/system.boolean) | Indicates whether the key is encrypted.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element must have a value of FALSE.<br/> |



## Remarks

For Windows Vista and Windows Server 2008, the data associated with the **sharedKey** element is encrypted before it is saved in the profile store.

For Windows XP with SP3 and Wireless LAN API for Windows XP with SP2, the data is not encrypted.

## Examples

To view sample profiles that use the **sharedKey** element, see [Non-Broadcast Profile Sample](non-broadcast-profile-sample.md), [WPA-Personal Profile Sample](wpa-personal-profile-sample.md), and [WPA2-Personal Profile Sample](wpa2-personal-profile-sample.md).

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

[**security**](wlan-profileschema-security-msm-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**security (MSM)**](wlan-profileschema-security-msm-element.md)
</dt> </dl>

 

 
