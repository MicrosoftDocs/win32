---
Description: The RegisterMediaTime method caches the time stamps from the current sample.
ms.assetid: 9ff8e4ec-3401-4272-894d-643f0fc029de
title: CRendererPosPassThru.RegisterMediaTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRendererPosPassThru.RegisterMediaTime method

The **RegisterMediaTime** method caches the time stamps from the current sample.

## Syntax


```C++
HRESULT RegisterMediaTime(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface of the sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                                  | Description                                |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                        |
| <dl> <dt>**VFW\_E\_MEDIA\_TIME\_NOT\_SET**</dt> </dl> | The sample is not time-stamped.<br/> |



 

## Remarks

This method stores the time stamps from the current sample. The [**CRendererPosPassThru::GetMediaTime**](crendererpospassthru-getmediatime.md) method retrieves the same values.

The filter should call this method for each sample that it receives. The method is overloaded to accept either a pointer to the sample, or the time stamp values themselves.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




