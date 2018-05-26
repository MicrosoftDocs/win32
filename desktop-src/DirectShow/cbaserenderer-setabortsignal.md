---
Description: The SetAbortSignal method sets a flag which indicates whether to stop rendering and reject further samples.
ms.assetid: 2dbf3b4d-e285-4d17-a77c-01a16c09d148
title: CBaseRenderer.SetAbortSignal method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.SetAbortSignal method

The `SetAbortSignal` method sets a flag which indicates whether to stop rendering and reject further samples.

## Syntax


```C++
void SetAbortSignal(
   BOOL bAbort
);
```



## Parameters

<dl> <dt>

*bAbort* 
</dt> <dd>

Boolean value indicating whether to stop rendering. If **TRUE**, the filter will not render any more samples.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method sets the [**CBaseRenderer::m\_bAbort**](cbaserenderer-m-babort.md) flag.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




