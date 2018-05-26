---
Description: The GetVideoSize method retrieves the native videos width and height.
ms.assetid: b3461a56-705b-465a-9cfc-e86fd52a07c5
title: CBaseControlVideo.GetVideoSize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlVideo.GetVideoSize method

The `GetVideoSize` method retrieves the native video's width and height.

## Syntax


```C++
HRESULT GetVideoSize(
   long *pWidth,
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pWidth* 
</dt> <dd>

Pointer to the video width.

</dd> <dt>

*pHeight* 
</dt> <dd>

Pointer to the video height.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




