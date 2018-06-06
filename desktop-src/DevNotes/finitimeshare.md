---
Description: Initializes IME Share.
ms.assetid: 7f58564e-d660-4936-b74c-af4eb93e2442
title: FInitIMEShare function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FInitIMEShare function

Initializes IME Share.

## Syntax


```C++
BOOL __cdecl FInitIMEShare(void);
```



## Parameters

This function has no parameters.

## Return value

The function returns **TRUE** on success or **FALSE** otherwise.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

This function should be called before any other IME Share functions are called.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**EndIMEShare**](endimeshare.md)
</dt> </dl>

 

 




