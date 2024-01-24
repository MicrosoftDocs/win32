---
description: Defines a string type for the ICONFilePath element in the Mobile Broadband profile.
ms.assetid: 053bc5b8-fab2-4abe-97f8-ed98aea880b1
title: iconFileType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- iconFileType
api_type: 
- Schema
---

# iconFileType Simple Type

The **iconFileType** simple type defines a string type for the [**ICONFilePath**](schema-iconfilepath-mbnprofile-element.md) element in the Mobile Broadband profile. This string is at least one character long and at most 1024 characters long.

``` syntax
<xs:simpleType name="iconFileType">
    <xs:restriction
        base="token"
    >
        <xs:minLength
            value="1"
         />
        <xs:maxLength
            value="1024"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




