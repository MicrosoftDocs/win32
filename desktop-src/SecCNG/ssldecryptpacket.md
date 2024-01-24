---
description: Decrypts a single Secure Sockets Layer protocol (SSL) packet.
ms.assetid: 22a7dd2b-d023-47b9-8f76-1c17c2dd6466
title: SslDecryptPacket function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslDecryptPacket
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslDecryptPacket function

the **SslDecryptPacket** function decrypts a single [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) packet.

## Syntax


```C++
SECURITY_STATUS WINAPI SslDecryptPacket(
  _In_    NCRYPT_PROV_HANDLE hSslProvider,
  _Inout_ NCRYPT_KEY_HANDLE  hKey,
  _In_    PBYTE              *pbInput,
  _In_    DWORD              cbInput,
  _Out_   PBYTE              pbOutput,
  _In_    DWORD              cbOutput,
  _Out_   DWORD              *pcbResult,
  _In_    ULONGLONG          SequenceNumber,
  _In_    DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the SSL protocol provider instance.

</dd> <dt>

*hKey* \[in, out\]
</dt> <dd>

The handle to the key that is used to decrypt the packet.

</dd> <dt>

*pbInput* \[in\]
</dt> <dd>

A pointer to the buffer that contains the packet to be decrypted.

</dd> <dt>

*cbInput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbInput* buffer.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

A pointer to a buffer to contain the decrypted packet.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The length, bytes, of the *pbOutput* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

The number of bytes written to the *pbOutput* buffer.

</dd> <dt>

*SequenceNumber* \[in\]
</dt> <dd>

The sequence number that corresponds to this packet.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the provided handles is not valid.<br/> |



 

## Remarks

The length of the packet can be zero, such as when a "HelloRequest" message is decrypted.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

