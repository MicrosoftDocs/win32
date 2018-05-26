---
Description: This operator tests for inequality between CMediaType objects.
ms.assetid: 9caf4cb9-f049-42e7-abe4-79f8bf0ea542
title: CMediaType.CMediaTypeoperator!= method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaType.CMediaType::operator!= method

This operator tests for inequality between [**CMediaType**](cmediatype.md) objects.

## Syntax


```C++
BOOL CMediaType::operator!=(
  [ref] const CMediaType &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **CMediaType** object to compare.

</dd> </dl>

## Return value

Returns **TRUE** if *rt* is not equal to this object. Otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




