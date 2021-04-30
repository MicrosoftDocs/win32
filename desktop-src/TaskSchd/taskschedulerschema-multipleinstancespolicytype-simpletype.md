---
title: multipleInstancesPolicyType Simple Type
description: Defines the instance policy constants for the MultipleInstancesPolicy (settingsType) element.
ms.assetid: 6e3f83b0-b71e-49c9-9c27-5a37f996746b
keywords:
- multipleInstancesPolicyType simple type Task Scheduler
topic_type:
- apiref
api_name:
- multipleInstancesPolicyType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# multipleInstancesPolicyType Simple Type

Defines the instance policy constants for the [**MultipleInstancesPolicy (settingsType)**](taskschedulerschema-multipleinstancespolicy-settingstype-element.md) element.

``` syntax
<xs:simpleType name="multipleInstancesPolicyType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="Parallel"
         />
        <xs:enumeration
            value="Queue"
         />
        <xs:enumeration
            value="IgnoreNew"
         />
        <xs:enumeration
            value="StopExisting"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **multipleInstancesPolicyType** simple type defines the following values.



| Value        | Description                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------|
| Parallel     | Starts new instance while an existing instance is running.<br/>                           |
| Queue        | Starts new instance of task after all other instances of the task are complete.<br/>      |
| IgnoreNew    | Default. Does not start new instance if an existing instance of the task is running.<br/> |
| StopExisting | Stops an existing instance of the task before it starts new instance.<br/>                |



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

 

 





