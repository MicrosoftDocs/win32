---
Description: The ReceiveMultiple method delivers a batch of media samples to the input pin.
ms.assetid: e9c7d6ed-fbf9-4c90-8e1e-3bad66cb5d4f
title: COutputQueue.ReceiveMultiple method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue.ReceiveMultiple method

The `ReceiveMultiple` method delivers a batch of media samples to the input pin.

## Syntax


```C++
HRESULT ReceiveMultiple(
   IMediaSample **ppSamples,
   long         nSamples,
   long         *nSamplesProcessed
);
```



## Parameters

<dl> <dt>

*ppSamples* 
</dt> <dd>

Address of a pointer to an array of samples.

</dd> <dt>

*nSamples* 
</dt> <dd>

Number of samples in the array.

</dd> <dt>

*nSamplesProcessed* 
</dt> <dd>

Pointer to a variable that receives the number of samples delivered successfully.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | End-of-stream notification received before processing this sample.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                                           |



 

## Remarks

If the object is using a thread, this method queues all of the samples passed in the array. Otherwise, the method calls the [**IMemInputPin::ReceiveMultiple**](/windows/win32/Strmif/nf-strmif-imeminputpin-receivemultiple?branch=master) method on the input pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




