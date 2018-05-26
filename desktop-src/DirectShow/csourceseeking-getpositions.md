---
Description: The GetPositions method retrieves the current position and the stop position. This method implements the IMediaSeekingGetPositions method.
ms.assetid: f577b052-669b-457d-beab-94f574fef08d
title: CSourceSeeking.GetPositions method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourceSeeking.GetPositions method

The `GetPositions` method retrieves the current position and the stop position. This method implements the [**IMediaSeeking::GetPositions**](/windows/win32/Strmif/nf-strmif-imediaseeking-getpositions?branch=master) method.

## Syntax


```C++
HRESULT GetPositions(
   LONGLONG *pCurrent,
   LONGLONG *pStop
);
```



## Parameters

<dl> <dt>

*pCurrent* 
</dt> <dd>

Pointer to a variable that receives the start position.

</dd> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that receives the stop position.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

For the *pCurrent* parameter, this method returns the value of the [**CSourceSeeking::m\_rtStart**](csourceseeking-m-rtstart.md) member variable, which represents the latest seek time, not the current streaming position. However, when an application calls **IMediaSeeking::GetPositions** through the filter graph manager, the values typically come from a renderer filter, not a source filter.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




