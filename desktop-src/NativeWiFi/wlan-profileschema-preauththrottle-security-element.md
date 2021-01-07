---
description: Specifies the number pre-authentication attempts to try on neighboring APs.
ms.assetid: 7e89e962-7544-4efb-9e3c-c108bee22aea
title: preAuthThrottle (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- preAuthThrottle
api_type: 
- Schema
api_location: 
---

# preAuthThrottle (security) Element

The preAuthThrottle (security) element specifies the number pre-authentication attempts to try on neighboring APs. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-pmkcachemode-security-element.md) set to "enabled". If **PMKCacheMode** is enabled, and this element is absent, the number of tries defaults to 3.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
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

 

 




