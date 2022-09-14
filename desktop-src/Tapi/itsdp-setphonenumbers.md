---
description: The SetPhoneNumbers method sets an array of phone numbers associated with a conference blob.
ms.assetid: 674c08df-7e91-4f19-9d65-4bc6e7af117b
title: ITSdp::SetPhoneNumbers method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::SetPhoneNumbers method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetPhoneNumbers** method sets an array of phone numbers associated with a conference blob.

## Syntax


```C++
HRESULT SetPhoneNumbers(
  [in] VARIANT Numbers,
  [in] VARIANT Names
);
```



## Parameters

<dl> <dt>

*Numbers* \[in\]
</dt> <dd>

SAFEARRAY of **BSTR**s listing phone numbers.

</dd> <dt>

*Names* \[in\]
</dt> <dd>

SAFEARRAY of **BSTR**s listing names.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Numbers* or *Names* parameter is not valid.<br/>     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The lists that *Numbers* and *Names* point to are the same length.

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

 

 




