---
Description: This operator overloads the assignment operator to copy a media type.
ms.assetid: 28115548-97a5-426d-97cd-c5e759d8e39e
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
  [ref] const CMediaType &amp;cmtype
);
```



## Parameters

<dl> <dt>

*cmtype* \[ref\]
</dt> <dd>

Reference to a **CMediaType** object.

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

 

 




