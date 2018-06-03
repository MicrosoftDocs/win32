---
title: IJobRestartEventHandler class
description: The IJobRestartEventHandler interface enables a solution to receive notification from the AXE engine when a job is restarting the system.
ms.assetid: 6C47CF87-B6D0-4A27-9790-2FEC471AF546
keywords:
- IJobRestartEventHandler class Access Execution Engine
- IJobRestartEventHandler class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IJobRestartEventHandler
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IJobRestartEventHandler class

The **IJobRestartEventHandler** interface enables a solution to receive notification from the AXE engine when a job is restarting the system.

## When to implement

A **IJobRestartEventHandler** interface should be implemented by a solution that needs to save state information, or perform some cleanup, before restarting the system.

**IJobRestartEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IJobRestartEventHandler** class has these methods.



| Method                                                       | Description                                                                                           |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**OnJobRestart**](ijobrestarteventhandler-onjobrestart.md) | The AXE Core raises this event when a job is ending because the system is being restarted.<br/> |



 

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

 

 





