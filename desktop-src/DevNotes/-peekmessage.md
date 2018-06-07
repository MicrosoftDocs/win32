---
Description: Dispatches incoming sent messages, checks the thread message queue for a posted message, and retrieves the message (if any exist).
ms.assetid: 6b20f354-413d-4197-8b49-e6f965121865
title: '\_PeekMessage function'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_PeekMessage function

\[This function is a wrapper over the **PeekMessage** function. This function may be altered or unavailable in the future. Applications should call **PeekMessage** directly.\]

Dispatches incoming sent messages, checks the thread message queue for a posted message, and retrieves the message (if any exist). See [**PeekMessage**](https://www.bing.com/search?q=**PeekMessage**).

## Syntax


```C++
BOOL _PeekMessage(
    ...
);
```



## Parameters

<dl> <dt>

*...* 
</dt> <dd></dd> </dl>

## Requirements



|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msmdun80.dll; </dt> <dt>Sqlunirl.dll</dt> </dl> |



## See also

<dl> <dt>

[**PeekMessage**](https://www.bing.com/search?q=**PeekMessage**)
</dt> </dl>

 

 




