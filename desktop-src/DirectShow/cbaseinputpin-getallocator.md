---
Description: The GetAllocator method retrieves the memory allocator proposed by this pin. This method implements the IMemInputPinGetAllocator method.
ms.assetid: 07bc77f8-a877-4403-b424-20bda715a818
title: CBaseInputPin.GetAllocator method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseInputPin.GetAllocator method

The `GetAllocator` method retrieves the memory allocator proposed by this pin. This method implements the [**IMemInputPin::GetAllocator**](/windows/win32/Strmif/nf-strmif-imeminputpin-getallocator?branch=master) method.

## Syntax


```C++
HRESULT GetAllocator(
   IMemAllocator **ppAllocator
);
```



## Parameters

<dl> <dt>

*ppAllocator* 
</dt> <dd>

Address of a variable that receives a pointer to the allocator's [**IMemAllocator**](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master) interface.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an error code from the **CoCreateInstance** function.

## Remarks

This method creates a [**CMemAllocator**](cmemallocator.md) object. Override this method if your filter uses an allocator from a downstream pin, or a custom allocator.

If the method succeeds, the **IMemAllocator** interface has an outstanding reference count. Be sure to release it when you are done.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




