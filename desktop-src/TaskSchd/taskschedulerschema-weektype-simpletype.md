---
title: weekType Simple Type
description: Defines the values that can be used in the Week element.
ms.assetid: 83a525ae-020b-4528-9e14-1e7d9df7b8c0
keywords:
- weekType simple type Task Scheduler
topic_type:
- apiref
api_name:
- weekType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# weekType Simple Type

Defines the values that can be used in the [**Week**](taskschedulerschema-week-weekstype-element.md) element.

``` syntax
<xs:simpleType name="weekType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="[1-4]|Last"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **weekType** simple type is a **string** that is restricted by the following pattern:

-   `[1-4]|Last`

    Specifies the first through the fourth week of the month (1-4) or always the last week of the month.

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

 

 





