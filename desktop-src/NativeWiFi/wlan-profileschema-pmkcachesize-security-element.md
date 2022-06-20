---
description: Specifies the number of entries in the PMK cache on the client.
ms.assetid: 3a53f7fd-7f12-43d3-94e6-a11bec389a34
title: PMKCacheSize (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PMKCacheSize
api_type: 
- Schema
api_location: 
---

# PMKCacheSize (security) Element

The PMKCacheSize (security) element specifies the number of entries in the PMK cache on the client. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-pmkcachemode-security-element.md) set to "enabled". If **PMKCacheMode** is enabled, and this element is absent, the size of the cache defaults to 128 entries.

PMK caching is described in the [802.11i](https://standards.ieee.org/ieee/802.11i/3127/) specification.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
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
```

The element is defined by the [**security**](wlan-profileschema-security-msm-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 




