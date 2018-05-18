---
Description: 'The GetInfo method retrieves information about the current stream-control settings, including the start and stop times. This method implements the IAMStreamControl::GetInfo method.'
ms.assetid: '3bc9bb32-eb33-4752-b22c-9033c28b41f7'
title: 'CBaseStreamControl.GetInfo method'
---

# CBaseStreamControl.GetInfo method

The `GetInfo` method retrieves information about the current stream-control settings, including the start and stop times. This method implements the [**IAMStreamControl::GetInfo**](iamstreamcontrol-getinfo.md) method.

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

Pointer to an [**AM\_STREAM\_INFO**](am-stream-info.md) structure, allocated by the caller, that receives the current stream-control settings.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




