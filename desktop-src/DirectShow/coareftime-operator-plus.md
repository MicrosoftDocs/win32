---
Description: This operator adds two reference times.
ms.assetid: 4dfc087a-ec4f-4a8a-8bd4-4da9e1699bcd
title: COARefTime.operator+ method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COARefTime.operator+ method

This operator adds two reference times.

## Syntax


```C++
COARefTime operator+(
  [ref] const COARefTime &amp;rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **COARefTime** object to add.

</dd> </dl>

## Return value

Returns a new **COARefTime** object equal to the sum of the reference times.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




