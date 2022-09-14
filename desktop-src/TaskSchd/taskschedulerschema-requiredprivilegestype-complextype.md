---
title: requiredPrivilegesType Complex Type
description: Defines the child elements and sequencing information for the RequiredPrivileges (requiredPrivilegesType) element.
ms.assetid: ae96282a-d167-47ea-9d37-2d682f746d23
keywords:
- requiredPrivilegesType complex type Task Scheduler
topic_type:
- apiref
api_name:
- requiredPrivilegesType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# requiredPrivilegesType Complex Type

Defines the child elements and sequencing information for the [**RequiredPrivileges (requiredPrivilegesType)**](taskschedulerschema-requiredprivileges-requiredprivilegestype-element.md) element.

``` syntax
<xs:complexType name="requiredPrivilegesType">
    <xs:all>
        <xs:element name="Privilege"
            type="privilegeType"
            minOccurs="1"
            maxOccurs="64"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                                           | Type                                                                  | Description                                                |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------|
| [**Privilege**](taskschedulerschema-privilege-requiredprivilegestype-element.md) | [**privilegeType**](taskschedulerschema-privilegetype-simpletype.md) | Specifies the required privileges of the task. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





