---
description: The get\_SessionVersion method gets the 32-bit (ideally Network Time Protocol, or NTP) value that serves as the session version.
ms.assetid: 39c2aef4-24e3-4ea0-8b23-dff842f9ab84
title: ITSdp::get_SessionVersion method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_SessionVersion method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_SessionVersion** method gets the 32-bit (ideally Network Time Protocol, or NTP) value that serves as the session version. Although this is generated automatically when the session is created, the user is responsible for changing it when the SDP is modified.

## Syntax


```C++
HRESULT get_SessionVersion(
  [out] DOUBLE *pSessionVersion
);
```



## Parameters

<dl> <dt>

*pSessionVersion* \[out\]
</dt> <dd>

Pointer to the session version identifier.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                        |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pSessionVersion* parameter is not valid.<br/>           |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pSessionVersion* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>    |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                      |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                     |



 

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
</dt> <dt>

[**ITSdp::put\_SessionVersion**](itsdp-put-sessionversion.md)
</dt> </dl>

 

 




