---
title: versionType Simple Type
description: Defines a pattern that specifies a version of a task.
ms.assetid: e9eebbc1-5465-4af6-8b97-f1fd5827442e
keywords:
- versionType simple type Task Scheduler
topic_type:
- apiref
api_name:
- versionType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# versionType Simple Type

Defines a pattern that specifies a version of a task.

``` syntax
<xs:simpleType name="versionType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="\d+(\.\d+){1,3}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **versionType** simple type is a **string** that is restricted by the following pattern:

-   `\d+(\.\d+){1,3}`

    A double followed by one, two, or three doubles. For example, 1.2, or 1.2.3.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





