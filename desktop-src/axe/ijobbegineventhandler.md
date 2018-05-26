---
title: IJobBeginEventHandler class
description: IJobBeginEventHandler interface enables a solution to receive notification from the AXE engine when a job begins.
ms.assetid: CED8D8A1-256E-4E86-8D17-5AEE22545AA7
keywords:
- IJobBeginEventHandler class Access Execution Engine
- IJobBeginEventHandler class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IJobBeginEventHandler
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

# IJobBeginEventHandler class

The **IJobBeginEventHandler** interface enables a solution to receive notification from the AXE engine when a job begins.

## When to implement

An **IJobBeginEventHandler** interface should be implemented by a solution that needs to display the current status of the job to the user.

**IJobBeginEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IJobBeginEventHandler** class has these methods.



| Method                                   | Description                                                    |
|:-----------------------------------------|:---------------------------------------------------------------|
| [**OnJobBegin**](ievents-onjobbegin.md) | The AXE Core raises this event when the job begins.<br/> |



 

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

 

 





