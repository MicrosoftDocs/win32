---
Description: Gets the address of a function from a DLL.
ms.assetid: e425948c-5588-4a4f-994c-4e608af18439
title: '\_GetProcAddress\_ function'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_GetProcAddress\_ function

\[This function is a wrapper over the **GetProcAddress** function. This function may be altered or unavailable in the future. Applications should call **GetProcAddress** directly.\]

Gets the address of a function from a DLL. See [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx).

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

[**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx)
</dt> </dl>

 

 




