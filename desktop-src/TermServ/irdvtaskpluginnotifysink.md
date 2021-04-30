---
title: IRDVTaskPluginNotifySink interface
description: The IRDVTaskPluginNotifySink interface is used by the task agent to communicate with the trigger agent.
ms.assetid: ccf19693-d3cc-4cf7-af35-947be047beeb
ms.tgt_platform: multiple
keywords:
- IRDVTaskPluginNotifySink interface Remote Desktop Services
- IRDVTaskPluginNotifySink interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IRDVTaskPluginNotifySink
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPluginNotifySink interface

The **IRDVTaskPluginNotifySink** interface is used by the task agent to communicate with the trigger agent. A pointer to this interface is passed to the task agent in the [**IRDVTaskPlugin::Initialize**](irdvtaskplugin-initialize.md) method.

## Members

The **IRDVTaskPluginNotifySink** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IRDVTaskPluginNotifySink** also has these types of members:

-   [Methods](#methods)

### Methods

The **IRDVTaskPluginNotifySink** interface has these methods.



| Method                                                                  | Description                                                                       |
|:------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**DeleteSchedule**](irdvtaskpluginnotifysink-deleteschedule.md)       | Called by the task agent to delete a scheduled task.<br/>                   |
| [**OnTaskStateChange**](irdvtaskpluginnotifysink-ontaskstatechange.md) | Used to notify the trigger agent that the state of a task has changed.<br/> |
| [**OnTerminated**](irdvtaskpluginnotifysink-onterminated.md)           | Called by the task agent to request that the task agent be shut down.<br/>  |
| [**ScheduleTask**](irdvtaskpluginnotifysink-scheduletask.md)           | Called by the task agent to schedule a task.<br/>                           |



 

## Remarks

Although this interface is supported on the operating systems identified in the Requirements below, it will only be used if the virtual machine is hosted on Windows Server 2012.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



 

