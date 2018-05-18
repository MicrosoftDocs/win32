---
title: PrerequisiteCollection class
description: This interface represents a collection of prerequisites for running a job that failed.
ms.assetid: '35894ECB-11CA-4AA0-95FD-3366A4238814'
keywords: ["PrerequisiteCollection class Access Execution Engine", "PrerequisiteCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- PrerequisiteCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# PrerequisiteCollection class

This interface represents a collection of prerequisites for running a job that failed.

## When to implement

Never. This is an interface implemented and exposed by the AXE Engine.

## Inheritance

The **PrerequisiteCollection** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**PrerequisiteCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **PrerequisiteCollection** class has these methods.



| Method                                                                            | Description                                                |
|:----------------------------------------------------------------------------------|:-----------------------------------------------------------|
| [**~PrerequisiteCollection**](prerequisitecollection--prerequisitecollection.md) | Destructor method.<br/>                              |
| [**GetCount**](prerequisitecollection-getcount.md)                               | Returns the number of issues in the collection.<br/> |
| [**GetItem**](prerequisitecollection-getitem.md)                                 | Returns an issue from the collection.<br/>           |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





