---
description: Defines a type for the SimIccID element of the Mobile Broadband profile.
ms.assetid: ce77180e-71e2-4cef-84e0-32397216385f
title: simIccIDType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- simIccIDType
api_type: 
- Schema
---

# simIccIDType Simple Type

The **simIccIDType** simple type defines a type for the [**SimIccID**](schema-simiccid-mbnprofile-element.md) element of the Mobile Broadband profile. This type is a collection of digits and/or upper- and lower-case letters, at least one character long and at most 20 characters long.

``` syntax
<xs:simpleType name="simIccIDType">
    <xs:restriction
        base="token"
    >
        <xs:pattern
            value="[a-zA-Z\d]{1,20}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **simIccIDType** simple type is a token that is restricted by the following pattern:

-   `[a-zA-Z\d]{1,20}`

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




