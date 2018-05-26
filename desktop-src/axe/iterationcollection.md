---
title: IterationCollection class
description: This interface provides containers for Iteration objects.
ms.assetid: EF81C4E7-964D-4875-979F-7C87C549CBF1
keywords:
- IterationCollection class Access Execution Engine
- IterationCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IterationCollection
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

# IterationCollection class

This interface provides containers for [**Iteration**](iteration-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**IterationCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **IterationCollection** class has these methods.



| Method                                                                   | Description                                                                                      |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**~IterationCollection**](iterationcollection--iterationcollection.md) | Destructor method.<br/>                                                                    |
| [**AddItem**](iterationcollection-additem.md)                           | Creates an [**Iteration**](iteration-struct.md) and adds it to the collection.<br/>       |
| [**Clear**](iterationcollection-clear.md)                               | Deletes all [**Iteration**](iteration-struct.md) objects from the collection.<br/>        |
| [**DeleteItem**](iterationcollection-deleteitem.md)                     | Deletes an [**Iteration**](iteration-struct.md) object from the collection.<br/>          |
| [**GetCount**](iterationcollection-getcount.md)                         | Returns the count of [**Iteration**](iteration-struct.md) objects in the collection.<br/> |
| [**GetItem**](iterationcollection-getitem.md)                           | Returns an [**Iteration**](iteration-struct.md) object from the collection.<br/>          |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





