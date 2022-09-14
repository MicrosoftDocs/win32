---
title: DisallowStartOnRemoteAppSession (settingsType) Element
description: Specifies that the task will not be started if triggered to run in a Remote Applications Integrated Locally (RAIL) session.
ms.assetid: 8323d8d9-fb6a-4876-9967-cc2344c77de3
keywords:
- DisallowStartOnRemoteAppSession element Task Scheduler
topic_type:
- apiref
api_name:
- DisallowStartOnRemoteAppSession
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DisallowStartOnRemoteAppSession (settingsType) Element

Specifies that the task will not be started if triggered to run in a Remote Applications Integrated Locally (RAIL) session.

``` syntax
<xs:element name="DisallowStartOnRemoteAppSession"
    type="boolean"
    default="false"
    minOccurs="0"
 />
```

The **DisallowStartOnRemoteAppSession** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

The default setting for this element is False.

For C++ development, this information is accessed through the [**ITaskSettings2::DisallowStartOnRemoteAppSession**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings2-get_disallowstartonremoteappsession) property.

## Examples

The following XML defines a settings element that does not allow the task to start if the task is triggered to run in a RAIL session.


```XML
<Settings>
    <DisallowStartOnRemoteAppSession>true</DisallowStartOnRemoteAppSession>
</Settings>
        
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





