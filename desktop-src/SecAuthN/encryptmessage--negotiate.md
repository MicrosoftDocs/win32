---
Description: 'Encrypts a message to provide privacy by using Negotiate.'
ms.assetid: 'b80b3d64-9c0a-4602-9378-1e208f6593fc'
title: 'EncryptMessage (Negotiate) function'
ms.topic: article
ms.date: 07/25/2019
---

# EncryptMessage (Negotiate) function

The **EncryptMessage (Negotiate)** function encrypts a message to provide [*privacy*](https://docs.microsoft.com/en-us/windows/win32/secgloss/p-gly). **EncryptMessage (Negotiate)** allows the application to choose among [*cryptographic algorithms*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly) supported by the chosen mechanism. The **EncryptMessage (Negotiate)** function uses the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) referenced by the context handle. Some packages do not have messages to be encrypted or decrypted but rather provide an integrity [*hash*](https://docs.microsoft.com/en-us/windows/win32/secgloss/h-gly) that can be checked.

> [!Note]  
> **EncryptMessage (Negotiate)** and [**DecryptMessage (Negotiate)**](decryptmessage--negotiate.md) can be called at the same time from two different threads in a single [*security support provider interface*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

## Syntax

```C++
SECURITY_STATUS SEC_Entry EncryptMessage(
  _In_    PCtxtHandle    phContext,
  _In_    ULONG          fQOP,
  _Inout_ PSecBufferDesc pMessage,
  _In_    ULONG          MessageSeqNo
);
```

## Parameters

*phContext* \[in\]
A handle to the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) to be used to encrypt the message.

*fQOP* \[in\]
Package-specific flags that indicate the quality of protection. A [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) can use this parameter to enable the selection of [*cryptographic algorithms*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly).

This parameter can be the following flag.

| Value                  | Meaning                                                     |
|------------------------|-------------------------------------------------------------|
| SECQOP_WRAP_NO_ENCRYPT | Produce a header or trailer but do not encrypt the message. |

> [!NOTE]
> KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.

*pMessage* \[in, out\]
A pointer to a [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures that can be of type SECBUFFER\_DATA. That buffer contains the message to be encrypted. The message is encrypted in place, overwriting the original contents of the structure.

The function does not process buffers with the SECBUFFER\_READONLY attribute.

The length of the [**SecBuffer**](secbuffer.md) structure that contains the message must be no greater than **cbMaximumMessage**, which is obtained from the [**QueryContextAttributes (Negotiate)**](querycontextattributes--negotiate.md) (SECPKG\_ATTR\_STREAM\_SIZES) function.

Applications that do not use SSL must supply a [**SecBuffer**](secbuffer.md) of type SECBUFFER\_PADDING.

*MessageSeqNo* \[in\]
The sequence number that the transport application assigned to the message. If the transport application does not maintain sequence numbers, this parameter must be zero.

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.

| Return code                         | Description                                                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **SEC\_E\_BUFFER\_TOO\_SMALL**      | The output buffer is too small. For more information, see Remarks.                                                                   |
| **SEC\_E\_CONTEXT\_EXPIRED**        | The application is referencing a context that has already been closed. A properly written application should not receive this error. |
| **SEC\_E\_CRYPTO\_SYSTEM\_INVALID** | The [*cipher*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly) chosen for the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) is not supported.                                |
| **SEC\_E\_INSUFFICIENT\_MEMORY**    | There is not enough memory available to complete the requested action.                                                               |
| **SEC\_E\_INVALID\_HANDLE**         | A context handle that is not valid was specified in the *phContext* parameter.                                                       |
| **SEC\_E\_INVALID\_TOKEN**          | No SECBUFFER\_DATA type buffer was found.                                                                                            |
| **SEC\_E\_QOP\_NOT\_SUPPORTED**     | Neither confidentiality nor [*integrity*](https://docs.microsoft.com/en-us/windows/win32/secgloss/i-gly) are supported by the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly).             |

## Remarks

The **EncryptMessage (Negotiate)** function encrypts a message based on the message and the [*session key*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) from a [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly).

If the transport application created the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) to support sequence detection and the caller provides a sequence number, the function includes this information with the encrypted message. Including this information protects against replay, insertion, and suppression of messages. The [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) incorporates the sequence number passed down from the transport application.

> [!Note]  
> These buffers must be supplied in the order shown.

| Buffer type                | Description                                                                                 |
|----------------------------|---------------------------------------------------------------------------------------------|
| SECBUFFER\_STREAM\_HEADER  | Used internally. No initialization required.                                                |
| SECBUFFER\_DATA            | Contains the [*plaintext*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) message to be encrypted. |
| SECBUFFER\_STREAM\_TRAILER | Used internally. No initialization required.                                                |
| SECBUFFER\_EMPTY           | Used internally. No initialization required. Size can be zero.                              |

For optimal performance, the *pMessage* structures should be allocated from contiguous memory.

**Windows XP:** This function was also known as **SealMessage**. Applications should now use **EncryptMessage (Negotiate)** only.

## Requirements

|                          |                                                 |
|--------------------------|-------------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]                |
| Minimum supported server | Windows Server 2003 \[desktop apps only\]       |
| Header                   | Sspi.h (include Security.h)                     |
| Library                  | Secur32.lib                                     |
| DLL                      | Secur32.dll                                     |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**AcceptSecurityContext (Negotiate)**](acceptsecuritycontext--negotiate.md)
- [**DecryptMessage (Negotiate)**](decryptmessage--negotiate.md)
- [**InitializeSecurityContext (Negotiate)**](initializesecuritycontext--negotiate.md)
- [**QueryContextAttributes (Negotiate)**](querycontextattributes--negotiate.md)
- [**SecBuffer**](secbuffer.md)
- [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea)
