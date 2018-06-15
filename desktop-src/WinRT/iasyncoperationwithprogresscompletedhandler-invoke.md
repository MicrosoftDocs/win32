---
Description: Invokes the method that is called when the specified asynchronous operation reports progress.
ms.assetid: FB60DDC0-7521-4999-8DD8-175556004198
title: IAsyncOperationWithProgressCompletedHandler&lt;TResult,TProgress&gt;::Invoke method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**IAsyncOperationWithProgress&lt;TResult,TProgress&gt;**](https://msdn.microsoft.com/en-us/library/BR205807(v=VS.85).aspx)\***

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

[**IAsyncOperationWithProgressCompletedHandler&lt;TResult,TProgress&gt;**](https://msdn.microsoft.com/en-us/library/BR205808(v=VS.85).aspx)
</dt> </dl>

 

 




