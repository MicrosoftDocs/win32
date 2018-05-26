---
Description: The GetCapabilities method retrieves all the seeking capabilities of the stream. This method implements the IMediaSeekingGetCapabilities method.
ms.assetid: c60c4f47-48de-47d0-9b87-589b84df842c
title: CPosPassThru.GetCapabilities method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.GetCapabilities method

The **GetCapabilities** method retrieves all the seeking capabilities of the stream. This method implements the [**IMediaSeeking::GetCapabilities**](/windows/win32/Strmif/nf-strmif-imediaseeking-getcapabilities?branch=master) method.

## Syntax


```C++
HRESULT GetCapabilities(
   DWORD *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* 
</dt> <dd>

Pointer to a variable that receives a bitwise combination of [**AM\_SEEKING\_SEEKING\_CAPABILITIES**](/windows/win32/strmif/ne-strmif-am_seeking_seekingcapabilities?branch=master) flags.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




