---
description: Contain either the name or a description of a wireless LAN profile.
ms.assetid: cb30d76f-051f-4b90-a0e0-24088a99ca9b
title: nameType Simple Type (LAN_policy) (profile)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- nameType
api_type: 
- Schema
api_location: 
---

# nameType Simple Type (LAN_policy) for profileschema

The nameType simple type can contain either the name or a description of a wireless LAN profile. This string value must be between 1 and 255 characters long.

``` syntax
<xs:simpleType name="nameType">
    <xs:restriction
        base="string"
    >
        <xs:minLength
            value="1"
         />
        <xs:maxLength
            value="255"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



 

 




