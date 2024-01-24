---
description: Increments the reference count to a Secure Sockets Layer protocol (SSL) provider instance.
ms.assetid: 67e7b8b4-b073-4936-b1e0-3fc7c1c011a2
title: SslIncrementProviderReferenceCount function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslIncrementProviderReferenceCount
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslIncrementProviderReferenceCount function

The **SslIncrementProviderReferenceCount** function increments the reference count to a [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) provider instance.

## Syntax


```C++
SECURITY_STATUS WINAPI SslIncrementProviderReferenceCount(
  _In_ NCRYPT_PROV_HANDLE hSslProvider
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the SSL protocol provider instance.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | The *hSslProvider* handle is not valid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

