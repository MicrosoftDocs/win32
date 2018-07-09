---
Description: Retrieves a handle to the handshake hash that is used for client authentication.
ms.assetid: 55007ce0-4bf1-4605-9b34-2931935762aa
title: SslCreateClientAuthHash function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslCreateClientAuthHash
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslCreateClientAuthHash function

The **SslCreateClientAuthHash** function retrieves a handle to the handshake [*hash*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hash-gly) that is used for client authentication.

## Syntax


```C++
SECURITY_STATUS WINAPI SslCreateClientAuthHash(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _Out_ NCRYPT_HASH_HANDLE *phHandshakeHash,
  _In_  DWORD              dwProtocol,
  _In_  DWORD              dwCipherSuite,
  _In_  LPCWSTR            pszHashAlgId,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the [*Secure Sockets Layer protocol*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-secure-sockets-layer-protocol-gly) (SSL) protocol provider instance.

</dd> <dt>

*phHandshakeHash* \[out\]
</dt> <dd>

A pointer to an **NCRYPT\_HASH\_HANDLE** variable to receive the hash handle.

</dd> <dt>

*dwProtocol* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Protocol Identifier**](https://www.bing.com/search?q=**CNG+SSL+Provider+Protocol+Identifier**) values.

</dd> <dt>

*dwCipherSuite* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Cipher Suite Identifier**](https://www.bing.com/search?q=**CNG+SSL+Provider+Cipher+Suite+Identifier**) values.

</dd> <dt>

*pszHashAlgId* \[in\]
</dt> <dd>

One of the [**CNG Algorithm Identifiers**](cng-algorithm-identifiers.md) values.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use and must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* parameter contains a pointer that is not valid.<br/>                |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phHandshakeHash* parameter is set to **NULL**.<br/>                               |
| <dl> <dt>**NTE\_NOT\_SUPPORTED**</dt> <dt>0x80090029L</dt> </dl>     | The selected function is not supported in the specified version of the interface.<br/> |
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Insufficient memory to allocate buffers.<br/>                                          |
| <dl> <dt>**NTE\_BAD\_FLAGS**</dt> <dt>0x80090009L</dt> </dl>         | The *dwFlags* parameter must be set to zero.<br/>                                      |



 

## Remarks

The **SslCreateClientAuthHash** function is called for [*Transport Layer Security protocol*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-transport-layer-security-protocol-gly) (TLS) 1.2 or later conversations to create hash objects that are used to hash handshake messages. It is called once for each possible [*hashing algorithm*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hashing-algorithm-gly) that can be used in the client authentication signature.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

 




