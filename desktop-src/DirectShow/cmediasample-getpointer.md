---
Description: The GetPointer method retrieves a read/write pointer to the buffer. This method implements the IMediaSampleGetPointer method.
ms.assetid: dd797ad5-6066-4366-a56f-621132f2e6ea
title: CMediaSample.GetPointer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaSample.GetPointer method

The `GetPointer` method retrieves a read/write pointer to the buffer. This method implements the [**IMediaSample::GetPointer**](/windows/win32/Strmif/nf-strmif-imediasample-getpointer?branch=master) method.

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

 

 




