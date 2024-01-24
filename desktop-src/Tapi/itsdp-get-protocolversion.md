---
description: The get\_ProtocolVersion method gets the Session Descriptor Protocol (SDP; see RFC 2327) protocol version.
ms.assetid: 7c62357c-427f-40f9-a9d2-c4e1a8400e97
title: ITSdp::get_ProtocolVersion method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_ProtocolVersion method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_ProtocolVersion** method gets the Session Descriptor Protocol (SDP; see RFC 2327) protocol version.

## Syntax


```C++
HRESULT get_ProtocolVersion(
  [out] unsigned char *pProtocolVersion
);
```



## Parameters

<dl> <dt>

*pProtocolVersion* \[out\]
</dt> <dd>

Pointer to the protocol version.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                         |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                        |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pProtocolVersion* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>     |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                       |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                      |



 

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

 

 




