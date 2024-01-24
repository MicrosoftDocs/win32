---
title: Date (registrationInfoType) Element
description: Specifies the date and time when the task is registered.
ms.assetid: 0b226786-152d-4231-afa6-db5a630525f3
keywords:
- Date element Task Scheduler
topic_type:
- apiref
api_name:
- Date
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Date (registrationInfoType) Element

Specifies the date and time when the task is registered.

``` syntax
<xs:element name="Date"
    type="dateTime"
    minOccurs="0"
 />
```

The **Date** element is defined by the [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) complex type.

## Parent element



| Element                                                                           | Derived from                                                                         | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |



## Remarks

For scripting development, the registration date of a task is specified using the [**RegistrationInfo.Date**](registrationinfo-date.md) property.

For C++ development, the registration date of a task is specified using the [**IRegistrationInfo::Date**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationinfo-get_date) property.

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

 

 





