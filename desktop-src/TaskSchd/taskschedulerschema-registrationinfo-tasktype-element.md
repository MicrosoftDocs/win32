---
title: RegistrationInfo (taskType) Element
description: Specifies administrative information about the task, such as the author of the task and the date the task is registered.
ms.assetid: f3961bad-e9a3-4626-87ed-9639d912717d
keywords:
- registration information Task Scheduler , XML element
- RegistrationInfo element Task Scheduler
topic_type:
- apiref
api_name:
- RegistrationInfo
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RegistrationInfo (taskType) Element

Specifies administrative information about the task, such as the author of the task and the date the task is registered.

``` syntax
<xs:element name="RegistrationInfo"
    type="registrationInfoType"
    minOccurs="0"
 />
```

The **RegistrationInfo** element is defined by the [**taskType**](taskschedulerschema-tasktype-complextype.md) complex type.

## Parent element



| Element                                          | Derived from                                                 | Description                                                                  |
|--------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------|
| [**Task**](taskschedulerschema-task-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Defines the task that is performed by the Task Scheduler service.<br/> |



## Child elements



| Element                                                                                                                  | Type     | Description                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------|
| [**Author (registrationInfoType)**](taskschedulerschema-author-registrationinfotype-element.md)                         | string   | Specifies the author of the task.<br/>                                                                              |
| [**Date (registrationInfoType)**](taskschedulerschema-date-registrationinfotype-element.md)                             | dateTime | Specifies the date and time when the task is registered.<br/>                                                       |
| [**Description (registrationInfoType)**](taskschedulerschema-description-registrationinfotype-element.md)               | string   | Specifies the description of the task.<br/>                                                                         |
| [**Documentation (registrationInfoType)**](taskschedulerschema-documentation-registrationinfotype-element.md)           | string   | Specifies any additional documentation for the task.<br/>                                                           |
| [**SecurityDescriptor (registrationInfoType)**](taskschedulerschema-securitydescriptor-registrationinfotype-element.md) | string   | Specifies the security descriptor of the task.<br/>                                                                 |
| [**Source (registrationInfoType)**](taskschedulerschema-source-registrationinfotype-element.md)                         | string   | Specifies where the task originated from. For example, from a component, a service, an application, or a user.<br/> |
| [**URI (registrationInfoType)**](taskschedulerschema-uri-registrationinfotype-element.md)                               | anyURI   | Specifies the URI of the task.<br/>                                                                                 |
| [**Version (registrationInfoType)**](taskschedulerschema-version-registrationinfotype-element.md)                       | string   | Specifies the version number of the task.<br/>                                                                      |



## Remarks

For scripting development, the registration information of a task is specified using the [**TaskDefinition.RegistrationInfo**](taskdefinition-registrationinfo.md) property.

For C++ development, the registration information of a task is specified using the [**RegistrationInfo property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_registrationinfo).

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

 

 





