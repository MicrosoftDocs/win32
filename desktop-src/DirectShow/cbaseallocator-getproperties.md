---
Description: The GetProperties method retrieves the number of buffers that the allocator will create, and the buffer properties. This method implements the IMemAllocatorGetProperties method.
ms.assetid: ccee4d69-52fc-4e3c-b6a4-787914708be4
title: CBaseAllocator.GetProperties method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseAllocator.GetProperties method

The `GetProperties` method retrieves the number of buffers that the allocator will create, and the buffer properties. This method implements the [**IMemAllocator::GetProperties**](/windows/win32/Strmif/nf-strmif-imemallocator-getproperties?branch=master) method.

## Syntax


```C++
HRESULT GetProperties(
   ALLOCATOR_PROPERTIES *pProps
);
```



## Parameters

<dl> <dt>

*pProps* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/strmif/ns-strmif-_allocatorproperties?branch=master) structure that receives the allocator properties.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




