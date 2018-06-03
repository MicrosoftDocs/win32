---
title: Trace class
description: This interface provides access to Trace objects.
ms.assetid: 20D0DE37-186A-424F-AC36-59C01BAE2F62
keywords:
- Trace class Access Execution Engine
- Trace class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Trace
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

# Trace class

This interface provides access to **Trace** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Trace** has these types of members:

-   [Methods](#methods)

### Methods

The **Trace** class has these methods.



| Method                                 | Description                                        |
|:---------------------------------------|:---------------------------------------------------|
| [**~Trace**](trace--trace.md)         | Destructor method.<br/>                      |
| [**Clear**](trace-clear.md)           | Clears the settings of the **Trace**.<br/>   |
| [**GetFile**](trace-getfile.md)       | Returns the file name of the **Trace**.<br/> |
| [**GetLink**](trace-getlink.md)       | Returns the link of the **Trace**.<br/>      |
| [**GetName**](trace-getname.md)       | Returns the name of the **Trace**.<br/>      |
| [**GetTooltip**](trace-gettooltip.md) | Returns the tooltip of the **Trace**.<br/>   |
| [**SetFile**](trace-setfile.md)       | Sets the file name of the **Trace**.<br/>    |
| [**SetLink**](trace-setlink.md)       | Sets the link of the **Trace**.<br/>         |
| [**SetName**](trace-setname.md)       | Sets the name of the **Trace**.<br/>         |
| [**SetTooltip**](trace-settooltip.md) | Sets the tooltip of the **Trace**.<br/>      |



 

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





