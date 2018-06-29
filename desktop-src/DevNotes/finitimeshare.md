---
Description: Initializes IME Share.
ms.assetid: 7f58564e-d660-4936-b74c-af4eb93e2442
title: FInitIMEShare function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FInitIMEShare
api_type: 
- DllExport
api_location: 
- Imeshare.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

This function should be called before any other IME Share functions are called.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**EndIMEShare**](endimeshare.md)
</dt> </dl>

 

 




