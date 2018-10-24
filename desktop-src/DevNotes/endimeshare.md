---
Description: Terminates IME Share.
ms.assetid: aa33b5ed-fd4a-4829-9b7f-d545a4e7bd02
title: EndIMEShare function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EndIMEShare
api_type: 
- DllExport
api_location: 
- Imeshare.dll
---

# EndIMEShare function

Terminates IME Share.

## Syntax


```C++
void __cdecl EndIMEShare(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

This function should be called after the last IME Share function is called.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**FInitIMEShare**](finitimeshare.md)
</dt> </dl>

 

 




