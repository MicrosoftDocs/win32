---
description: The GetEmailNames method gets an array of e-mail names associated with the conference blob.
ms.assetid: e51f25d7-41e5-408e-930b-396c7ac24437
title: ITSdp::GetEmailNames method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::GetEmailNames method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetEmailNames** method gets an array of e-mail names associated with the conference blob.

## Syntax


```C++
HRESULT GetEmailNames(
  [out] VARIANT *pAddresses,
  [out] VARIANT *pNames
);
```



## Parameters

<dl> <dt>

*pAddresses* \[out\]
</dt> <dd>

**VARIANT** pointer to a SAFEARRAY of **BSTR**s listing e-mail addresses.

</dd> <dt>

*pNames* \[out\]
</dt> <dd>

**VARIANT** pointer to a SAFEARRAY of **BSTR**s listing names.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                              |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pAddresses* or *pNames* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>           |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                             |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                            |



 

## Remarks

The lists that *pAddresses* and *pNames* point to are the same length.

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

 

 




