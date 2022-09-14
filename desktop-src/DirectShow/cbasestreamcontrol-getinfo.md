---
description: The GetInfo method retrieves information about the current stream-control settings, including the start and stop times. This method implements the IAMStreamControl::GetInfo method.
ms.assetid: 3bc9bb32-eb33-4752-b22c-9033c28b41f7
title: CBaseStreamControl.GetInfo method (Strmctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl.GetInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseStreamControl.GetInfo method

The `GetInfo` method retrieves information about the current stream-control settings, including the start and stop times. This method implements the [**IAMStreamControl::GetInfo**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-getinfo) method.

## Syntax


```C++
HRESULT GetInfo(
   AM_STREAM_INFO *pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* 
</dt> <dd>

Pointer to an [**AM\_STREAM\_INFO**](/windows/desktop/api/strmif/ns-strmif-am_stream_info) structure, allocated by the caller, that receives the current stream-control settings.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




