---
title: SecurityDescriptor (registrationInfoType) Element
description: Specifies the security descriptor of the task.
ms.assetid: 79821b20-226a-4e7e-8ca1-6c9cf9f1b56e
keywords:
- SecurityDescriptor element Task Scheduler
topic_type:
- apiref
api_name:
- SecurityDescriptor
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SecurityDescriptor (registrationInfoType) Element

Specifies the security descriptor of the task.

``` syntax
<xs:element name="SecurityDescriptor"
    type="string"
 />
```

The **SecurityDescriptor** element is defined by the [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) complex type.

## Parent element



| Element                                                                           | Derived from                                                                         | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |



## Remarks

For scripting development, the security descriptor of a task is specified using the [**RegistrationInfo.SecurityDescriptor**](registrationinfo-securitydescriptor.md) property.

For C++ development, the security descriptor of a task is specified using the [**IRegistrationInfo::SecurityDescriptor**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationinfo-get_securitydescriptor) property.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





