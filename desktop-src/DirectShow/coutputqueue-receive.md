---
Description: The Receive method delivers a media sample to the input pin.
ms.assetid: a8ee0988-8955-48d0-be1b-24eea72d560d
title: COutputQueue.Receive method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COutputQueue.Receive method

The `Receive` method delivers a media sample to the input pin.

## Syntax


```C++
HRESULT Receive(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | End-of-stream notification received before processing this sample.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                                           |



 

## Remarks

This method calls the [**COutputQueue::ReceiveMultiple**](coutputqueue-receivemultiple.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




