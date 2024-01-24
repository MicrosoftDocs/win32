---
title: DeleteExpiredTaskAfter (settingsType) Element
description: Specifies the amount of time that the Task Scheduler will wait before deleting the task after it expires.
ms.assetid: 947a2fec-ceda-4726-aa1a-26fd1b258c1f
keywords:
- DeleteExpiredTaskAfter element Task Scheduler
topic_type:
- apiref
api_name:
- DeleteExpiredTaskAfter
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DeleteExpiredTaskAfter (settingsType) Element

Specifies the amount of time that the Task Scheduler will wait before deleting the task after it expires. If no value is specified for this element, then the Task Scheduler service will not delete the task. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="DeleteExpiredTaskAfter"
    type="duration"
    minOccurs="0"
    default="PT0S"
 />
```

The **DeleteExpiredTaskAfter** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**DeleteExpiredTaskAfter Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_deleteexpiredtaskafter).

For script development, see [**TaskSettings.DeleteExpiredTaskAfter**](tasksettings-deleteexpiredtaskafter.md).

## Examples

The following XML defines a settings element that deletes an expired task after one week.


```XML
<Settings>
    <DeleteExpiredTaskAfter>PT7D</DeleteExpiredTaskAfter>
</Settings>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





