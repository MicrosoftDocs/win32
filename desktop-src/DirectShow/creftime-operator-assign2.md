---
Description: 'The = operator assigns a new reference time.'
ms.assetid: '556c2e8a-4726-42ab-949d-9a028ebb1b95'
title: 'CRefTime.operator= method'
---

# CRefTime.operator= method

The = operator assigns a new reference time.

## Syntax


```C++
CRefTime&amp; operator=(
   const LONGLONG ll
);
```



## Parameters

<dl> <dt>

*ll* 
</dt> <dd>

New reference time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




