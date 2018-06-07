---
Description: Opens a handle to a private key.
ms.assetid: 2406be2c-121c-4475-b193-d370a88641da
title: SslOpenPrivateKey function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SslOpenPrivateKey function

The **SslOpenPrivateKey** function opens a handle to a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).

## Syntax


```C++
SECURITY_STATUS WINAPI SslOpenPrivateKey(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _Out_ NCRYPT_KEY_HANDLE  *phPrivateKey,
  _In_  PCCERT_CONTEXT     pCertContext,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the [*Secure Sockets Layer protocol*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-secure-sockets-layer-protocol-gly) (SSL) protocol provider instance.

</dd> <dt>

*phPrivateKey* \[out\]
</dt> <dd>

The address of a buffer in which to write the handle to the private key.

When you have finished using the key, you should free *phPrivateKey* by calling the [**SslFreeObject**](sslfreeobject.md) function.

</dd> <dt>

*pCertContext* \[in\]
</dt> <dd>

The address of the certificate from which to obtain the private key.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Not enough memory is available to allocate necessary buffers.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* handle is not valid.<br/>                       |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phPrivateKey* or *pCertContext* parameter is **NULL**.<br/>   |



 

## Remarks

The private key obtained is part of a [*public/private key pair*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-private-key-pair-gly) within a [*certificate*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-gly). This function merely extracts the private key from the certificate specified by the *pCertContext* parameter.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

 




