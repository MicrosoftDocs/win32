---
Description: 'The get\_DevSyncOffset method retrieves the standard deviation of the time in milliseconds between when each frame was due and when it was actually rendered, for all frames since streaming started.'
ms.assetid: '86f60064-f913-4377-bad0-148a213171fc'
title: 'CBaseVideoRenderer.get\_DevSyncOffset method'
---

# CBaseVideoRenderer.get\_DevSyncOffset method

The `get_DevSyncOffset` method retrieves the standard deviation of the time in milliseconds between when each frame was due and when it was actually rendered, for all frames since streaming started.

## Syntax


```C++
HRESULT get_DevSyncOffset(
   int *piDev
);
```



## Parameters

<dl> <dt>

*piDev* 
</dt> <dd>

Pointer to the standard deviation of the time as previously described.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_DevSyncOffset**](iqualprop-get-devsyncoffset.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




