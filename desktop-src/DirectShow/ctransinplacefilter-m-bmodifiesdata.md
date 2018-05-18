---
Description: 'The m\_bModifiesData member variable indicates whether the filter modifies the sample data that is receives. The value is set in the CTransInPlaceFilter constructor, but defaults to TRUE.'
ms.assetid: '8ccdba46-315f-4519-b363-6870d1217f98'
title: 'CTransInPlaceFilter::m\_bModifiesData member'
---

# CTransInPlaceFilter::m\_bModifiesData member

The `m_bModifiesData` member variable indicates whether the filter modifies the sample data that is receives. The value is set in the **CTransInPlaceFilter** constructor, but defaults to **TRUE**.

## Syntax


```C++
bool m_bModifiesData;
```



## Remarks

This variable affects how the filter negotiates the allocator. If the value is **TRUE**, the filter cannot use a read-only allocator for both pin connections.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




