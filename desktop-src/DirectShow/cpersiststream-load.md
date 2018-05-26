---
Description: Loads the filters data from a given stream.
ms.assetid: c2bfd379-2916-4698-bc41-653161723706
title: CPersistStream.Load method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPersistStream.Load method

Loads the filter's data from a given stream.

## Syntax


```C++
HRESULT Load(
   LPSTREAM pStm
);
```



## Parameters

<dl> <dt>

*pStm* 
</dt> <dd>

Pointer to the stream from which to be loaded.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the **IPersistStream::Load** method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




