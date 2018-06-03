---
Description: Passes an EC\_VIDEO\_SIZE\_CHANGED message to the filter graph manager.
ms.assetid: 39cb4f30-c12d-49bd-8d8a-70bf686b680d
title: CBaseControlVideo.OnVideoSizeChange method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseControlVideo.OnVideoSizeChange method

Passes an EC\_VIDEO\_SIZE\_CHANGED message to the filter graph manager.

## Syntax


```C++
virtual HRESULT OnVideoSizeChange();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                   | Description               |
|-----------------------------------------------------------------------------------------------|---------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Failure.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/> |



 

## Remarks

A video renderer should call this member function each time the video size is changed; this will typically be called once after initial connection. If the renderer can support dynamic format changes (from 320 x 240 to 160 x 120), it should also call it after each change.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




