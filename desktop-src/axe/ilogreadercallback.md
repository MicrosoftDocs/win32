---
title: ILogReaderCallback class
description: Defines the interface invoked by the LogReaderCallback method.
ms.assetid: 93A8505A-42B9-480C-927C-C9970A217926
keywords:
- ILogReaderCallback class Access Execution Engine
- ILogReaderCallback class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ILogReaderCallback
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

# ILogReaderCallback class

Defines the interface invoked by the [**LogReaderCallback**](ilogreadercallback-logreadercallback.md) method.

## When to implement

A **ILogReaderCallback** interface should be implemented by a solution that needs to display or process events logged in the AXE Event Tracing log files.

**ILogReaderCallback** has these types of members:

-   [Methods](#methods)

### Methods

The **ILogReaderCallback** class has these methods.



| Method                                                            | Description                                                                                                          |
|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**LogReaderCallback**](ilogreadercallback-logreadercallback.md) | The AXE Core raises this event to send information for a single log entry to the solution for processing.<br/> |



 

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

 

 





