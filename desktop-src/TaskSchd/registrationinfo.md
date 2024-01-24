---
title: RegistrationInfo object
description: Scripting object that provides the administrative information that can be used to describe the task.
ms.assetid: '3d5a5545-5adc-4361-9ce8-fffd35ff6df7'
keywords:
- registration information Task Scheduler , object
- RegistrationInfo object Task Scheduler
- RegistrationInfo object Task Scheduler , described
topic_type:
- apiref
api_name:
- RegistrationInfo
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegistrationInfo object

Scripting object that provides the administrative information that can be used to describe the task. This information includes details such as a description of the task, the author of the task, the date the task is registered, and the security descriptor of the task.

## Members

The **RegistrationInfo** object has these types of members:

-   [Properties](#properties)

### Properties

The **RegistrationInfo** object has these properties.



| Property                                                                     | Access type           | Description                                                                                                                                |
|:-----------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Author**](registrationinfo-author.md)<br/>                         | Read/write<br/> | Gets or sets the author of the task.<br/>                                                                                            |
| [**Date**](registrationinfo-date.md)<br/>                             | Read/write<br/> | Gets or sets the date and time when the task is registered.<br/>                                                                     |
| [**Description**](registrationinfo-description.md)<br/>               | Read/write<br/> | Gets or sets the description of the task.<br/>                                                                                       |
| [**Documentation**](registrationinfo-documentation.md)<br/>           | Read/write<br/> | Gets or sets any additional documentation for the task.<br/>                                                                         |
| [**SecurityDescriptor**](registrationinfo-securitydescriptor.md)<br/> |                       | Gets or sets the security descriptor of the task.<br/>                                                                               |
| [**Source**](registrationinfo-source.md)<br/>                         | Read/write<br/> | Gets or sets where the task originated from. For example, a task may originate from a component, service, application, or user.<br/> |
| [**URI**](registrationinfo-uri.md)<br/>                               | Read/write<br/> | Gets or sets the URI of the task.<br/>                                                                                               |
| [**Version**](registrationinfo-version.md)<br/>                       | Read/write<br/> | Gets or sets the version number of the task.<br/>                                                                                    |
| [**XmlText**](registrationinfo-xmltext.md)<br/>                       | Read/write<br/> | Gets or sets an XML-formatted version of the registration information for the task.<br/>                                             |



 

## Remarks

Registration information can be used to identify a task through the Task Scheduler UI, or as search criteria when enumerating over the registered tasks.

When reading or writing XML for a task, registration information for the task is specified in the [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





