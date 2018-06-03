---
Description: Gets the outcome of an asynchronous action.
ms.assetid: E5AF357D-B1EE-4581-AEBC-6F1C89D7DBB0
title: IAsyncAction::GetResults method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAsyncAction::GetResults method

Gets the outcome of an asynchronous action.

## Syntax


```C++
HRESULT GetResults();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

This method always returns **S\_OK**.

## Remarks

Calling the **GetResults** method has no effect if the current implementation has a dynamic type of [**IAsyncAction**](https://www.bing.com/search?q=**IAsyncAction**).

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Windows.Foundation.idl</dt> </dl> |



## See also

<dl> <dt>

[**IAsyncAction**](https://www.bing.com/search?q=**IAsyncAction**)
</dt> </dl>

 

 




