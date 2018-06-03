---
Description: Represents the method that is called when an asynchronous action completes.
ms.assetid: B410E7C1-B108-4204-9AD1-663F7E05BBC3
title: AsyncActionCompletedHandler interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AsyncActionCompletedHandler interface

Represents the method that is called when an asynchronous action completes.

## Members

The **AsyncActionCompletedHandler** interface inherits from [**IAsyncInfo**](/windows/desktop/api/AsyncInfo/nn-asyncinfo-iasyncinfo). **AsyncActionCompletedHandler** also has these types of members:

-   [Methods](#methods)

### Methods

The **AsyncActionCompletedHandler** interface has these methods.



| Method                                               | Description                                                                                    |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Invoke**](asyncactioncompletedhandler-invoke.md) | Invokes the method that is called when the specified asynchronous action completes.<br/> |



 

## Remarks

Assign an **AsyncActionCompletedHandler** to an [**IAsyncAction**](https://www.bing.com/search?q=**IAsyncAction**) to receive a notification when the asynchronous action completes.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Windows.Foundation.idl</dt> </dl> |



## See also

<dl> <dt>

[**IAsyncInfo**](/windows/desktop/api/AsyncInfo/nn-asyncinfo-iasyncinfo)
</dt> </dl>

 

 




