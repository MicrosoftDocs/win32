---
Description: Retrieves the number of type-information interfaces provided by an object.
ms.assetid: 29575325-8f97-4f39-8272-86a917d9144f
title: CMediaControl.GetTypeInfoCount method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CMediaControl.GetTypeInfoCount method

Retrieves the number of type-information interfaces provided by an object.

## Syntax


```C++
HRESULT GetTypeInfoCount(
   UINT *pctinfo
);
```



## Parameters

<dl> <dt>

*pctinfo* 
</dt> <dd>

Pointer to the number of type-information interfaces that the object provides. If the object provides type information, this number is 1; otherwise, the number is 0.

</dd> </dl>

## Return value

Returns E\_POINTER if *pctinfo* is invalid; otherwise, returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




