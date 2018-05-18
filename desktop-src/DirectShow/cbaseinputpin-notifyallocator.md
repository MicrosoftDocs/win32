---
Description: 'The NotifyAllocator method specifies an allocator for the connection. This method implements the IMemInputPin::NotifyAllocator method.'
ms.assetid: '16167bd5-2d33-4329-87ec-6a6c578e0060'
title: 'CBaseInputPin.NotifyAllocator method'
---

# CBaseInputPin.NotifyAllocator method

The `NotifyAllocator` method specifies an allocator for the connection. This method implements the [**IMemInputPin::NotifyAllocator**](imeminputpin-notifyallocator.md) method.

## Syntax


```C++
HRESULT NotifyAllocator(
   IMemAllocator *pAllocator,
   BOOL          bReadOnly
);
```



## Parameters

<dl> <dt>

*pAllocator* 
</dt> <dd>

Pointer to the allocator's [**IMemAllocator**](imemallocator.md) interface.

</dd> <dt>

*bReadOnly* 
</dt> <dd>

Flag that specifies whether samples from this allocator are read-only. If **TRUE**, samples are read-only.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

During the pin connection, the output pin chooses an allocator and calls this method to notify the input pin. The output pin can use the allocator that the input pin proposed in the [**IMemInputPin::GetAllocator**](imeminputpin-getallocator.md) method, or it can provide its own allocator.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




