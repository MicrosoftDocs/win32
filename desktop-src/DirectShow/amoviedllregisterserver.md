---
Description: Obsolete. Use AMovieDllRegisterServer2 instead.
ms.assetid: d3be5fe0-f993-4a15-a3b8-3d761d51f289
title: AMovieDllRegisterServer function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AMovieDllRegisterServer function

Obsolete. Use [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) instead.

## Syntax


```C++
HRESULT AMovieDllRegisterServer(void);
```



## Parameters

This function has no parameters.

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dllsetup.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**DLL Setup Functions**](dll-setup-functions.md)
</dt> </dl>

 

 




