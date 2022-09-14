---
description: Decrypts a message by using Digest.
ms.assetid: 46d45f59-33fa-434a-b329-20b6257c9a19
title: DecryptMessage (Digest) function
ms.topic: reference
ms.date: 07/25/2019
---

# DecryptMessage (Digest) function

The **DecryptMessage (Digest)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](../secgloss/h-gly.md).

The Digest [*security support provider*](../secgloss/s-gly.md) (SSP) provides encryption and decryption confidentiality for messages exchanged between client and server as a SASL mechanism only.

> [!Note]  
> [**EncryptMessage (Digest)**](encryptmessage--digest.md) and **DecryptMessage (Digest)** can be called at the same time from two different threads in a single [*security support provider interface*](../secgloss/s-gly.md) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

## Syntax

```C++
SECURITY_STATUS SEC_ENTRY DecryptMessage(
  PCtxtHandle    phContext,
  PSecBufferDesc pMessage,
  unsigned long  MessageSeqNo,
  unsigned long  *pfQOP
);
```

## Parameters

*phContext* \[in\]

A handle to the [*security context*](../secgloss/s-gly.md) to be used to decrypt the message.

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. At least one of these must be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

When using the Digest SSP, on input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. One of these must be of type SECBUFFER\_DATA or SECBUFFER\_STREAM, and it must contain the encrypted message.

*MessageSeqNo* \[in\]

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

When using the Digest SSP, this parameter must be set to zero. The Digest SSP manages sequence numbering internally.

*pfQOP* \[out\]

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

This parameter can be one of the following flags.


| Value | Meaning | 
|-------|---------|
| <span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl><dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt></dl> | The message was not encrypted, but a header or trailer was produced.<br /><blockquote>[!Note]<br />KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br /> | 
| <span id="SIGN_ONLY_"></span><span id="sign_only_"></span><dl><dt><strong>SIGN_ONLY</strong></dt></dl> | When using the Digest SSP, use this flag when the [*security context*](../secgloss/s-gly.md) is set to verify the [*signature*](../secgloss/s-gly.md) only. For more information, see [Quality of Protection](quality-of-protection.md).<br /> | 


## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.

| Return code                         | Description                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEC\_E\_BUFFER\_TOO\_SMALL**      | The message buffer is too small. Used with the Digest SSP.                                                                                                                   |
| **SEC\_E\_CRYPTO\_SYSTEM\_INVALID** | The [*cipher*](../secgloss/c-gly.md) chosen for the [*security context*](../secgloss/s-gly.md) is not supported. Used with the Digest SSP.                                                                                       |
| **SEC\_E\_INCOMPLETE\_MESSAGE**     | The data in the input buffer is incomplete. The application needs to read more data from the server and call [**DecryptMessage (Digest)**](decryptmessage--digest.md) again. |
| **SEC\_E\_INVALID\_HANDLE**         | A context handle that is not valid was specified in the *phContext* parameter. Used with the Digest SSP.                                                                     |
| **SEC\_E\_MESSAGE\_ALTERED**        | The message has been altered. Used with the Digest SSP.                                                                                                                      |
| **SEC\_E\_OUT\_OF\_SEQUENCE**       | The message was not received in the correct sequence.                                                                                                                        |
| **SEC\_E\_QOP\_NOT\_SUPPORTED**     | Neither confidentiality nor [*integrity*](../secgloss/i-gly.md) are supported by the [*security context*](../secgloss/s-gly.md). Used with the Digest SSP.                           |

## Remarks

Sometimes an application will read data from the remote party, attempt to decrypt it by using **DecryptMessage (Digest)**, and discover that **DecryptMessage (Digest)** succeeded but the output buffers are empty. This is normal behavior, and applications must be able to deal with it.

**Windows XP:** This function was also known as **UnsealMessage**. Applications should now use **DecryptMessage (Digest)** only.

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**EncryptMessage (Digest)**](encryptmessage--digest.md)
- [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
- [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
