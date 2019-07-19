---
Description: 'Encrypts a message to provide privacy by using NTLM.'
ms.assetid: '852a4624-792d-4f7d-bd3e-5a28692e2ef3'
title: 'EncryptMessage (NTLM) function'
---

# EncryptMessage (NTLM) function

The **EncryptMessage (NTLM)** function encrypts a message to provide [*privacy*](security.p_gly#-security-privacy-gly). **EncryptMessage (NTLM)** allows an application to choose among [*cryptographic algorithms*](security.c_gly#-security-cryptographic-algorithm-gly) supported by the chosen mechanism. The **EncryptMessage (NTLM)** function uses the security context referenced by the context handle. Some packages do not have messages to be encrypted or decrypted but rather provide an integrity [*hash*](security.h_gly#-security-hash-gly) that can be checked.

> [!Note]  
> **EncryptMessage (NTLM)** and [**DecryptMessage (NTLM)**](decryptmessage--ntlm.md) can be called at the same time from two different threads in a single Security Support Provider Interface (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

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

A handle to the security [*context*](security.c_gly#-security-context-gly) to be used to encrypt the message.

*fQOP* \[in\]

Package-specific flags that indicate the quality of protection. A security package can use this parameter to enable the selection of cryptographic algorithms.

This parameter can be the following flag.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Value</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td><span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl> <dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt> </dl></td><td>Produce a header or trailer but do not encrypt the message.<br/><blockquote>[!Note]<br />
KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br/></td></tr></tbody></table>

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures that can be of type SECBUFFER\_DATA. That buffer contains the message to be encrypted. The message is encrypted in place, overwriting the original contents of the structure.

The function does not process buffers with the SECBUFFER\_READONLY attribute.

The length of the [**SecBuffer**](secbuffer.md) structure that contains the message must be no greater than **cbMaximumMessage**, which is obtained from the [**QueryContextAttributes (NTLM)**](querycontextattributes--ntlm.md) (SECPKG\_ATTR\_STREAM\_SIZES) function.

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
| **SEC\_E\_CRYPTO\_SYSTEM\_INVALID** | The [*cipher*](security.c_gly#-security-cipher-gly) chosen for the security context is not supported.                                |
| **SEC\_E\_INSUFFICIENT\_MEMORY**    | There is not enough memory available to complete the requested action.                                                               |
| **SEC\_E\_INVALID\_HANDLE**         | A context handle that is not valid was specified in the *phContext* parameter.                                                       |
| **SEC\_E\_INVALID\_TOKEN**          | No SECBUFFER\_DATA type buffer was found.                                                                                            |
| **SEC\_E\_QOP\_NOT\_SUPPORTED**>    | Neither confidentiality nor [*integrity*](security.i_gly#-security-integrity-gly) are supported by the security context.             |

## Remarks

The **EncryptMessage (NTLM)** function encrypts a message based on the message and the session key from a security context.

If the transport application created the security context to support sequence detection and the caller provides a sequence number, the function includes this information with the encrypted message. Including this information protects against replay, insertion, and suppression of messages. The security package incorporates the sequence number passed down from the transport application.

> [!Note]  
> These buffers must be supplied in the order shown.

| Buffer type                | Description                                                                                 |
|----------------------------|---------------------------------------------------------------------------------------------|
| SECBUFFER\_STREAM\_HEADER  | Used internally. No initialization required.                                                |
| SECBUFFER\_DATA            | Contains the [*plaintext*](security.p_gly#-security-plaintext-gly) message to be encrypted. |
| SECBUFFER\_STREAM\_TRAILER | Used internally. No initialization required.                                                |
| SECBUFFER\_EMPTY           | Used internally. No initialization required. Size can be zero.                              |

For optimal performance, the *pMessage* structures should be allocated from contiguous memory.

**Windows XP:** This function was also known as **SealMessage**. Applications should now use **EncryptMessage (NTLM)** only.

## Requirements

|                          |                                           |
| -------------------------|-------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**AcceptSecurityContext (NTLM)**](acceptsecuritycontext--ntlm.md)
- [**DecryptMessage (NTLM)**](decryptmessage--ntlm.md)
- [**InitializeSecurityContext (NTLM)**](initializesecuritycontext--ntlm.md)
- [**QueryContextAttributes (NTLM)**](querycontextattributes--ntlm.md)
- [**SecBuffer**](secbuffer.md)
- [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea)
