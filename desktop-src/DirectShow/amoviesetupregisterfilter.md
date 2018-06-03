---
Description: Obsolete. Use AMovieSetupRegisterFilter2 instead.
ms.assetid: 42278829-d09e-46c7-8f1a-fa4572f7cc00
title: AMovieSetupRegisterFilter function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AMovieSetupRegisterFilter function

Obsolete. Use [**AMovieSetupRegisterFilter2**](amoviesetupregisterfilter2.md) instead.

## Syntax


```C++
HRESULT AMovieSetupRegisterFilter(
   const AMOVIESETUP_FILTER const * psetupdata,
         IFilterMapper              *pIFM,
         BOOL                       bRegister
);
```



## Parameters

<dl> <dt>

*psetupdata* 
</dt> <dd>

Reserved.

</dd> <dt>

*pIFM* 
</dt> <dd>

Reserved.

</dd> <dt>

*bRegister* 
</dt> <dd>

Reserved.

</dd> </dl>

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

 

 




