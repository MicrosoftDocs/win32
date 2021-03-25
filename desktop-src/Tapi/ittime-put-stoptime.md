---
description: The put\_StopTime method sets the NTP (Network Time Protocol) ending time value. If the end time is zero, the session is not bounded.
ms.assetid: 6f07054c-5fb2-4ee4-9025-3acf9b51ddbd
title: ITTime::put_StopTime method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTime::put\_StopTime method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_StopTime** method sets the NTP (Network Time Protocol) ending time value. If the end time is zero, the session is not bounded.

## Syntax


```C++
HRESULT put_StopTime(
  [in] DOUBLE Time
);
```



## Parameters

<dl> <dt>

*Time* \[in\]
</dt> <dd>

Stop time for the session.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Time* parameter is not valid.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

This function may send data over the wire in unencrypted form; therefore, someone eavesdropping on the network may be able to read the data. The security risk of sending the data in clear text should be considered before using this method.

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

[**ITTime::get\_StopTime**](ittime-get-stoptime.md)
</dt> </dl>

 

 




