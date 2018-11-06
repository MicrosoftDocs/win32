---
Description: Sets the method that is called when the asynchronous action completes.
ms.assetid: 632800E4-D02B-4D45-8A9B-B373AC938558
title: IAsyncAction::put_Completed method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAsyncAction.put_Completed
api_type: 
- COM
api_location: 
- Windows.Foundation.idl
---

# IAsyncAction::put\_Completed method

Sets the method that is called when the asynchronous action completes.

## Syntax


```C++
HRESULT put_Completed(
  [out] AsyncActionCompletedHandler *handler
);
```



## Parameters

<dl> <dt>

*handler* \[out\]
</dt> <dd>

Type: **[**AsyncActionCompletedHandler**](asyncactioncompletedhandler.md)\***

The method that handles the completion notification.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Windows.Foundation.idl</dt> </dl> |



## See also

<dl> <dt>

[**IAsyncAction**](https://msdn.microsoft.com/en-us/library/BR205781(v=VS.85).aspx)
</dt> </dl>

 

 




