---
title: Author (registrationInfoType) Element
description: Specifies the author of the task.
ms.assetid: 1faa4952-0737-4313-afa5-4a9bad5daaff
keywords:
- Author element Task Scheduler
topic_type:
- apiref
api_name:
- Author
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Author (registrationInfoType) Element

Specifies the author of the task.

``` syntax
<xs:element name="Author"
    type="string"
    minOccurs="0"
 />
```

The **Author** element is defined by the [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) complex type.

## Parent element



| Element                                                                           | Derived from                                                                         | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |



## Remarks

For scripting development, the author of the task is specified using the [**RegistrationInfo.Author**](registrationinfo-author.md) property.

For C++ development, the author of the task is specified using the [**IRegistrationInfo::Author**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationinfo-get_author) property.

## Examples

The following XML defines the author of a task.


```XML
<RegistrationInfo>
    <Author></Author>
 </RegistrationInfo>
```



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

 

 





