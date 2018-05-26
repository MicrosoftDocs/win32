---
title: CategoryCollection class
description: This interface provides containers for the categories of an Issue.
ms.assetid: 7E91A748-9CB8-44A9-A605-251BC8F93070
keywords:
- CategoryCollection class Access Execution Engine
- CategoryCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- CategoryCollection
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

# CategoryCollection class

This interface provides containers for the categories of an [**Issue**](issue-struct.md).

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**CategoryCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **CategoryCollection** class has these methods.



| Method                                                                | Description                                                               |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**~CategoryCollection**](categorycollection--categorycollection.md) | Destructor method.<br/>                                             |
| [**AddItem**](categorycollection-additem.md)                         | Creates and adds a category to the **CategoryCollection**.<br/>     |
| [**Clear**](categorycollection-clear.md)                             | Deletes all categories from the **CategoryCollection**.<br/>        |
| [**DeleteItem**](categorycollection-deleteitem.md)                   | Deletes a category from the **CategoryCollection**.<br/>            |
| [**GetCount**](categorycollection-getcount.md)                       | Returns the count of categories in the **CategoryCollection**.<br/> |
| [**GetItem**](categorycollection-getitem.md)                         | Resturns a category from the **CategoryCollection**.<br/>           |



 

## Remarks

A **CategoryCollection** object holds data from element **Issue/Categories**.

A category is the value of an **Issue/Categories/Category** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





