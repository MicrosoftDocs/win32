---
Description: The Transform method transforms a sample in place.
ms.assetid: 2268041b-70d4-48a9-9bb8-4ab921cce649
title: CTransInPlaceFilter.Transform method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CTransInPlaceFilter.Transform method

The `Transform` method transforms a sample in place.

## Syntax


```C++
virtual HRESULT Transform(
   IMediaSample *pSample
) = 0;
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                            |
|-----------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Do not deliver this sample.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                    |



 

## Remarks

The derived class must implement this method. Transform the sample data in place. If the filter is using two allocators, it copies the data from the input sample to a new sample, and passes the copy to this method.

If the filter should not deliver this sample (for example, to support quality control), the method should return S\_FALSE.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




