---
description: The CheckCapabilities method queries whether a stream has specified seeking capabilities. This method implements the IMediaSeeking::CheckCapabilities method.
ms.assetid: 48096af6-bbce-4a1f-be9a-fd150ed4536e
title: CPosPassThru.CheckCapabilities method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.CheckCapabilities
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.CheckCapabilities method

The `CheckCapabilities` method queries whether a stream has specified seeking capabilities. This method implements the [**IMediaSeeking::CheckCapabilities**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-checkcapabilities) method.

## Syntax


```C++
HRESULT CheckCapabilities(
   DWORD *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* 
</dt> <dd>

Pointer to a bitwise combination of one or more [**AM\_SEEKING\_SEEKING\_CAPABILITIES**](/windows/win32/api/strmif/ne-strmif-am_seeking_seeking_capabilities) attributes. When the method returns, the value indicates which of those attributes are available.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




