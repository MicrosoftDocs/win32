---
description: The NotifyAllocator method informs the CDrawImage object whether the allocator for the connection is a CImageAllocator object.
ms.assetid: cc1604e7-f755-4a7a-9294-6fd06bb434d4
title: CDrawImage.NotifyAllocator method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.NotifyAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.NotifyAllocator method

The `NotifyAllocator` method informs the **CDrawImage** object whether the allocator for the connection is a [**CImageAllocator**](cimageallocator.md) object.

## Syntax


```C++
void NotifyAllocator(
   BOOL bUsingImageAllocator
);
```



## Parameters

<dl> <dt>

*bUsingImageAllocator* 
</dt> <dd>

Boolean value that indicates what kind of allocator is being used.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method after the pins agree to an allocator. If the filter knows the allocator is a **CImageAllocator** object, it should call this method with the value **TRUE**. (Typically, the filter will know this only if it owns the allocator in question.) Otherwise, it should call this method with the value **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::DrawImage**](cdrawimage-drawimage.md)
</dt> </dl>

 

 




