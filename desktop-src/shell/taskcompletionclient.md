---
Description: Enables task completion.
ms.assetid: 323343D6-FC4A-4A5F-B065-DD72B6077F99
title: TaskCompletionClient interface
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TaskCompletionClient
api_type: 
- COM
api_location: 
- ExecModelClient.dll
---

# TaskCompletionClient interface

Enables task completion.

## Members

The **TaskCompletionClient** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **TaskCompletionClient** also has these types of members:

-   [Methods](#methods)

### Methods

The **TaskCompletionClient** interface has these methods.



| Method                                                                    | Description                            |
|:--------------------------------------------------------------------------|:---------------------------------------|
| [**ApplyTaskCompletion**](taskcompletionclient-applytaskcompletion.md)   | Begins the task completion.<br/> |
| [**RevokeTaskCompletion**](taskcompletionclient-revoketaskcompletion.md) | Ends the task completion.<br/>   |



 

## Remarks

The GUID for this interface is "E97D552D-9AE9-46AA-9151-D2DA4BBB5E96".

This API is deprecated and may not be available in future versions of Windows. Apps should use the APIs in the [**Windows.ApplicationModel.ExtendedExecution**](https://msdn.microsoft.com/en-us/library/Mt188319(v=WIN.10).aspx) namespace instead.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                           |
| DLL<br/>                      | <dl> <dt>ExecModelClient.dll</dt> </dl> |



 

 




