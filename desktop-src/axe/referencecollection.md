---
title: ReferenceCollection class
description: This interface provides containers for IssueReference objects.
ms.assetid: DD776CD3-290D-4B85-8E91-8857C8FA59F4
keywords:
- ReferenceCollection class Access Execution Engine
- ReferenceCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ReferenceCollection
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

# ReferenceCollection class

This interface provides containers for [**IssueReference**](issuereference-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ReferenceCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **ReferenceCollection** class has these methods.



| Method                                                                   | Description                                                                                                             |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**~ReferenceCollection**](referencecollection--referencecollection.md) | Destructor method.<br/>                                                                                           |
| [**AddItem**](referencecollection-additem.md)                           | Creates an [**IssueReference**](issuereference-struct.md) and adds it to the **ReferenceCollection**.<br/>       |
| [**Clear**](referencecollection-clear.md)                               | Deletes all [**IssueReference**](issuereference-struct.md) objects from the **ReferenceCollection**.<br/>        |
| [**DeleteItem**](referencecollection-deleteitem.md)                     | Deletes an [**IssueReference**](issuereference-struct.md) from the **ReferenceCollection**.<br/>                 |
| [**GetCount**](referencecollection-getcount.md)                         | Returns the count of [**IssueReference**](issuereference-struct.md) objects in the **ReferenceCollection**.<br/> |
| [**GetItem**](referencecollection-getitem.md)                           | Returns an [**IssueReference**](issuereference-struct.md) from the **ReferenceCollection**.<br/>                 |



 

## Remarks

A **ReferenceCollection** holds data from an **Activity/References** element.

An **IssueReference** holds data from a **References/IssueReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





