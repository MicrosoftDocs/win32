---
description: Represents the method that is called when an asynchronous action completes.
ms.assetid: B410E7C1-B108-4204-9AD1-663F7E05BBC3
title: AsyncActionCompletedHandler interface
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- AsyncActionCompletedHandler
api_type:
- COM
api_location:
- Windows.Foundation.idl
---

# AsyncActionCompletedHandler interface

Represents the method that is called when an asynchronous action completes.

## Members

The **AsyncActionCompletedHandler** interface inherits from [**IAsyncInfo**](/windows/win32/api/asyncinfo/nn-asyncinfo-iasyncinfo). **AsyncActionCompletedHandler** also has these types of members:

-   [Methods](#methods)

### Methods

The **AsyncActionCompletedHandler** interface has these methods.



| Method                                               | Description                                                                                    |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Invoke**](asyncactioncompletedhandler-invoke.md) | Invokes the method that is called when the specified asynchronous action completes.<br/> |



 

## Remarks

Assign an **AsyncActionCompletedHandler** to an [**IAsyncAction**](/windows/win32/api/windows.foundation/nn-windows-foundation-iasyncaction) to receive a notification when the asynchronous action completes.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Windows.Foundation.idl</dt> </dl> |



## See also

<dl> <dt>

[**IAsyncInfo**](/windows/win32/api/asyncinfo/nn-asyncinfo-iasyncinfo)
</dt> </dl>

 

