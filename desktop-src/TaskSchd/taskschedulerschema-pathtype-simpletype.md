---
title: pathType Simple Type
description: Defines the minimum and maximum number of characters for a string that defines a file path.
ms.assetid: 09908f75-ba7b-4e31-877e-80fabea6bd27
keywords:
- pathType simple type Task Scheduler
topic_type:
- apiref
api_name:
- pathType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# pathType Simple Type

Defines the minimum and maximum number of characters for a string that defines a file path. The path cannot be an empty string, and must be less than 260 characters.

``` syntax
<xs:simpleType name="pathType">
    <xs:restriction
        base="nonEmptyString"
    >
        <xs:maxLength
            value="260"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





