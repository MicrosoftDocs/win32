---
title: Subject class
description: This interface provides access to Subject elements.
ms.assetid: CF68ACB3-969B-4E46-983E-53F31B236891
keywords:
- Subject class Access Execution Engine
- Subject class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Subject
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

# Subject class

This interface provides access to **Subject** elements.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Subject** has these types of members:

-   [Methods](#methods)

### Methods

The **Subject** class has these methods.



| Method                                                   | Description                                                      |
|:---------------------------------------------------------|:-----------------------------------------------------------------|
| [**~Subject**](subject--subject.md)                     | Destructor method.<br/>                                    |
| [**GetClass**](subject-getclass.md)                     | Returns the class name of the **Subject**.<br/>            |
| [**GetClassDisplay**](subject-getclassdisplay.md)       | Returns the class display name of the **Subject**.<br/>    |
| [**GetInstance**](subject-getinstance.md)               | Returns the instance name of the **Subject**.<br/>         |
| [**GetInstanceDisplay**](subject-getinstancedisplay.md) | Returns the instance display name of the **Subject**.<br/> |
| [**SetClass**](subject-setclass.md)                     | Sets the class name of the **Subject**.<br/>               |
| [**SetClassDisplay**](subject-setclassdisplay.md)       | Sets the class display name of the **Subject**.<br/>       |
| [**SetInstance**](subject-setinstance.md)               | Sets the instance name of the **Subject**.<br/>            |
| [**SetInstanceDisplay**](subject-setinstancedisplay.md) | Sets the instance display name of the **Subject**.<br/>    |



 

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





