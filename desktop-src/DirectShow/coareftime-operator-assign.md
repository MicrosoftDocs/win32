---
Description: This operator assigns a new reference time.
ms.assetid: ae6a33ab-f4e0-4f1c-80a0-8a25ee1e9dc5
title: COARefTime.operator= method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COARefTime.operator= method

This operator assigns a new reference time.

## Syntax


```C++
COARefTime&amp; operator=(
  [ref] const double &amp;rd
);
```



## Parameters

<dl> <dt>

*rd* \[ref\]
</dt> <dd>

Reference to a **double** value that specifies the new reference time in seconds.

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

 

 




