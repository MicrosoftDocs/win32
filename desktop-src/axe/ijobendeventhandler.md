---
title: IJobEndEventHandler class
description: The IJobEndEventHandler interface enables a solution to receive a notification from the AXE engine when a job has completely finished.
ms.assetid: 072E436F-266C-4E35-84EC-2B4A45DE72D7
keywords:
- IJobEndEventHandler class Access Execution Engine
- IJobEndEventHandler class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IJobEndEventHandler
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IJobEndEventHandler class

The **IJobEndEventHandler** interface enables a solution to receive a notification from the AXE engine when a job has completely finished.

## When to implement

An **IJobEndEventHandler** should be implemented by a solution that wants to display the status of the current job execution to the user.

**IJobEndEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IJobEndEventHandler** class has these methods.



| Method                               | Description                                                       |
|:-------------------------------------|:------------------------------------------------------------------|
| [**OnJobEnd**](ievents-onjobend.md) | The AXE Core raises this event when the job has ended.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





