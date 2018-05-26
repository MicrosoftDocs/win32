---
Description: Helper object to pass seek commands upstream.
ms.assetid: 2ca9bae7-a133-4e09-8aa7-1c4601ec5db0
title: CTransformOutputPinm\_pPosition member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformOutputPin::m\_pPosition member

Helper object to pass seek commands upstream.

## Syntax


```C++
IUnknown *m_pPosition;
```



## Remarks

When the pin is first queried for the [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master) or [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) interface, it creates and aggregates a [**CPosPassThru**](cpospassthru.md) helper object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




