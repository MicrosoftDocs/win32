---
description: The GetEncryptionKey method gets the encryption key.
ms.assetid: a80d8660-d13e-483f-b1d7-ee2043ef5cab
title: ITConnection::GetEncryptionKey method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::GetEncryptionKey method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetEncryptionKey** method gets the encryption key.

## Syntax


```C++
HRESULT GetEncryptionKey(
  [out] BSTR         *ppKeyType,
  [out] VARIANT_BOOL *pfValidKeyData,
  [out] BSTR         *ppKeyData
);
```



## Parameters

<dl> <dt>

*ppKeyType* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the type of encryption key.

</dd> <dt>

*pfValidKeyData* \[out\]
</dt> <dd>

Indicates validity of encryption key data.

</dd> <dt>

*ppKeyData* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the encryption key data.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                                                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppKeyType, pfValidKeyData,* or *ppKeyData* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>                              |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                                                |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                                               |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppKeyType* and *ppKeyData* parameters.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConnection**](itconnection.md)
</dt> </dl>

 

