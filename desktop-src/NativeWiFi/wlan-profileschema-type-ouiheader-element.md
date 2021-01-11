---
description: Contains a 1-byte hexBinary that is used to differentiate between NICs made by the same IHV.
ms.assetid: fd6bae3d-27a8-4bff-9340-b444312b8216
title: type (OUIHeader) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- type
api_type: 
- Schema
api_location: 
---

# type (OUIHeader) Element

The type (OUIHeader) element contains a 1-byte hexBinary that is used to differentiate between NICs made by the same IHV.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
<xs:element name="type">
    <xs:simpleType>
        <xs:restriction
            base="hexBinary"
        >
            <xs:length
                value="1"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**OUIHeader**](wlan-profileschema-ouiheader-ihv-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OUIHeader**](wlan-profileschema-ouiheader-ihv-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OUIHeader (IHV)**](wlan-profileschema-ouiheader-ihv-element.md)
</dt> </dl>

 

 




