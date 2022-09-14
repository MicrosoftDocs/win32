---
description: Indicates whether pre-authentication will be used by the client.
ms.assetid: 305d77b6-fe2d-45c6-ac91-5769f91de152
title: preAuthMode (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- preAuthMode
api_type: 
- Schema
api_location: 
---

# preAuthMode (security) Element

The preAuthMode (security) element indicates whether pre-authentication will be used by the client. Pre-authentication is necessary for WPA2 secure fast roaming. This element is valid only for WPA2-defined networks with [**PMKCacheMode**](wlan-profileschema-pmkcachemode-security-element.md) set to "enabled". If **PMKCacheMode** is enabled, and this element is absent, the default value is "disabled".

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
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

 

 




