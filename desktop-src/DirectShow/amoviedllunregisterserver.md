---
Description: Obsolete. Use AMovieDllRegisterServer2 instead.
ms.assetid: 80f52109-6239-4e3d-a395-eb69f5278cd2
title: AMovieDllUnregisterServer function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AMovieDllUnregisterServer function

Obsolete. Use [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) instead.

## Syntax


```C++
HRESULT AMovieDllUnregisterServer(void);
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

 

 




