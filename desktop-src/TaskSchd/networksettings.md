---
title: NetworkSettings object
description: For scripting, provides the settings that the Task Scheduler service uses to obtain a network profile.
ms.assetid: '86ac26c3-c868-4886-8f0b-3a6f6efe3e9d'
keywords:
- NetworkSettings object Task Scheduler
- NetworkSettings object Task Scheduler , described
topic_type:
- apiref
api_name:
- NetworkSettings
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# NetworkSettings object

For scripting, provides the settings that the Task Scheduler service uses to obtain a network profile.

## Members

The **NetworkSettings** object has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkSettings** object has these properties.



| Property                                        | Access type           | Description                                                                                    |
|:------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------|
| [**Id**](networksettings-id.md)<br/>     | Read/write<br/> | Gets or sets a GUID value that identifies a network profile.<br/>                        |
| [**Name**](networksettings-name.md)<br/> | Read/write<br/> | Gets or sets the name of a network profile. The name is used for display purposes. <br/> |



 

## Remarks

When reading or writing your own XML for a task, network settings are specified using the [**NetworkSettings**](taskschedulerschema-networksettings-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





