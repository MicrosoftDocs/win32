---
title: Source (registrationInfoType) Element
description: Specifies where the task originated from. For example, from a component, a service, an application, or a user.
ms.assetid: 174e2aac-7cd0-4c19-9441-2c93a3260c6f
keywords:
- Source element Task Scheduler
topic_type:
- apiref
api_name:
- Source
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Source (registrationInfoType) Element

Specifies where the task originated from. For example, from a component, a service, an application, or a user.

``` syntax
<xs:element name="Source"
    type="string"
    minOccurs="0"
 />
```

The **Source** element is defined by the [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) complex type.

## Parent element



| Element                                                                           | Derived from                                                                         | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |



## Remarks

For scripting development, the source of a task is specified using the [**RegistrationInfo.Source**](registrationinfo-source.md) property.

For C++ development, the source of a task is specified using the [**IRegistrationInfo::Source**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationinfo-get_source) property.

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

 

 





