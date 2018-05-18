---
Description: 'The SetNotify method sets or removes a callback on the allocator. The allocator calls the callback method whenever the allocator''s IMemAllocator::ReleaseBuffer method is called.'
ms.assetid: 'ef9a6c66-d392-4130-b4fc-9eb6aecb6cbf'
title: 'CBaseAllocator.SetNotify method'
---

# CBaseAllocator.SetNotify method

\[[**SetNotify**](iamwmbufferpass-setnotify.md) may be altered or unavailable in subsequent versions.\]

The `SetNotify` method sets or removes a callback on the allocator. The allocator calls the callback method whenever the allocator's [**IMemAllocator::ReleaseBuffer**](imemallocator-releasebuffer.md) method is called.

## Syntax


```C++
HRESULT SetNotify(
   IMemAllocatorNotifyCallbackTemp *pNotify
);
```



## Parameters

<dl> <dt>

*pNotify* 
</dt> <dd>

Pointer to the [**IMemAllocatorNotifyCallbackTemp**](imemallocatornotifycallbacktemp.md) interface that will be used for the callback. The caller must implement the interface. Use the value **NULL** to remove the callback.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method implements the [**IMemAllocatorCallbackTemp::SetNotify**](imemallocatorcallbacktemp-setnotify.md) method. The allocator does not expose the [**IMemAllocatorCallbackTemp**](imemallocatorcallbacktemp.md) interface unless the *fEnableReleaseCallback* flag is set to **TRUE** in the [**CBaseAllocator**](cbaseallocator.md) constructor.

This method sets the [**CBaseAllocator::m\_pNotify**](cbaseallocator-m-pnotify.md) member variable equal to *pNotify* and increments the reference count on the interface. If *m\_pNotify* is non-**NULL**, the allocator's **ReleaseBuffer** method calls [**IMemAllocatorNotifyCallbackTemp::NotifyRelease**](imemallocatornotifycallbacktemp-notifyrelease.md). See the Remarks section in that method for information about implementing the callback.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




