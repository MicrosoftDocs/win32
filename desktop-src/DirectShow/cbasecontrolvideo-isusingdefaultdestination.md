---
description: The IsUsingDefaultDestination method determines if the renderer is using the default destination window.
ms.assetid: 0b956575-4cf0-4f1f-9223-bb1ec3ae8b10
title: CBaseControlVideo.IsUsingDefaultDestination method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.IsUsingDefaultDestination
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.IsUsingDefaultDestination method

The `IsUsingDefaultDestination` method determines if the renderer is using the default destination window.

## Syntax


```C++
virtual HRESULT IsUsingDefaultDestination() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if using the default destination; otherwise, returns S\_FALSE.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




