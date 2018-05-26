---
Description: Ends monitoring of inactivity.
ms.assetid: 26e52341-77cd-46cd-8b32-e786dfac870e
title: EndIdleDetection function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EndIdleDetection function

\[This function is not supported and may be altered or unavailable in the future. Instead, use the **GetLastInputInfo** function.\]

Ends monitoring of inactivity.

## Syntax


```C++
BOOL WINAPI EndIdleDetection(
   DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*dwReserved* 
</dt> <dd>

This parameter must be set to zero.

</dd> </dl>

## Return value

Returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions. This function is not exported by name; specify ordinal 4 when calling **GetProcAddress**.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msidle.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetLastInputInfo**](_win32_getlastinputinfo_cpp)
</dt> </dl>

 

 




