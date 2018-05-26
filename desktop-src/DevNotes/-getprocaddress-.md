---
Description: Gets the address of a function from a DLL.
ms.assetid: e425948c-5588-4a4f-994c-4e608af18439
title: '\_GetProcAddress\_ function'
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# \_GetProcAddress\_ function

\[This function is a wrapper over the **GetProcAddress** function. This function may be altered or unavailable in the future. Applications should call **GetProcAddress** directly.\]

Gets the address of a function from a DLL. See [**GetProcAddress**](base.getprocaddress).

## Syntax


```C++
FARPROC _GetProcAddress_(
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

[**GetProcAddress**](base.getprocaddress)
</dt> </dl>

 

 




