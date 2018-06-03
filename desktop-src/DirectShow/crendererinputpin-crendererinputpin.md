---
Description: The CRendererInputPin method is a constructor method.
ms.assetid: 272f864e-d6a8-4a9e-b72f-892147db9970
title: CRendererInputPin.CRendererInputPin constructor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CRendererInputPin.CRendererInputPin constructor

The `CRendererInputPin` method is a constructor method.

## Syntax


```C++
CRendererInputPin(
   CBaseRenderer *pRenderer,
   HRESULT       *phr,
   LPCWSTR       Name
);
```



## Parameters

<dl> <dt>

*pRenderer* 
</dt> <dd>

Pointer to the [**CBaseRenderer**](cbaserenderer.md) object that implements the filter.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value.

</dd> <dt>

*Name* 
</dt> <dd>

Pointer to a wide-character string containing the pin identifier.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




