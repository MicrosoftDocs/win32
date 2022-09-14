---
description: The get\_StopTime method gets the NTP (Network Time Protocol) ending time value. If the end time is zero, the session is not bounded.
ms.assetid: f18042c0-e41d-43b3-a75d-6ab161afde6e
title: ITTime::get_StopTime method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTime::get\_StopTime method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_StopTime** method gets the NTP (Network Time Protocol) ending time value. If the end time is zero, the session is not bounded.

## Syntax


```C++
HRESULT get_StopTime(
  [out] DOUBLE *pTime
);
```



## Parameters

<dl> <dt>

*pTime* \[out\]
</dt> <dd>

Pointer to the stop time for the session.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pTime* parameter is not a valid pointer.<br/>        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITTime**](ittime.md)
</dt> <dt>

[**ITTime::put\_StopTime**](ittime-put-stoptime.md)
</dt> </dl>

 

 




