---
title: TaskVariables object
description: Scripting object that defines task variables that can be passed as parameters to task handlers and external executables that are launched by tasks.
ms.assetid: '194babe0-16bd-4a78-af45-139c9c7eacbe'
keywords:
- TaskVariables object Task Scheduler
- TaskVariables object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskVariables
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskVariables object

Scripting object that defines task variables that can be passed as parameters to task handlers and external executables that are launched by tasks.

## Members

The **TaskVariables** object has these types of members:

-   [Methods](#methods)

### Methods

The **TaskVariables** object has these methods.



| Method                                         | Description                                                                                               |
|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**GetContext**](taskvariables-getcontext.md) | Used to share the context between different steps and tasks that are in the same job instance.<br/> |
| [**GetInput**](taskvariables-getinput.md)     | Gets the input variables for a task.<br/>                                                           |
| [**SetOutput**](taskvariables-setoutput.md)   | Sets the output variables for a task.<br/>                                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





