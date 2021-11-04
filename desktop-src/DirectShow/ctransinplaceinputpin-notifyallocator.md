---
description: CTransInPlaceInputPin.NotifyAllocator method - The NotifyAllocator method specifies an allocator for the connection. This method implements the IMemInputPin::NotifyAllocator method.
ms.assetid: adc1c5b6-99da-4140-b644-7b98f6b8bad4
title: CTransInPlaceInputPin.NotifyAllocator method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceInputPin.NotifyAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceInputPin.NotifyAllocator method

The `NotifyAllocator` method specifies an allocator for the connection. This method implements the [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) method.

## Syntax


```C++
HRESULT NotifyAllocator(
   IMemAllocator *pAllocator,
   BOOL          bReadOnly
);
```



## Parameters

<dl> <dt>

*pAllocator* 
</dt> <dd>

Pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> <dt>

*bReadOnly* 
</dt> <dd>

Flag that specifies whether samples from this allocator are read-only. If **TRUE**, samples are read-only.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                               | Description                          |
|-------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | Failure<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument<br/> |



 

## Remarks

The filter attempts to use the same allocator for both pin connections.

-   If the output pin is not connected, the input pin automatically accepts the allocator. When the output pin is connected, the filter will reconnect the input pin. At that point, the filter will try again to use a single allocator.
-   If the output pin is connected, the input pin accepts the allocator. The output pin also uses the same allocator. It calls `NotifyAllocator` on the downstream input pin.

The previous case has the following exception:

-   If the proposed allocator is read-only (that is, the *bReadOnly* parameter is **TRUE**) and the filter needs to modify the samples, then the filter must use two different allocators. In this case, if the upstream filter is proposing to use the downstream filter's allocator, the method returns E\_FAIL.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




