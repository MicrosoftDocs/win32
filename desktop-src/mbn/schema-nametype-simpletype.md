---
Description: Defines a string type for the Mobile Broadband profile.
ms.assetid: a5c14c39-2731-44f0-9fd2-e78d900b66f0
title: nameType Simple Type
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- nameType
api_type: 
- Schema
---

# nameType Simple Type

The **nameType** simple type defines a string type for the Mobile Broadband profile. This string is at least one character long and at most 255 characters long.

``` syntax
<xs:simpleType name="nameType">
    <xs:restriction
        base="normalizedString"
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



|                                     |                                                   |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




