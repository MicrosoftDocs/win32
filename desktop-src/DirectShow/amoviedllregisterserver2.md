---
description: The AMovieDllRegisterServer2 function registers and unregisters filters.
ms.assetid: 2122949d-0117-4c68-bfcd-c717b14dc970
title: AMovieDllRegisterServer2 function (Dllsetup.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AMovieDllRegisterServer2
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# AMovieDllRegisterServer2 function

The **AMovieDllRegisterServer2** function registers and unregisters filters.

## Syntax


```C++
HRESULT AMovieDllRegisterServer2(
   BOOL bRegister
);
```



## Parameters

<dl> <dt>

*bRegister* 
</dt> <dd>

**TRUE** indicates register the filter, **FALSE** indicates unregister it.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use this function to set up your filters. For more information, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dllsetup.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**DLL Setup Functions**](dll-setup-functions.md)
</dt> </dl>

 

 




