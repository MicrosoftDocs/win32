---
Description: This operator assigns a new reference time.
ms.assetid: e3a005c0-95d5-41e0-80bb-e70399a50dca
title: COARefTime.operator= method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COARefTime.operator= method

This operator assigns a new reference time.

## Syntax


```C++
COARefTime&amp; operator=(
  [ref] const REFERENCE_TIME &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a [**REFERENCE\_TIME**](reference-time.md) value that specifies the new reference time in 100-nanosecond units.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




