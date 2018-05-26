---
Description: Constructor method.
ms.assetid: c0eff80f-04d3-4919-bb27-1b76c1bd1cce
title: CBaseStreamControl.CBaseStreamControl constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseStreamControl.CBaseStreamControl constructor

Constructor method.

## Syntax


```C++
CBaseStreamControl(
   HRESULT *phr
);
```



## Parameters

<dl> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. If the constructor fails, this parameter receives an error code. If this occurs, the object is not in a valid state.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




