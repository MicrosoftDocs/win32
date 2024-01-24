---
description: Defines the type that is used to specify valid values for the color of certain elements in a Journal XML file.
ms.assetid: 10a19f28-d0aa-4126-b3f5-fde35fc5fdb0
title: ColorType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ColorType
api_type: 
- Schema
api_location: 
---

# ColorType Simple Type

Defines the type that is used to specify valid values for the color of certain elements in a Journal XML file.

``` syntax
<xs:simpleType name="ColorType">
    <xs:restriction
        base="string"
     />
</xs:simpleType>
```

## Remarks

A color can be a hexadecimal RGB value in the format \#RRGGBB. It must match the following regular expression: \#\[0-9a-fA-F\]{6}. For example: "\#4a79B5".

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




