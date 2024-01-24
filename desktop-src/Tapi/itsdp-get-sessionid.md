---
description: The get\_SessionId method gets the 32-bit NTP (Network Time Protocol) value that serves as the session identifier. This is generated automatically when the session is created.
ms.assetid: 5177f120-4b93-40bc-9481-aedf65a8dee9
title: ITSdp::get_SessionId method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_SessionId method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_SessionId** method gets the 32-bit NTP (Network Time Protocol) value that serves as the session identifier. This is generated automatically when the session is created.

## Syntax


```C++
HRESULT get_SessionId(
  [out] DOUBLE *pSessionId
);
```



## Parameters

<dl> <dt>

*pSessionId* \[out\]
</dt> <dd>

Pointer to the session identifier.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pSessionId* parameter is not valid.<br/>             |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pSessionId* parameter is not a valid pointer.<br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The return value of this method could be **ULONG**, but Visual Basic doesn't support the **ULONG** type. A **DOUBLE** is the next smallest type that encompasses the entire range of values required.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITSdp**](itsdp.md)
</dt> </dl>

 

 




