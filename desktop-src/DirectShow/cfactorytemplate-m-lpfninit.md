---
description: Pointer to a function that gets called from the DLL entry point. Can be NULL.
ms.assetid: 0769f55b-6f0d-4a89-9d3f-64f211426342
title: CFactoryTemplate::m_lpfnInit member (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lpfnInit
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CFactoryTemplate::m\_lpfnInit member

Pointer to a function that gets called from the DLL entry point. Can be **NULL**.

## Syntax


```C++
LPFNInitRoutine m_lpfnInit;
```



## Remarks

The function pointer type is [**LPFNInitRoutine**](lpfninitroutine.md). If you provide this function in your DLL, the DLL entry-point function calls it with following parameters:

-   *bLoading*: **TRUE** when the DLL is loaded, **FALSE** when the DLL is unloaded.
-   *rclsid*: Pointer to the object's CLISD, specified in the [**CFactoryTemplate::m\_ClsID**](cfactorytemplate-m-clsid.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




