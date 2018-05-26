---
Description: The UsingDifferentAllocators method determines whether the input and output pins are using different allocators.
ms.assetid: 75feaa6e-6395-4d47-ae92-10a857f8764b
title: CTransInPlaceFilter.UsingDifferentAllocators method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransInPlaceFilter.UsingDifferentAllocators method

The `UsingDifferentAllocators` method determines whether the input and output pins are using different allocators.

## Syntax


```C++
BOOL UsingDifferentAllocators() const;
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the input and output pins are using different allocators, or **FALSE** otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




