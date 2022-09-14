---
description: The SetEncryptionKey method sets the encryption key needed to decrypt the session or an indication to a mechanism to obtain a usable key by external means.
ms.assetid: 9efcf90e-3645-49f4-b27d-9a8246637310
title: ITConnection::SetEncryptionKey method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITConnection::SetEncryptionKey method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetEncryptionKey** method sets the encryption key needed to decrypt the session or an indication to a mechanism to obtain a usable key by external means.

## Syntax


```C++
HRESULT SetEncryptionKey(
  [in] BSTR pKeyType,
  [in] BSTR *ppKeyData
);
```



## Parameters

<dl> <dt>

*pKeyType* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the encryption key type.

</dd> <dt>

*ppKeyData* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing encryption key information.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                  |
|--------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Method succeeded.<br/> |



 

## Remarks

The application must use [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *pKeyType* and *ppKeyData* parameters. The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variables are no longer needed.

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

 

