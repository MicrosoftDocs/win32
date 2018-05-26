---
Description: The DecideBufferSize method sets the output pins buffer requirements.
ms.assetid: 33e41668-b4f6-4142-b22e-2ddfb96332df
title: CTransformFilter.DecideBufferSize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.DecideBufferSize method

The `DecideBufferSize` method sets the output pin's buffer requirements.

## Syntax


```C++
virtual HRESULT DecideBufferSize(
   IMemAllocator        *pAlloc,
   ALLOCATOR_PROPERTIES *ppropInputRequest
) = 0;
```



## Parameters

<dl> <dt>

*pAlloc* 
</dt> <dd>

Pointer to the [**IMemAllocator**](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master) interface on the output pin's allocator.

</dd> <dt>

*ppropInputRequest* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/strmif/ns-strmif-_allocatorproperties?branch=master) structure that contains buffer requirements from the downstream input pin.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

The output pin's [**CTransformOutputPin::DecideBufferSize**](ctransformoutputpin-decidebuffersize.md) method calls this method. The derived class must implement this method. For more information, see [**CBaseOutputPin::DecideBufferSize**](cbaseoutputpin-decidebuffersize.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




