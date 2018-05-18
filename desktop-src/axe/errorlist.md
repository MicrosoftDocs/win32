---
title: ErrorList class
description: Report all errors that have occurred during an operation performed by Axe.
ms.assetid: 'e50f156e-b6c4-463d-9782-6ae608ec3184'
keywords: ["ErrorList class Access Execution Engine", "ErrorList class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- ErrorList
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorList class

Report all errors that have occurred during an operation performed by Axe. C++ solutions access an instance of the **ErrorList** interface.

## When to implement

Never. This is an interface implemented by Axe.

## Inheritance

The **ErrorList** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**ErrorList** has these types of members:

-   [Methods](#methods)

### Methods

The **ErrorList** class has these methods.



| Method                                           | Description                                                                                             |
|:-------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**~ErrorList**](errorlist--errorlist.md)       | Destructor method.<br/>                                                                           |
| [**GetError**](errorlist-geterror.md)           | Retrieve a specific error from the error list. <br/>                                              |
| [**GetErrorCount**](errorlist-geterrorcount.md) | Retrieve the number of errors in the error list that have occurred while processing the job.<br/> |



 

## Remarks

Managed code uses an [**AxeException**](https://msdn.microsoft.com/library/windows/desktop/hh802908) object.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



 

 





