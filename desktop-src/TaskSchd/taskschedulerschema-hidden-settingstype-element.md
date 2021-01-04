---
title: Hidden (settingsType) Element
description: Specifies that the task will not be visible in the UI by default.
ms.assetid: a08c270f-6d4e-4473-9538-c1e1e21b3b10
keywords:
- Hidden element Task Scheduler
topic_type:
- apiref
api_name:
- Hidden
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Hidden (settingsType) Element

Specifies that the task will not be visible in the UI by default. However, administrators can override this setting through the use of a "master switch" that makes all tasks visible in the UI.

``` syntax
<xs:element name="Hidden"
    type="boolean"
    default="false"
    minOccurs="0"
 />
```

The **Hidden** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                    |
|-------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**Hidden Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_hidden).

For script development, see [**TaskSettings.Hidden**](tasksettings-hidden.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





