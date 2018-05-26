---
Description: Invokes the method that is called when the specified asynchronous operation reports progress.
ms.assetid: FB60DDC0-7521-4999-8DD8-175556004198
title: IAsyncOperationWithProgressCompletedHandler&lt;TResult,TProgress&gt;Invoke method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAsyncOperationWithProgressCompletedHandler&lt;TResult,TProgress&gt;::Invoke method

Invokes the method that is called when the specified asynchronous operation reports progress.

## Syntax


```C++
HRESULT Invoke(
  [in] IAsyncOperationWithProgress<TResult,TProgress> *asyncInfo
);
```



## Parameters

<dl> <dt>

*asyncInfo* \[in\]
</dt> <dd>

Type: **[**IAsyncOperationWithProgress&lt;TResult,TProgress&gt;**](/windows/win32/Windows.Foundation.Collections/ns-windows-foundation-collections-iasyncoperationwithprogress?branch=master)\***

The asynchronous action that reports completion.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows 8<br/>           |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[**IAsyncOperationWithProgressCompletedHandler&lt;TResult,TProgress&gt;**](/windows/win32/Windows.Foundation.Collections/?branch=master)
</dt> </dl>

 

 




