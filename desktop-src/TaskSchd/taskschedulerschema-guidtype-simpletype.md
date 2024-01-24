---
title: guidType simple type (Task Scheduler)
description: Defines the pattern for valid GUIDs.
ms.assetid: 1aa3f08b-4b3e-4e72-8ac4-d859a8da4c32
keywords:
- guidType simple type Task Scheduler
topic_type:
- apiref
api_name:
- guidType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# guidType simple type (Task Scheduler)

Defines the pattern for valid GUIDs.

``` syntax
<xs:simpleType name="guidType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="\{([0-9a-fA-F]){8}(\-[0-9a-fA-F]{4}){3}\-[0-9a-fA-F]{12}\}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **guidType** simple type is a **string** that is restricted by the following pattern:

-   `\{([0-9a-fA-F]){8}(\-[0-9a-fA-F]{4}){3}\-[0-9a-fA-F]{12}\}`

    A unique 128-bit number.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Simple Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





