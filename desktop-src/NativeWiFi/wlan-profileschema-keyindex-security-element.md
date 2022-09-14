---
description: Specifies which key index should be used to encrypt wireless traffic. This is only used when keyType is set to &\#0034;networkKey&\#0034;.
ms.assetid: 5629605d-4c23-4318-8f09-939e13302552
title: keyIndex (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- keyIndex
api_type: 
- Schema
api_location: 
---

# keyIndex (security) Element

The keyIndex (security) element specifies which key index should be used to encrypt wireless traffic. This is only used when [**keyType**](wlan-profileschema-keytype-sharedkey-element.md) is set to "networkKey".

``` syntax
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
```

The element is defined by the [**security**](wlan-profileschema-security-msm-element.md) element.

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

 

 




