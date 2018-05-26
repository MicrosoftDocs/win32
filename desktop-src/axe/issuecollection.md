---
title: IssueCollection class
description: This interface provides containers for Issue objects.
ms.assetid: 463CBBFC-BDED-423C-A89A-AFBBC92F3DE4
keywords:
- IssueCollection class Access Execution Engine
- IssueCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IssueCollection
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

# IssueCollection class

This interface provides containers for [**Issue**](issue-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**IssueCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **IssueCollection** class has these methods.



| Method                                                       | Description                                                                                       |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**~IssueCollection**](issuecollection--issuecollection.md) | Destructor object.<br/>                                                                     |
| [**AddItem**](issuecollection-additem.md)                   | Creates and adds an [**Issue**](issue-struct.md) to the **IssueCollection**.<br/>          |
| [**Clear**](issuecollection-clear.md)                       | Deletes all [**Issue**](issue-struct.md) objects from the **IssueCollection**.<br/>        |
| [**DeleteItem**](issuecollection-deleteitem.md)             | Deletes an [**Issue**](issue-struct.md) from the **IssueCollection**.<br/>                 |
| [**GetCount**](issuecollection-getcount.md)                 | Returns the count of [**Issue**](issue-struct.md) objects in the **IssueCollection**.<br/> |
| [**GetItem**](issuecollection-getitem.md)                   | Returns an [**Issue**](issue-struct.md) of the **IssueCollection**.<br/>                   |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





