---
description: Contains a 3 byte hexBinary that identifies the IHV.
ms.assetid: 0b2e73fb-df3a-48c4-b38d-970c37de46eb
title: OUI (OUIHeader) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OUI
api_type: 
- Schema
api_location: 
---

# OUI (OUIHeader) Element

The OUI (OUIHeader) element contains a 3 byte hexBinary that identifies the IHV.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
<xs:element name="OUI">
    <xs:simpleType>
        <xs:restriction
            base="hexBinary"
        >
            <xs:length
                value="3"
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

 

 




