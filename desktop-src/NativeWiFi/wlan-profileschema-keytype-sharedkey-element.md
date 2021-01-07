---
description: Indicates whether the shared key will be a network key or a pass phrase.
ms.assetid: 2cc909bb-7de6-492b-81ca-ddde93c17f63
title: keyType (sharedKey) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- keyType
api_type: 
- Schema
api_location: 
---

# keyType (sharedKey) Element

The keyType (sharedKey) element indicates whether the shared key will be a network key or a pass phrase.

``` syntax
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
```

The element is defined by the [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) element.

## Remarks

When the [**encryption**](wlan-profileschema-encryption-authencryption-element.md) element has a value of WEP, **keyType** must be set to **networkKey**.

## Examples

To view sample profiles that use the **keyType** element, see [Non-Broadcast Profile Sample](non-broadcast-profile-sample.md), [WPA-Personal Profile Sample](wpa-personal-profile-sample.md), and [WPA2-Personal Profile Sample](wpa2-personal-profile-sample.md).

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

[**sharedKey**](wlan-profileschema-sharedkey-security-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**sharedKey (security)**](wlan-profileschema-sharedkey-security-element.md)
</dt> </dl>

 

 




