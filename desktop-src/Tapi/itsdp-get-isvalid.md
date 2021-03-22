---
description: The get\_IsValid method validates the Session Descriptor Protocol (SDP; see RFC 2327) blob for structure and field values.
ms.assetid: a3f849ac-bda9-4937-bf3b-bce8df20cbf0
title: ITSdp::get_IsValid method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_IsValid method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_IsValid** method validates the Session Descriptor Protocol (SDP; see RFC 2327) blob for structure and field values.

## Syntax


```C++
HRESULT get_IsValid(
  [out] VARIANT_BOOL *pfIsValid
);
```



## Parameters

<dl> <dt>

*pfIsValid* \[out\]
</dt> <dd>

Indicates whether the blob structure is valid.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pfIsValid* parameter is not valid.<br/>              |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pfIsValid* parameter is not a valid pointer.<br/>    |
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

[**ITSdp**](itsdp.md)
</dt> </dl>

 

 




