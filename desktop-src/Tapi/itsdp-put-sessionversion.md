---
description: The put\_SessionVersion method sets the session version.
ms.assetid: 8984d608-0fad-4979-9c58-ac2fb7926796
title: ITSdp::put_SessionVersion method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::put\_SessionVersion method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_SessionVersion** method sets the session version.

## Syntax


```C++
HRESULT put_SessionVersion(
  [in] DOUBLE SessionVersion
);
```



## Parameters

<dl> <dt>

*SessionVersion* \[in\]
</dt> <dd>

Session version value.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *SessionVersion* parameter is not valid.<br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The return value of this method could be **ULONG**, but Visual Basic doesn't support the **ULONG** type. A **DOUBLE** is the next smallest type that encompasses the entire range of values required.

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

[**ITSdp**](itsdp.md)
</dt> <dt>

[**ITSdp::get\_SessionVersion**](itsdp-get-sessionversion.md)
</dt> </dl>

 

 




