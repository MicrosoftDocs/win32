---
Description: 'This operator tests for equality between two reference times.'
ms.assetid: 'a265f7c6-8334-4bb3-8cb7-c7918ebdf97a'
title: 'COARefTime.operator== method'
---

# COARefTime.operator== method

This operator tests for equality between two reference times.

## Syntax


```C++
BOOL operator==(
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

Returns **TRUE** if the two objects are equal. Otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




