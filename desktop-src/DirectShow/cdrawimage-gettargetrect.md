---
Description: The GetTargetRect method retrieves the current destination rectangle.
ms.assetid: b6542b06-af36-4666-b6fa-d9fa3c6c7044
title: CDrawImage.GetTargetRect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDrawImage.GetTargetRect method

The `GetTargetRect` method retrieves the current destination rectangle.

## Syntax


```C++
void GetTargetRect(
   RECT *pTargetRect
);
```



## Parameters

<dl> <dt>

*pTargetRect* 
</dt> <dd>

Pointer to a **RECT** structure that receives the target rectangle.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




