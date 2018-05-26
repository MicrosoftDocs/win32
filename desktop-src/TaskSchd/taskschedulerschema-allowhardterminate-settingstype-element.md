---
title: AllowHardTerminate (settingsType) Element
description: Specifies that the task may be terminated using TerminateProcess.
ms.assetid: 093a3cc6-d3e1-48e3-bc9e-0b15df2a54de
keywords:
- AllowHardTerminate (settingsType) element Task Scheduler
- AllowHardTerminate element Task Scheduler
topic_type:
- apiref
api_name:
- AllowHardTerminate
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AllowHardTerminate (settingsType) Element

Specifies that the task may be terminated using TerminateProcess.

``` syntax
<xs:element name="AllowHardTerminate"
    type="boolean"
    default="true"
    minOccurs="0"
 />
```

The **AllowHardTerminate** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                 | Description                                                                        |
|-------------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see the [**AllowHardTerminate property of ITaskSettings**](/windows/win32/taskschd/nf-taskschd-itasksettings-get_allowhardterminate?branch=master).

For script development, see [**TaskSettings.AllowHardTerminate**](tasksettings-allowhardterminate.md).

## Examples

For a complete example of the XML for a task that allows hard termination, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





