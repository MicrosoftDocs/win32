---
title: actionBaseType Complex Type
description: Defines the Id attribute for all elements of this type.
ms.assetid: adc7117f-881f-4a32-8578-0530f2a0c179
keywords:
- actionBaseType complex type Task Scheduler
topic_type:
- apiref
api_name:
- actionBaseType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# actionBaseType Complex Type

Defines the Id attribute for all elements of this type.

``` syntax
<xs:complexType name="actionBaseType"
    abstract="true"
>
    <xs:attribute name="id"
        type="ID"
        use="optional"
     />
</xs:complexType>
```

## Attributes



| Name | Type | Description                                        |
|------|------|----------------------------------------------------|
| id   | ID   | Id of the action performed by the task.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





