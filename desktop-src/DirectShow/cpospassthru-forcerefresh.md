---
Description: The ForceRefresh method is obsolete.
ms.assetid: 9895f72b-abf8-46a8-aa75-2a30901a4c41
title: CPosPassThru.ForceRefresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.ForceRefresh method

The `ForceRefresh` method is obsolete.

## Syntax


```C++
HRESULT ForceRefresh();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

Originally this class was designed to cache pointers to the connected pin's [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master) and [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) interfaces. The `ForceRefresh` method released those interfaces.

As currently implemented, this class does not cache those interfaces. For compatibility, the `ForceRefresh` method is still included, but it returns S\_OK without doing anything.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




