---
description: Decrypts a message by using Negotiate.
ms.assetid: 188341ff-4e67-481e-af30-7f9913b1d24e
title: DecryptMessage (Negotiate) function
ms.topic: reference
ms.date: 07/25/2019
---

# DecryptMessage (Negotiate) function

The **DecryptMessage (Negotiate)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](../secgloss/h-gly.md).

> [!Note]  
> [**EncryptMessage (Negotiate)**](encryptmessage--negotiate.md) and **DecryptMessage (Negotiate)** can be called at the same time from two different threads in a single [*security support provider interface*](../secgloss/s-gly.md) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

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

A handle to the [*security context*](../secgloss/s-gly.md) to be used to decrypt the message.

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures . At least one of these must be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

*MessageSeqNo* \[in\]

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

*pfQOP* \[out\]

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

This parameter can be the following flag.


| Value | Meaning | 
|-------|---------|
| <span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl><dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt></dl> | The message was not encrypted, but a header or trailer was produced.<br /><blockquote>[!Note]<br />KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br /> | 


## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.

| Return code                     | Description                                                                                                                                                                        |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEC\_E\_INCOMPLETE\_MESSAGE** | The data in the input buffer is incomplete. The application needs to read more data from the server and call [**DecryptMessage (Negotiate)**](decryptmessage--negotiate.md) again. |
| **SEC\_E\_OUT\_OF\_SEQUENCE**   | The message was not received in the correct sequence.                                                                                                                              |

## Remarks

Sometimes an application will read data from the remote party, attempt to decrypt it by using **DecryptMessage (Negotiate)**, and discover that **DecryptMessage (Negotiate)** succeeded but the output buffers are empty. This is normal behavior, and applications must be able to deal with it.

**Windows XP:** This function was also known as **UnsealMessage**. Applications should now use **DecryptMessage (Negotiate)** only.

## Requirements

| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**EncryptMessage (Negotiate)**](encryptmessage--negotiate.md)
- [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
- [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
