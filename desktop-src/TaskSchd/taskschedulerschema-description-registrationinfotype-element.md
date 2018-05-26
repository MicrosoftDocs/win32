---
title: Description (registrationInfoType) Element
description: Specifies the description of the task.
ms.assetid: bf3552eb-01a6-4651-ae43-4b4e8eef3faf
keywords:
- Description element Task Scheduler
topic_type:
- apiref
api_name:
- Description
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Description (registrationInfoType) Element

Specifies the description of the task.

``` syntax
<xs:element name="Description"
    type="string"
    minOccurs="0"
 />
```

The **Description** element is defined by the [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) complex type.

## Parent element



| Element                                                                           | Derived from                                                                         | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |



## Remarks

For scripting development, the description of a task is specified using the [**RegistrationInfo.Description**](registrationinfo-description.md) property.

For C++ development, the description of a task is specified using the [**IRegistrationInfo::Description**](/windows/win32/taskschd/nf-taskschd-iregistrationinfo-get_description?branch=master) property.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





