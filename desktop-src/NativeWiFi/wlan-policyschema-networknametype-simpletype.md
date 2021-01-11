---
description: Defines a string type for service set identifiers (SSIDs).
ms.assetid: c9e79a3d-7d5c-4320-ade2-40124de00920
title: networkNameType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- networkNameType
api_type: 
- Schema
api_location: 
---

# networkNameType Simple Type

The networkNameType simple type defines a string type for service set identifiers (SSIDs). A SSID is a string that is at least one character long and at most 32 characters long.

``` syntax
<xs:simpleType name="networkNameType">
    <xs:restriction
        base="string"
    >
        <xs:minLength
            value="1"
         />
        <xs:maxLength
            value="32"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




