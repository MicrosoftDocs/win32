---
Description: Frees Java class loaders that may have been consumed while browsing the applets.
ms.assetid: f6d5e8b9-4c0b-4533-8bf7-070b8c2e6681
title: NotifyBrowserShutdown function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NotifyBrowserShutdown
api_type: 
- DllExport
api_location: 
- Msjava.dll
---

# NotifyBrowserShutdown function

Frees Java class loaders that may have been consumed while browsing the applets.

## Syntax


```C++
HRESULT WINAPI NotifyBrowserShutdown(
   LPVOID lpvReserved
);
```



## Parameters

<dl> <dt>

*lpvReserved* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

## Remarks

When the count of browser windows reaches zero in integrated Web mode, this function frees the Java class loaders. When the user starts browsing applets again, the Java VM will download the latest class files.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjava.dll</dt> </dl> |



 

 




