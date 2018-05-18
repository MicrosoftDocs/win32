---
Description: 'The get\_FramesDroppedInRenderer method retrieves the number of frames dropped by the renderer.'
ms.assetid: 'd890f285-b3bb-426c-80f6-e273cf0cccbb'
title: 'CBaseVideoRenderer.get\_FramesDroppedInRenderer method'
---

# CBaseVideoRenderer.get\_FramesDroppedInRenderer method

The `get_FramesDroppedInRenderer` method retrieves the number of frames dropped by the renderer.

## Syntax


```C++
HRESULT get_FramesDroppedInRenderer(
   int *pcFramesDropped
);
```



## Parameters

<dl> <dt>

*pcFramesDropped* 
</dt> <dd>

Pointer to the number of frames dropped.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_FramesDroppedInRenderer**](iqualprop-get-framesdroppedinrenderer.md) method. This is how the property page retrieves the data from the scheduler. Frames can also be dropped upstream without the renderer even seeing them.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




