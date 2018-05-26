---
title: Volatile Element
description: Indicates whether the task is automatically disabled every time Windows starts.
ms.assetid: E0298876-2A96-401D-B857-69758AF980E5
keywords:
- Volatile element Task Scheduler
topic_type:
- apiref
api_name:
- Volatile
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volatile Element

Indicates whether the task is automatically disabled every time Windows starts.

``` syntax
<xs:element name="Volatile"
    type="xsd:boolean"
    maxOccurs="1"
    minOccurs="0"
    default="false"
 />
```

The **Volatile** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from | Description                                                                        |
|-------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) |              | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ programming, this idle setting is specified using the [**ITaskSettings3::Volatile**](/windows/win32/Taskschd/nf-taskschd-itasksettings3-get_volatile?branch=master) property.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





