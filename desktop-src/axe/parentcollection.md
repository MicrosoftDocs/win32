---
title: ParentCollection class
description: This interface provides containers for the parents of a test case.
ms.assetid: 5AE7307E-6350-4718-BECE-F06D39967A63
keywords:
- ParentCollection class Access Execution Engine
- ParentCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ParentCollection
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

# ParentCollection class

This interface provides containers for the parents of a test case.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ParentCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **ParentCollection** class has these methods.



| Method                                                          | Description                                                          |
|:----------------------------------------------------------------|:---------------------------------------------------------------------|
| [**~ParentCollection**](parentcollection--parentcollection.md) | Destructor method.<br/>                                        |
| [**AddItem**](parentcollection-additem.md)                     | Creates a parent and adds it to the **ParentCollection**.<br/> |
| [**Clear**](parentcollection-clear.md)                         | Deletes all parents from the **ParentCollection**.<br/>        |
| [**DeleteItem**](parentcollection-deleteitem.md)               | Deletes a parent from the **ParentCollection**.<br/>           |
| [**GetCount**](parentcollection-getcount.md)                   | Returns the count of parents in the **ParentCollection**.<br/> |
| [**GetItem**](parentcollection-getitem.md)                     | Returns a parent from the **ParentCollection**.<br/>           |



 

## Remarks

A **ParentCollection** holds data from a **TestCase/Parents** element.

A parent is the value of a **Parents/Parent** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





