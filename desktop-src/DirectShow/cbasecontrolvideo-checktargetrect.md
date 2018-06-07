---
Description: The CheckTargetRect method determines if a target rectangle is valid.
ms.assetid: a16e7faf-6421-4f78-bbb1-40d38f1a5525
title: CBaseControlVideo.CheckTargetRect method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseControlVideo.CheckTargetRect method

The `CheckTargetRect` method determines if a target rectangle is valid.

## Syntax


```C++
virtual HRESULT CheckTargetRect(
   RECT *pTargetRect
);
```



## Parameters

<dl> <dt>

*pTargetRect* 
</dt> <dd>

Pointer to the target rectangle to check.

</dd> </dl>

## Return value

Returns E\_INVALIDARG if not valid; otherwise, returns NOERROR (S\_OK).

## Remarks

This member function determines if the target rectangle requested is valid. Because the destination rectangle specifies a position in the logical client of the window, the coordinates can be negative, although the overall width and height cannot be zero or a negative value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




