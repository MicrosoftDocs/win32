---
Description: The CheckMediaType method determines if the pin accepts a specific media type. This method overrides the CBasePinCheckMediaType method.
ms.assetid: 618c6f2e-2a15-43dd-811e-898dad0de226
title: CRendererInputPin.CheckMediaType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRendererInputPin.CheckMediaType method

The `CheckMediaType` method determines if the pin accepts a specific media type. This method overrides the [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method.

## Syntax


```C++
HRESULT CheckMediaType(
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to a media type object that contains the proposed media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




