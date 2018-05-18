---
Description: 'The GetFreeCount method retrieves the number of media samples that are not in use.'
ms.assetid: 'f4ce4cca-0168-42db-9fe7-858862f033a8'
title: 'CBaseAllocator.GetFreeCount method'
---

# CBaseAllocator.GetFreeCount method

The `GetFreeCount` method retrieves the number of media samples that are not in use.

## Syntax


```C++
HRESULT GetFreeCount(
   LONG *plBuffersFree
);
```



## Parameters

<dl> <dt>

*plBuffersFree* 
</dt> <dd>

Address of a variable that receives the number of samples that are not in use.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method implements the [**IMemAllocatorCallbackTemp::GetFreeCount**](imemallocatorcallbacktemp-getfreecount.md) method. The allocator does not expose the IMemAllocatorCallbackTemp interface unless the *fEnableReleaseCallback* flag is set to **TRUE** in the CBaseAllocator constructor.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




