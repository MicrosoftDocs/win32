---
description: The GetPhoneNumbers method gets an array of phone numbers associated with a conference blob.
ms.assetid: c4ad6c5a-e15c-45ae-94de-763a843554bb
title: ITSdp::GetPhoneNumbers method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::GetPhoneNumbers method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetPhoneNumbers** method gets an array of phone numbers associated with a conference blob.

## Syntax


```C++
HRESULT GetPhoneNumbers(
  [out] VARIANT *pNumbers,
  [out] VARIANT *pNames
);
```



## Parameters

<dl> <dt>

*pNumbers* \[out\]
</dt> <dd>

**VARIANT** pointer to a SAFEARRAY of **BSTR**s listing phone numbers.

</dd> <dt>

*pNames* \[out\]
</dt> <dd>

**VARIANT** pointer to a SAFEARRAY of **BSTR**s listing names.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                             |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pNumbers* or *pNames* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                          |



 

## Remarks

The lists that *pNumbers* and *pNames* point to are the same length.

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

 

 




