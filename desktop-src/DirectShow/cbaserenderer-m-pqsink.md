---
Description: Pointer to the object that receives quality-control messages.
ms.assetid: bf4fd84c-9522-4686-9fb1-17a2ce3e5a16
title: CBaseRendererm\_pQSink member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer::m\_pQSink member

Pointer to the object that receives quality-control messages.

## Syntax


```C++
IQualityControl *m_pQSink;
```



## Remarks

The base class does not implement quality control. This member variable defaults to **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




