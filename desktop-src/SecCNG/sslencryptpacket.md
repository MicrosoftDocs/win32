---
description: Encrypts a single Secure Sockets Layer protocol (SSL) packet.
ms.assetid: 1002158b-1a4f-4461-978f-b221ef6332e0
title: SslEncryptPacket function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslEncryptPacket
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslEncryptPacket function

The **SslEncryptPacket** function encrypts a single [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) packet.

## Syntax


```C++
SECURITY_STATUS WINAPI SslEncryptPacket(
  _In_    NCRYPT_PROV_HANDLE hSslProvider,
  _Inout_ NCRYPT_KEY_HANDLE  hKey,
  _In_    PBYTE              *pbInput,
  _In_    DWORD              cbInput,
  _Out_   PBYTE              pbOutput,
  _In_    DWORD              cbOutput,
  _Out_   DWORD              *pcbResult,
  _In_    ULONGLONG          SequenceNumber,
  _In_    DWORD              dwContentType,
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

The handle to the key that is used to encrypt the packet.

</dd> <dt>

*pbInput* \[in\]
</dt> <dd>

A pointer to the buffer that contains the packet to be encrypted.

</dd> <dt>

*cbInput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbInput* buffer.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

A pointer to a buffer to receive the encrypted packet.

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

*dwContentType* \[in\]
</dt> <dd>

The content type that corresponds to this packet, which specifies the higher level protocol used to process the enclosed packet.



| Value                                                                                                                                                                                                                                           | Meaning                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <span id="CT_CHANGE_CIPHER_SPEC"></span><span id="ct_change_cipher_spec"></span><dl> <dt>**CT\_CHANGE\_CIPHER\_SPEC**</dt> <dt>20</dt> </dl> | Indicates a change in the ciphering strategy.<br/>                         |
| <span id="CT_ALERT"></span><span id="ct_alert"></span><dl> <dt>**CT\_ALERT**</dt> <dt>21</dt> </dl>                                          | Indicates that the enclosed packet contains an alert.<br/>                 |
| <span id="CT_HANDSHAKE"></span><span id="ct_handshake"></span><dl> <dt>**CT\_HANDSHAKE**</dt> <dt>22</dt> </dl>                              | Indicates that the enclosed packet is part of the handshake protocol.<br/> |
| <span id="CT_APPLICATIONDATA"></span><span id="ct_applicationdata"></span><dl> <dt>**CT\_APPLICATIONDATA**</dt> <dt>23</dt> </dl>            | Indicates that the packet contains application data.<br/>                  |



 

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



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

