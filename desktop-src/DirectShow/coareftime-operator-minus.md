---
Description: 'This operator subtracts one reference time from another.'
ms.assetid: '5691cd76-0d25-45c0-bb58-6668abe1db01'
title: 'COARefTime.operator- method'
---

# COARefTime.operator- method

This operator subtracts one reference time from another.

## Syntax


```C++
COARefTime operator-(
  [ref] const COARefTime &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **COARefTime** object to subtract.

</dd> </dl>

## Return value

Returns a new **COARefTime** object equal to the difference of the reference times.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




