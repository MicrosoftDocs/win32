---
Description: The Receive method is called when the object receives a media sample from the output pin. The derived class must implement this method.
ms.assetid: ef45388b-b038-4838-b76b-dbbdc5388495
title: CPullPin.Receive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPullPin.Receive method

The `Receive` method is called when the object receives a media sample from the output pin. The derived class must implement this method.

## Syntax


```C++
virtual HRESULT Receive(
   IMediaSample *pSample
) = 0;
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface of the media sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Returning a value other than S\_OK will stop the data-pulling thread.

## Remarks

This method is called whenever a new sample arrives from the output pin. Write this method in the same manner as the [**IMemInputPin::Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) method.

The time stamps on the sample specify the byte offsets, relative to the original start position that was specified in [**CPullPin::Seek**](cpullpin-seek.md) method.

The start position is rounded down to the nearest alignment boundary, and the stop position is rounded up to the nearest alignment boundary. Also, if the stop position exceeds the total duration, the duration is used instead.

All time stamps are given as a byte offset multiplied by 10,000,000, defined as the constant UNITS. Thus, notionally one second is one byte. To find the actual byte offsets, call [**IMediaSample::GetTime**](/windows/win32/Strmif/nf-strmif-imediasample-gettime?branch=master) and divide the results by UNITS.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




