---
description: The get\_AvgSyncOffset method retrieves the average of the time in milliseconds between when each frame was due and when it was actually rendered for all frames since streaming started.
ms.assetid: b41741e9-e0b5-4c49-93ef-cb8c0cf2ddeb
title: CBaseVideoRenderer.get_AvgSyncOffset method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.get_AvgSyncOffset
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.get\_AvgSyncOffset method

The `get_AvgSyncOffset` method retrieves the average of the time in milliseconds between when each frame was due and when it was actually rendered for all frames since streaming started.

## Syntax


```C++
HRESULT get_AvgSyncOffset(
   int *piAvg
);
```



## Parameters

<dl> <dt>

*piAvg* 
</dt> <dd>

Pointer to the average of the time as previously described.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_AvgSyncOffset**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-iqualprop-get_avgsyncoffset) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




