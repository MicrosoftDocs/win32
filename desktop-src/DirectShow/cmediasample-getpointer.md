---
Description: 'The GetPointer method retrieves a read/write pointer to the buffer. This method implements the IMediaSample::GetPointer method.'
ms.assetid: 'dd797ad5-6066-4366-a56f-621132f2e6ea'
title: 'CMediaSample.GetPointer method'
---

# CMediaSample.GetPointer method

The `GetPointer` method retrieves a read/write pointer to the buffer. This method implements the [**IMediaSample::GetPointer**](imediasample-getpointer.md) method.

## Syntax


```C++
HRESULT GetPointer(
   BYTE **ppBuffer
);
```



## Parameters

<dl> <dt>

*ppBuffer* 
</dt> <dd>

Address of a variable that receives a pointer to the buffer.

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

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




