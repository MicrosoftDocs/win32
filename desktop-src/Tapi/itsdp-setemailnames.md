---
description: The SetEmailNames method sets an array of e-mail addresses associated with the conference blob.
ms.assetid: 1d6d5b01-bc0f-455f-8b23-bc0f409afde4
title: ITSdp::SetEmailNames method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::SetEmailNames method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetEmailNames** method sets an array of e-mail addresses associated with the conference blob.

## Syntax


```C++
HRESULT SetEmailNames(
  [in] VARIANT Addresses,
  [in] VARIANT Names
);
```



## Parameters

<dl> <dt>

*Addresses* \[in\]
</dt> <dd>

SAFEARRAY of **BSTR**s listing e-mail addresses.

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Addresses* or *Names* parameter is not valid.<br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The lists that *Addresses* and *Names* point to are the same length.

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

 

 




