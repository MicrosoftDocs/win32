---
title: nonEmptyStringType Simple Type
description: Defines the values used for a non-empty string of text.
ms.assetid: cb3b1ca6-4531-467c-a27a-b27a62233514
keywords:
- nonEmptyString simple type Task Scheduler
topic_type:
- apiref
api_name:
- nonEmptyString
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# nonEmptyStringType Simple Type

Defines the values used for a non-empty string of text.

``` syntax
<xs:simpleType name="nonEmptyString">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="1"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **nonEmptyString** simple type defines the following value.



| Value | Description                                            |
|-------|--------------------------------------------------------|
| 1     | The string contains at least one character.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





