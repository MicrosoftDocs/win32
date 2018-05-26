---
Description: The CheckMediaType method determines if the pin accepts a specific media type.
ms.assetid: 6a138679-02b7-4ccc-8881-a0d496f84f93
title: CBasePin.CheckMediaType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.CheckMediaType method

The `CheckMediaType` method determines if the pin accepts a specific media type.

## Syntax


```C++
virtual HRESULT CheckMediaType(
   const CMediaType *pmt
) = 0;
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the proposed media type.

</dd> </dl>

## Return value

Returns S\_OK if the proposed media type is acceptable. Otherwise, returns S\_FALSE or an error code.

## Remarks

The derived class must override this pure virtual method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




