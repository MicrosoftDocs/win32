---
Description: This operator overloads the assignment operator to copy a media type.
ms.assetid: 28115548-97a5-426d-97cd-c5e759d8e39e
title: CMediaType.CMediaType::operator= method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

 

 




