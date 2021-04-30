---
description: Defines a string type for either the name or the description of a wireless LAN policy profile.
ms.assetid: a01e8789-3401-4e58-b733-2ec95fc895b6
title: nameType Simple Type (LAN_policy)
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

# nameType Simple Type (LAN_policy)

The nameType simple type defines a string type for either the name or the description of a wireless LAN policy profile. Names and descriptions are strings that are at least one character long and at most 255 characters long.

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
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




