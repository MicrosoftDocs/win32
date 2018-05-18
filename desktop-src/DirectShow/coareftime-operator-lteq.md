---
Description: 'This operator tests if one reference time is greater than or equal to another.'
ms.assetid: '1182db5b-2d58-4abb-b9ec-f14c3de5a942'
title: 'COARefTime.operator&lt;= method'
---

# COARefTime.operator&lt;= method

This operator tests if one reference time is greater than or equal to another.

## Syntax


```C++
BOOL operator<=(
  [ref] const COARefTime &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **COARefTime** object to compare.

</dd> </dl>

## Return value

Returns **TRUE** if this object is greater than or equal to *rt*. Otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




