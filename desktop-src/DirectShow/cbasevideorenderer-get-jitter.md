---
Description: 'The get\_Jitter method retrieves the standard deviation of time in milliseconds between each frame and the next for all frames since streaming started.'
ms.assetid: '629e725e-7dee-4824-8f79-cd3335f4901b'
title: 'CBaseVideoRenderer.get\_Jitter method'
---

# CBaseVideoRenderer.get\_Jitter method

The `get_Jitter` method retrieves the standard deviation of time in milliseconds between each frame and the next for all frames since streaming started.

## Syntax


```C++
HRESULT get_Jitter(
   int *piJitter
);
```



## Parameters

<dl> <dt>

*piJitter* 
</dt> <dd>

Pointer to the standard deviation of the interframe time, in milliseconds.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_Jitter**](iqualprop-get-jitter.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




