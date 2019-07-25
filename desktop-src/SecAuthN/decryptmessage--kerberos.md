---
Description: 'Decrypts a message by using Kerberos.'
ms.assetid: '9e699f7c-f738-4702-bdef-fb2c276c38fc'
title: 'DecryptMessage (Kerberos) function'
ms.topic: article
ms.date: 07/25/2019
---

# DecryptMessage (Kerberos) function

The **DecryptMessage (Kerberos)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](https://docs.microsoft.com/en-us/windows/win32/secgloss/h-gly).

> [!Note]  
> [**EncryptMessage (Kerberos)**](encryptmessage--kerberos.md) and **DecryptMessage (Kerberos)** can be called at the same time from two different threads in a single [*security support provider interface*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

## Syntax

```C++
SECURITY_STATUS SEC_Entry DecryptMessage(
  _In_    PCtxtHandle    phContext,
  _Inout_ PSecBufferDesc pMessage,
  _In_    ULONG          MessageSeqNo,
  _Out_   PULONG         pfQOP
);
```

## Parameters

*phContext* \[in\]

A handle to the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) to be used to decrypt the message.

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures that may be of type SECBUFFER\_DATA. The buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

*MessageSeqNo* \[in\]

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

*pfQOP* \[out\]

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

This parameter can be the following flag.

| Value                  | Meaning                                                             |
|------------------------|---------------------------------------------------------------------|
| SECQOP_WRAP_NO_ENCRYPT | he message was not encrypted, but a header or trailer was produced. |

> [!NOTE]
> KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.

## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.

| Return code                     | Description                                                                                                                                                                      |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEC\_E\_INCOMPLETE\_MESSAGE** | The data in the input buffer is incomplete. The application needs to read more data from the server and call [**DecryptMessage (Kerberos)**](decryptmessage--kerberos.md) again. |
| **SEC\_E\_OUT\_OF\_SEQUENCE**   | The message was not received in the correct sequence.                                                                                                                            |

## Remarks

Sometimes an application will read data from the remote party, attempt to decrypt it by using **DecryptMessage (Kerberos)**, and discover that **DecryptMessage (Kerberos)** succeeded but the output buffers are empty. This is normal behavior, and applications must be able to deal with it.

For information about interoperating with GSSAPI, see [SSPI/Kerberos Interoperability with GSSAPI](sspi-kerberos-interoperability-with-gssapi.md).

**Windows XP:** This function was also known as **UnsealMessage**. Applications should now use **DecryptMessage (Kerberos)** only.

## Requirements

|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**EncryptMessage (Kerberos)**](encryptmessage--kerberos.md)
- [**SecBuffer**](secbuffer.md)
- [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea)
