---
description: The IsUsingDefaultSource method determines if the renderer is using the default source window.
ms.assetid: f68d47e7-6602-4321-8e9e-373d354077a1
title: CBaseControlVideo.IsUsingDefaultSource method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.IsUsingDefaultSource
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.IsUsingDefaultSource method

The `IsUsingDefaultSource` method determines if the renderer is using the default source window.

## Syntax


```C++
virtual HRESULT IsUsingDefaultSource() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the renderer is using the default source; otherwise, returns S\_FALSE.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




