---
title: UseUnifiedSchedulingEngine (settingsType) Element
description: Specifies that the Unified Scheduling Engine will be used to run this task.
ms.assetid: 93436f14-1caf-4ec8-bf74-a198b7dcb27c
keywords:
- UseUnifiedSchedulingEngine element Task Scheduler
topic_type:
- apiref
api_name:
- UseUnifiedSchedulingEngine
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UseUnifiedSchedulingEngine (settingsType) Element

Specifies that the Unified Scheduling Engine will be used to run this task.

``` syntax
<xs:element name="UseUnifiedSchedulingEngine"
    type="boolean"
    default="false"
    minOccurs="0"
 />
```

The **UseUnifiedSchedulingEngine** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

The default setting for this element is False.

For C++ development, this information is accessed through the [**ITaskSettings2::UseUnifiedSchedulingEngine**](/windows/win32/taskschd/nf-taskschd-itasksettings2-get_useunifiedschedulingengine?branch=master) property.

## Examples

The following XML defines a settings element that specifies that the Unified Scheduling Engine will be used to run this task.


```XML
<Settings>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
</Settings>
        
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





