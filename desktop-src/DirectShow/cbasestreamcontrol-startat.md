---
Description: The StartAt method informs the pin when to start delivering data. This method implements the IAMStreamControl::StartAt method.
ms.assetid: fd2943e8-8d35-4122-a99e-96d12459b335
title: CBaseStreamControl.StartAt method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseStreamControl.StartAt method

The `StartAt` method informs the pin when to start delivering data. This method implements the [**IAMStreamControl::StartAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-startat) method.

## Syntax


```C++
HRESULT StartAt(
   const REFERENCE_TIME *ptStart = NULL,
         DWORD          dwCookie = 0
);
```



## Parameters

<dl> <dt>

*ptStart* 
</dt> <dd>

Pointer to a [**REFERENCE\_TIME**](reference-time.md) value that specifies when the pin should start delivering data.

</dd> <dt>

*dwCookie* 
</dt> <dd>

Specifies a value to send along with the start notification.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




