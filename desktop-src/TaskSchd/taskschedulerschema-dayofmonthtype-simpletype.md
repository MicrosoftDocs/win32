---
title: dayOfMonthType Simple Type
description: Defines the possible values for specifying a day of the month.
ms.assetid: 13497cf4-e1e5-4d54-9dff-0fe89be1fed8
keywords:
- dayOfMonthType simple type Task Scheduler
topic_type:
- apiref
api_name:
- dayOfMonthType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# dayOfMonthType Simple Type

Defines the possible values for specifying a day of the month.

``` syntax
<xs:simpleType name="dayOfMonthType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="[1-9]|[1-2][0-9]|3[0-1]|Last"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **dayOfMonthType** simple type is a **string** that is restricted by the following pattern:

-   `[1-9]|[1-2][0-9]|3[0-1]|Last`

    Specifies the 1st through the 31st day of the month, or always the last day of the month.

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

 

 





