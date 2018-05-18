---
title: ErrorWarningCollection class
description: This interface provides container objects for errors and warnings.
ms.assetid: 'A5E2AF8F-63B3-4580-9984-9AAFF65EF97B'
keywords: ["ErrorWarningCollection class Access Execution Engine", "ErrorWarningCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- ErrorWarningCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarningCollection class

This interface provides container objects for errors and warnings.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ErrorWarningCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **ErrorWarningCollection** class has these methods.



| Method                                                                            | Description                                                                                 |
|:----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**~ErrorWarningCollection**](errorwarningcollection--errorwarningcollection.md) | Destructor method.<br/>                                                               |
| [**AddItem**](errorwarningcollection-additem.md)                                 | Overloaded. Adds an [**ErrorWarning**](errorwarning.md) item to the collection.<br/> |
| [**DeleteItem**](errorwarningcollection-deleteitem.md)                           | Deletes an item from the collection.<br/>                                             |
| [**GetCount**](errorwarningcollection-getcount.md)                               | Provides the count of the items in the collection.<br/>                               |
| [**GetItem**](errorwarningcollection-getitem.md)                                 | Gets an item from the collection.<br/>                                                |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





