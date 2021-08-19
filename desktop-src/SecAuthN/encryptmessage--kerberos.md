---
description: Encrypts a message to provide privacy by using Kerberos.
ms.assetid: b9b6ca95-b986-4de7-bd28-994a5125ad05
title: EncryptMessage (Kerberos) function
ms.topic: reference
ms.date: 07/25/2019
---

# EncryptMessage (Kerberos) function

The **EncryptMessage (Kerberos)** function encrypts a message to provide [*privacy*](../secgloss/p-gly.md). **EncryptMessage (Kerberos)** allows an application to choose among [*cryptographic algorithms*](../secgloss/c-gly.md) supported by the chosen mechanism. The **EncryptMessage (Kerberos)** function uses the [*security context*](../secgloss/s-gly.md) referenced by the context handle. Some packages do not have messages to be encrypted or decrypted but rather provide an integrity [*hash*](../secgloss/h-gly.md) that can be checked.

> [!Note]  
> **EncryptMessage (Kerberos)** and [**DecryptMessage (Kerberos)**](decryptmessage--kerberos.md) can be called at the same time from two different threads in a single [*security support provider interface*](../secgloss/s-gly.md) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

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

<dl> <dt>

*phContext* \[in\]
</dt> <dd>

A handle to the [*security context*](../secgloss/s-gly.md) to be used to encrypt the message.

</dd> <dt>

*fQOP* \[in\]
</dt> <dd>

Package-specific flags that indicate the quality of protection. A [*security package*](../secgloss/s-gly.md) can use this parameter to enable the selection of [*cryptographic algorithms*](../secgloss/c-gly.md).

This parameter can be the following flag.


| Value | Meaning | 
|-------|---------|
| <span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl><dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt></dl> | Produce a header or trailer but do not encrypt the message.<br /><blockquote>[!Note]<br />KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br /> | 


</dd> <dt>

*pMessage* \[in, out\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures that can be of type SECBUFFER\_DATA. That buffer contains the message to be encrypted. The message is encrypted in place, overwriting the original contents of the structure.

The function does not process buffers with the SECBUFFER\_READONLY attribute.

The length of the [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structure that contains the message must be no greater than **cbMaximumMessage**, which is obtained from the [**QueryContextAttributes (Kerberos)**](querycontextattributes--kerberos.md) (SECPKG\_ATTR\_STREAM\_SIZES) function.

Applications that do not use SSL must supply a [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) of type SECBUFFER\_PADDING.

</dd> <dt>

*MessageSeqNo* \[in\]
</dt> <dd>

The sequence number that the transport application assigned to the message. If the transport application does not maintain sequence numbers, this parameter must be zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.

| Return code                                                                                                    | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_BUFFER\_TOO\_SMALL**</dt> </dl>      | The output buffer is too small. For more information, see Remarks.                                                                                                                                                                 |
| <dl> <dt>**SEC\_E\_CONTEXT\_EXPIRED**</dt> </dl>        | The application is referencing a context that has already been closed. A properly written application should not receive this error.                                                                                               |
| <dl> <dt>**SEC\_E\_CRYPTO\_SYSTEM\_INVALID**</dt> </dl> | The [*cipher*](../secgloss/c-gly.md) chosen for the [*security context*](../secgloss/s-gly.md) is not supported.                                                                                                         |
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl>    | There is not enough memory available to complete the requested action.                                                                                                                                                             |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>         | A context handle that is not valid was specified in the *phContext* parameter.                                                                                                                                                     |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>          | No SECBUFFER\_DATA type buffer was found.                                                                                                                                                                                          |
| <dl> <dt>**SEC\_E\_QOP\_NOT\_SUPPORTED**</dt> </dl>     | Neither confidentiality nor [*integrity*](../secgloss/i-gly.md) are supported by the [*security context*](../secgloss/s-gly.md). |

## Remarks

The **EncryptMessage (Kerberos)** function encrypts a message based on the message and the [*session key*](../secgloss/s-gly.md) from a [*security context*](../secgloss/s-gly.md).

If the transport application created the [*security context*](../secgloss/s-gly.md) to support sequence detection and the caller provides a sequence number, the function includes this information with the encrypted message. Including this information protects against replay, insertion, and suppression of messages. The [*security package*](../secgloss/s-gly.md) incorporates the sequence number passed down from the transport application.

> [!Note]  
> These buffers must be supplied in the order shown.

| Buffer type                           | Description                                                                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| SECBUFFER\_STREAM\_HEADER<  | Used internally. No initialization required.                                                                       |
| SECBUFFER\_DATA            | Contains the [*plaintext*](../secgloss/s-gly.md) message to be encrypted. |
| SECBUFFER\_STREAM\_TRAILER | Used internally. No initialization required.                                                                        |
| SECBUFFER\_EMPTY           | Used internally. No initialization required. Size can be zero.                                                      |

For optimal performance, the *pMessage* structures should be allocated from contiguous memory.

**Windows XP:** This function was also known as **SealMessage**. Applications should now use **EncryptMessage (Kerberos)** only.

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**AcceptSecurityContext (Kerberos)**](acceptsecuritycontext--kerberos.md)
</dt> <dt>

[**DecryptMessage (Kerberos)**](decryptmessage--kerberos.md)
</dt> <dt>

[**InitializeSecurityContext (Kerberos)**](initializesecuritycontext--kerberos.md)
</dt> <dt>

[**QueryContextAttributes (Kerberos)**](querycontextattributes--kerberos.md)
</dt> <dt>

[**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
</dt> <dt>

[**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
</dt> </dl>
