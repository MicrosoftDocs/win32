---
Description: Terminates IME Share.
ms.assetid: aa33b5ed-fd4a-4829-9b7f-d545a4e7bd02
title: EndIMEShare function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

This function should be called after the last IME Share function is called.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**FInitIMEShare**](finitimeshare.md)
</dt> </dl>

 

 




