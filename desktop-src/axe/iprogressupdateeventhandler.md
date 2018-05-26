---
title: IProgressUpdateEventHandler class
description: The IProgressUpdateEventHandler interface enables a solution to receive notification from the AXE engine about the progress of an assessment.
ms.assetid: 5EF11FC4-F206-4388-9A52-58A2844730D4
keywords:
- IProgressUpdateEventHandler class Access Execution Engine
- IProgressUpdateEventHandler class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IProgressUpdateEventHandler
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

# IProgressUpdateEventHandler class

The **IProgressUpdateEventHandler** interface enables a solution to receive notification from the AXE engine about the progress of an assessment.

## When to implement

Solutions that need to display progress information to the user should implement a **IProgressUpdateEventHandler** interface.

**IProgressUpdateEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IProgressUpdateEventHandler** class has these methods.



| Method                                               | Description                                                                                                          |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**OnProgressUpdate**](ievents-onprogressupdate.md) | The AXE Core raises this event to notify the solution of the current progress reported by the assessment.<br/> |



 

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

 

 





