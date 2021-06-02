---
description: Specifies the 802.11 wireless LAN standard used on a wireless LAN.
ms.assetid: 19582ff0-59bd-4c93-8c92-0135e6e025d2
title: phyType (connectivity) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- phyType
api_type: 
- Schema
api_location: 
---

# phyType (connectivity) Element

The phyType (connectivity) element specifies the 802.11 wireless LAN standard used on a wireless LAN.

You can specify multiple **phyType**s. If no **phyType** is specified, the profile can be used to connect to any **phyType**. The value "n" is only supported on Windows Vista with Service Pack 1 (SP1) and later versions of the operating system.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
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
```

The element is defined by the [**connectivity**](wlan-profileschema-connectivity-msm-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**connectivity**](wlan-profileschema-connectivity-msm-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**connectivity (MSM)**](wlan-profileschema-connectivity-msm-element.md)
</dt> </dl>

 

 




