---
Description: 'The ReleaseBuffer method returns a media sample to the list of free media samples. This method implements the IMemAllocator::ReleaseBuffer method.'
ms.assetid: '35e4e426-044c-4e57-af13-2fddf8501db7'
title: 'CBaseAllocator.ReleaseBuffer method'
---

# CBaseAllocator.ReleaseBuffer method

The `ReleaseBuffer` method returns a media sample to the list of free media samples. This method implements the [**IMemAllocator::ReleaseBuffer**](imemallocator-releasebuffer.md) method.

## Syntax


```C++
HRESULT ReleaseBuffer(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](imediasample.md) interface of the media sample object.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

When a media sample's reference count reaches zero, the sample calls **ReleaseBuffer** with itself as the parameter. This method performs the following actions.

-   Returns the media sample to the free list ([**CBaseAllocator::m\_lFree**](cbaseallocator-m-lfree.md)).
-   Calls the [**CBaseAllocator::NotifySample**](cbaseallocator-notifysample.md) method, which releases any threads that are blocked on calls to the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method.
-   If the [**CBaseAllocator::SetNotify**](cbaseallocator-setnotify.md) method was called previously, calls the **IMemAllocatorNotifyCallbackTemp::NotifyRelease** method.
-   When the last sample is released, if there is a pending [**CBaseAllocator::Decommit**](cbaseallocator-decommit.md) call, calls the [**CBaseAllocator::Free**](cbaseallocator-free.md) method to release the buffer memory. (In the base class, **Free** is a pure virtual method.)

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




