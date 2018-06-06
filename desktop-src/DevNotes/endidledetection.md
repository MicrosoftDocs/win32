---
Description: Ends monitoring of inactivity.
ms.assetid: 26e52341-77cd-46cd-8b32-e786dfac870e
title: EndIdleDetection function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions. This function is not exported by name; specify ordinal 4 when calling **GetProcAddress**.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msidle.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetLastInputInfo**](https://www.bing.com/search?q=**GetLastInputInfo**)
</dt> </dl>

 

 




