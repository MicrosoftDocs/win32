---
title: ParameterSet class
description: Provides access to a collection of parameters in a given scope.
ms.assetid: 284D30FF-40E1-4FF0-909A-8CA3364ABE9C
keywords:
- ParameterSet class Access Execution Engine
- ParameterSet class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ParameterSet
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

# ParameterSet class

Provides access to a collection of parameters in a given scope.

## When to implement

Never. This is an interface implemented by Axe and provided to the assessment.

**ParameterSet** has these types of members:

-   [Methods](#methods)

### Methods

The **ParameterSet** class has these methods.



| Method                                              | Description                                                              |
|:----------------------------------------------------|:-------------------------------------------------------------------------|
| [**~ParameterSet**](parameterset--parameterset.md) | Destructor method.<br/>                                            |
| [**GetParameter**](parameterset-getparameter.md)   | Returns a parameter object for the specified named parameter.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





