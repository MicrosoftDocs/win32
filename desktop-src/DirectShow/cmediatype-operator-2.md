---
Description: This operator overloads the assignment operator to copy a media type.
ms.assetid: 5b94191d-b5e4-42b2-b0c5-8c2da2483c54
title: CMediaType.CMediaTypeoperator= method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaType.CMediaType::operator= method

This operator overloads the assignment operator to copy a media type.

## Syntax


```C++
CMediaType&amp; CMediaType::operator=(
  [ref] const AM_MEDIA_TYPE &amp;mtype
);
```



## Parameters

<dl> <dt>

*mtype* \[ref\]
</dt> <dd>

Reference to an [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




