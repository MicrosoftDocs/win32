---
Description: 'Encrypts a message to provide privacy by using Schannel.'
ms.assetid: 'b02b38bd-f3dd-4bf8-a36e-44ff9fbbe550'
title: 'EncryptMessage (Schannel) function'
ms.topic: article
ms.date: 07/25/2019
---

# EncryptMessage (Schannel) function

The **EncryptMessage (Schannel)** function encrypts a message to provide [*privacy*](https://docs.microsoft.com/en-us/windows/win32/secgloss/p-gly). **EncryptMessage (Schannel)** allows an application to choose among [*cryptographic algorithms*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly) supported by the chosen mechanism. The **EncryptMessage (Schannel)** function uses the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) referenced by the context handle. Some packages do not have messages to be encrypted or decrypted but rather provide an integrity [*hash*](https://docs.microsoft.com/en-us/windows/win32/secgloss/h-gly) that can be checked.

When using the Schannel SSP, this function encrypts messages by using a [*session key*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) negotiated with the remote party that will receive the message. The encryption algorithm is determined by the [[*cipher*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly) suite]([*cipher*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly)-suites-in-schannel.md) in use.

> [!Note]  
> **EncryptMessage (Schannel)** and [**DecryptMessage (Schannel)**](decryptmessage--schannel.md) can be called at the same time from two different threads in a single [*security support provider interface*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

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

| Value                                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECQOP_WRAP_OOB_DATA"></span><span id="secqop_wrap_oob_data"></span><dl> <dt>**SECQOP\_WRAP\_OOB\_DATA**</dt> </dl> | Send an Schannel alert message. In this case, the *pMessage* parameter must contain a standard two-byte SSL/TLS event code. This value is supported only by the Schannel SSP.<br/> For example, beginning with Windows Vista, the "server hello" message sent by the server during the re-authentication protocol must be encrypted as a TLS alert.<br/> |

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures. One of these can be of type SECBUFFER\_DATA. That buffer contains the message to be encrypted. The message is encrypted in place, overwriting the original contents of the structure.

The function does not process buffers with the SECBUFFER\_READONLY attribute.

The length of the [**SecBuffer**](secbuffer.md) structure that contains the message must be no greater than **cbMaximumMessage**, which is obtained from the [**QueryContextAttributes (Schannel)**](querycontextattributes--schannel.md) (SECPKG\_ATTR\_STREAM\_SIZES) function.

*MessageSeqNo* \[in\]

The sequence number that the transport application assigned to the message. If the transport application does not maintain sequence numbers, this parameter must be zero.

When using the Schannel SSP, this parameter must be set to zero. The Schannel SSP does not use sequence numbers.

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.

| Return code                                                                                                    | Description                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_BUFFER\_TOO\_SMALL**</dt> </dl>      | The output buffer is too small. For more information, see Remarks.<br/>                                                                               |
| <dl> <dt>**SEC\_E\_CONTEXT\_EXPIRED**</dt> </dl>        | The application is referencing a context that has already been closed. A properly written application should not receive this error.<br/>             |
| <dl> <dt>**SEC\_E\_CRYPTO\_SYSTEM\_INVALID**</dt> </dl> | The [*cipher*](https://docs.microsoft.com/en-us/windows/win32/secgloss/c-gly) chosen for the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) is not supported.<br/>                       |
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl>    | There is not enough memory available to complete the requested action.<br/>                                                                           |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>         | A context handle that is not valid was specified in the *phContext* parameter.<br/>                                                                   |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>          | No SECBUFFER\_DATA type buffer was found.<br/>                                                                                                        |
| <dl> <dt>**SEC\_E\_QOP\_NOT\_SUPPORTED**</dt> </dl>     | Neither confidentiality nor [*integrity*](https://docs.microsoft.com/en-us/windows/win32/secgloss/i-gly) are supported by the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly).<br/> |

## Remarks

The **EncryptMessage (Schannel)** function encrypts a message based on the message and the [*session key*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) from a [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly).

If the transport application created the [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) to support sequence detection and the caller provides a sequence number, the function includes this information with the encrypted message. Including this information protects against replay, insertion, and suppression of messages. The [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) incorporates the sequence number passed down from the transport application.

When used with the Schannel SSP, the *pMessage* parameter must contain a [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea) structure with the following buffers.

> [!Note]  
> These buffers must be supplied in the order shown.

| Buffer type                | Description                                                                                                         |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| SECBUFFER\_STREAM\_HEADER  | Used internally. No initialization required.                                                                        |
| SECBUFFER\_DATA            | Contains the [*plaintext*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) message to be encrypted. |
| SECBUFFER\_STREAM\_TRAILER | Used internally. No initialization required.                                                                        |
| SECBUFFER\_EMPTY           | Used internally. No initialization required. Size can be zero.                                                      |

When you use the Schannel SSP, determine the maximum size of each of the buffers by calling the [**QueryContextAttributes (Schannel)**](querycontextattributes--schannel.md) function and specifying the SECPKG\_ATTR\_STREAM\_SIZES attribute. This function returns a [**SecPkgContext\_StreamSizes**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/ns-sspi-_secpkgcontext_streamsizes) structure whose members contain the maximum sizes for the header (**cbHeader** member), message (**cbMaximumMessage** member) and trailer (**cbTrailer** member) buffers.

For optimal performance, the *pMessage* structures should be allocated from contiguous memory.

**Windows XP/2000:** This function was also known as **SealMessage**. Applications should now use **EncryptMessage (Schannel)** only.

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
- [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md)
- [**DecryptMessage (Schannel)**](decryptmessage--schannel.md)
- [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md)
- [**QueryContextAttributes (Schannel)**](querycontextattributes--schannel.md)
- [**SecBuffer**](secbuffer.md)
- [**SecBufferDesc**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-deletesecuritypackagea)
