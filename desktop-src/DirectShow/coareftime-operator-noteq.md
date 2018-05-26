---
Description: This operator tests for inequality between two reference times.
ms.assetid: c081fff2-d85e-409a-8902-4b2aa2c1fc78
title: COARefTime.operator!= method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COARefTime.operator!= method

This operator tests for inequality between two reference times.

## Syntax


```C++
BOOL operator!=(
  [ref] const COARefTime &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **COARefTime** object to compare.

</dd> </dl>

## Return value

Returns **TRUE** if the two objects are not equal. Otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




