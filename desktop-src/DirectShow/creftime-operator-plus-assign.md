---
Description: The += operator adds two reference times.
ms.assetid: 016d3dac-4d7c-490a-83aa-1d88a2080748
title: CRefTime.operator+= method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRefTime.operator+= method

The += operator adds two reference times.

## Syntax


```C++
CRefTime&amp; operator+=(
  [ref] const CRefTime &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a **CRefTime** object.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




