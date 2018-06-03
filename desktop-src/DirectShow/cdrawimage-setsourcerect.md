---
Description: The SetSourceRect method sets the source rectangle.
ms.assetid: 982636fe-73ea-4f13-9f2b-7ae8df839ab1
title: CDrawImage.SetSourceRect method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDrawImage.SetSourceRect method

The `SetSourceRect` method sets the source rectangle.

## Syntax


```C++
void SetSourceRect(
   RECT *pSourceRect
);
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to a **RECT** structure that defines the new source rectangle.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method if the source rectangle changes; for example, in response to an [**IBasicVideo::SetSourcePosition**](/windows/desktop/api/Control/nf-control-ibasicvideo-setsourceposition) call.

Validate the rectangle given in *pSourceRect* before calling this method, to make sure it does not extend beyond the native video size.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




