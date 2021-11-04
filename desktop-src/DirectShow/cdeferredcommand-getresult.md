---
description: The GetResult method retrieves the resulting argument list, if one exists.
ms.assetid: a2a8b17c-3dcf-4f59-89c3-f42070d2a8eb
title: CDeferredCommand.GetResult method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.GetResult
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDeferredCommand.GetResult method

The `GetResult` method retrieves the resulting argument list, if one exists.

## Syntax


```C++
VARIANT* GetResult();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to a **VARIANT** containing the method's argument list, if it exists.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




