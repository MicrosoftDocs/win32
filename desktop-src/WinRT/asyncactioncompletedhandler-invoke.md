---
description: Invokes the method that is called when the specified asynchronous action completes.
ms.assetid: 97199C1A-7CE3-4BBD-86A3-2CA9B27CC05E
title: AsyncActionCompletedHandler::Invoke method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AsyncActionCompletedHandler.Invoke
api_type: 
- COM
api_location: 
- Windows.Foundation.idl
---

# AsyncActionCompletedHandler::Invoke method

Invokes the method that is called when the specified asynchronous action completes.

## Syntax


```C++
HRESULT Invoke(
  [in] IAsyncAction *asyncInfo
);
```



## Parameters

<dl> <dt>

*asyncInfo* \[in\]
</dt> <dd>

Type: **[**IAsyncAction**](/windows/win32/api/windows.foundation/nn-windows-foundation-iasyncaction)\***

The asynchronous action that reports completion.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Windows.Foundation.idl</dt> </dl> |



## See also

<dl> <dt>

[**AsyncActionCompletedHandler**](asyncactioncompletedhandler.md)
</dt> </dl>

 

