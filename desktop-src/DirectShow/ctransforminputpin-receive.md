---
Description: The Receive method receives the next media sample in the stream. This method implements the IMemInputPinReceive method.
ms.assetid: 65e4f8f5-2aa2-435b-84b4-e65af3f51afc
title: CTransformInputPin.Receive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformInputPin.Receive method

The `Receive` method receives the next media sample in the stream. This method implements the [**IMemInputPin::Receive**](/windows/win32/Strmif/nf-strmif-imeminputpin-receive?branch=master) method.

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

Pointer to the sample's [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                                                |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Pin is currently flushing; sample was rejected.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                        |



 

## Remarks

This method calls the pin's [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method, which checks the pin's streaming state and checks for format changes in the media type. Then it calls the filter's [**CTransformFilter::Receive**](ctransformfilter-receive.md) method, which processes the sample and delivers it downstream.

If the filter needs to access the sample after this method returns, it should hold a reference count by calling the **IUnknown::AddRef** method on the sample. For example, some decoder filters need the current sample in order to decode the next sample.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




