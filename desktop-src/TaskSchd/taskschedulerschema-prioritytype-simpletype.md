---
title: priorityType Simple Type
description: Defines the minimum and maximum values for the Priority (settingsType) element.
ms.assetid: 44e97d78-f035-4db9-a557-f24960518628
keywords:
- priorityType simple type Task Scheduler
topic_type:
- apiref
api_name:
- priorityType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# priorityType Simple Type

Defines the minimum and maximum values for the [**Priority (settingsType)**](taskschedulerschema-priority-settingstype-element.md) element.

``` syntax
<xs:simpleType name="priorityType">
    <xs:restriction
        base="byte"
    >
        <xs:enumeration
            value="0"
         />
        <xs:enumeration
            value="10"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **priorityType** simple type defines the following values.



| Value | Description                         |
|-------|-------------------------------------|
| 0     | Minimum integer allowed.<br/> |
| 10    | Maximum integer allowed.<br/> |



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

 

 





