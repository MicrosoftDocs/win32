---
description: The Unregister method removes the filter from the registry.
ms.assetid: 2eb70e9f-1acf-433e-972f-24fb32eaeb13
title: CBaseFilter.Unregister method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.Unregister
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.Unregister method

The `Unregister` method removes the filter from the registry.

> [!Note]  
> This method is obsolete. New filters should be unregistered using the [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) function. For more information, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md).

 

## Syntax


```C++
HRESULT Unregister();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




