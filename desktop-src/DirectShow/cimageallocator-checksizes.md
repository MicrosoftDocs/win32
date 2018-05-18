---
Description: 'The CheckSizes method checks allocator properties against the current media type.'
ms.assetid: '040b4ed0-c1cc-4995-a0f8-86efa493f84b'
title: 'CImageAllocator.CheckSizes method'
---

# CImageAllocator.CheckSizes method

The `CheckSizes` method checks allocator properties against the current media type.

## Syntax


```C++
HRESULT CheckSizes(
   ALLOCATOR_PROPERTIES *pRequest
);
```



## Parameters

<dl> <dt>

*pRequest* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](allocator-properties.md) structure that describes the requested allocator properties.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                           | Description                                                                 |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | The requested properties are compatible with the media type.<br/>     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | The requested properties are not compatible with the media type.<br/> |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The owning pin is not connected.<br/>                                 |



 

## Remarks

When the method returns, if the return value is S\_OK, the **cbBuffer** member of *pRequest* contains the actual buffer size. This might be larger than the requested size, but will never be smaller.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> </dl>

 

 




