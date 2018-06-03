---
title: ErrorWarning class
description: This interface provides the ability to create and query error and warning objects.
ms.assetid: 87DE42C6-E829-465E-B595-D527F53ED8AF
keywords:
- ErrorWarning class Access Execution Engine
- ErrorWarning class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ErrorWarning
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

# ErrorWarning class

This interface provides the ability to create and query error and warning objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ErrorWarning** has these types of members:

-   [Methods](#methods)

### Methods

The **ErrorWarning** class has these methods.



| Method                                              | Description                                         |
|:----------------------------------------------------|:----------------------------------------------------|
| [**~ErrorWarning**](errorwarning--errorwarning.md) | Destructor method.<br/>                       |
| [**GetHresult**](errorwarning-gethresult.md)       | Gets the **HRESULT** value of this item.<br/> |
| [**GetKind**](errorwarning-getkind.md)             | Gets the kind of item this is.<br/>           |
| [**GetMessage**](errorwarning-getmessage.md)       | Gets the text message of this item.<br/>      |
| [**SetHresult**](errorwarning-sethresult.md)       | Sets the **HRESULT** value of this item.<br/> |
| [**SetKind**](errorwarning-setkind.md)             | Sets the kind of item for this item.<br/>     |
| [**SetMessage**](errorwarning-setmessage.md)       | Sets the text message of this item.<br/>      |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





