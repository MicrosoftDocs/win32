---
description: The Register method adds the filter to the registry.
ms.assetid: 934e421a-25a6-40fa-a48b-6d7331f34b78
title: CBaseFilter.Register method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.Register
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.Register method

The `Register` method adds the filter to the registry.

> [!Note]  
> This method is obsolete. New filters should be registered using the [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) function. For more information, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md).

 

## Syntax


```C++
HRESULT Register();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                             | Description                                          |
|-----------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                  |
| <dl> <dt>**S\_FALSE**</dt> </dl> | No registration information is available.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




