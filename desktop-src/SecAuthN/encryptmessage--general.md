---
Description: 'Encrypts a message to provide privacy.'
ms.assetid: '2e09f262-9c3e-4db2-9285-017f5e1810c7'
title: 'EncryptMessage (General) function'
---

# EncryptMessage (General) function

The **EncryptMessage (General)** function encrypts a message to provide [*privacy*](security.p_gly#-security-privacy-gly). **EncryptMessage (General)** allows an application to choose among [*cryptographic algorithms*](security.c_gly#-security-cryptographic-algorithm-gly) supported by the chosen mechanism. The **EncryptMessage (General)** function uses the [*security context*](security.s_gly#-security-security-context-gly) referenced by the context handle. Some packages do not have messages to be encrypted or decrypted but rather provide an integrity [*hash*](security.h_gly#-security-hash-gly) that can be checked.

When using the Digest [*security support provider*](security.s_gly#-security-security-support-provider-gly) (SSP), this function is available as a SASL mechanism only.

When using the Schannel SSP, this function encrypts messages by using a [*session key*](security.s_gly#-security-session-key-gly) negotiated with the remote party that will receive the message. The encryption algorithm is determined by the [cipher suite](cipher-suites-in-schannel.md) in use.

> [!Note]  
> **EncryptMessage (General)** and [**DecryptMessage (General)**](decryptmessage--general-.md) can be called at the same time from two different threads in a single [*Security Support Provider Interface*](security.s_gly#-security-security-support-provider-interface-gly) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

 

For information about using this function with a specific SSP, see the following topics.



| Topic                                                            | Description                                               |
|------------------------------------------------------------------|-----------------------------------------------------------|
| [**EncryptMessage (Digest)**](encryptmessage--digest-.md)       | Encrypts a message to provide privacy by using Digest.    |
| [**EncryptMessage (Kerberos)**](encryptmessage--kerberos-.md)   | Encrypts a message to provide privacy by using Kerberos.  |
| [**EncryptMessage (Negotiate)**](encryptmessage--negotiate-.md) | Encrypts a message to provide privacy by using Negotiate. |
| [**EncryptMessage (NTLM)**](encryptmessage--ntlm-.md)           | Encrypts a message to provide privacy by using NTLM.      |
| [**EncryptMessage (Schannel)**](encryptmessage--schannel-.md)   | Encrypts a message to provide privacy by using Schannel.  |



 

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*phContext* \[in\]
</dt> <dd>

A handle to the security [*context*](security.c_gly#-security-context-gly) to be used to encrypt the message.

</dd> <dt>

*fQOP* \[in\]
</dt> <dd>

Package-specific flags that indicate the quality of protection. A [*security package*](security.s_gly#-security-security-package-gly) can use this parameter to enable the selection of cryptographic algorithms.

When using the Digest SSP, this parameter must be set to zero.

This parameter can be one of the following flags.



<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Value</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td><span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl> <dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt> </dl></td><td>Produce a header or trailer but do not encrypt the message.<br/><blockquote>[!Note]<br />
KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br/></td></tr><tr class="even"><td><span id="SECQOP_WRAP_OOB_DATA"></span><span id="secqop_wrap_oob_data"></span><dl> <dt><strong>SECQOP_WRAP_OOB_DATA</strong></dt> </dl></td><td>Send an Schannel alert message. In this case, the <em>pMessage</em> parameter must contain a standard two-byte SSL/TLS event code. This value is supported only by the Schannel SSP.<br/></td></tr></tbody></table>



 

</dd> <dt>

*pMessage* \[in, out\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](secbufferdesc.md) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures. One of these can be of type SECBUFFER\_DATA. That buffer contains the message to be encrypted. The message is encrypted in place, overwriting the original contents of the structure.

The function does not process buffers with the SECBUFFER\_READONLY attribute.

The length of the [**SecBuffer**](secbuffer.md) structure that contains the message must be no greater than **cbMaximumMessage**, which is obtained from the [**QueryContextAttributes (General)**](querycontextattributes--general-.md) (SECPKG\_ATTR\_STREAM\_SIZES) function.

When using the Digest SSP, there must be a second buffer of type SECBUFFER\_PADDING or SEC\_BUFFER\_DATA to hold [*signature*](security.d_gly#-security-digital-signature-gly) information. To get the size of the output buffer, call the [**QueryContextAttributes (General)**](querycontextattributes--general-.md) function and specify SECPKG\_ATTR\_SIZES. The function will return a [**SecPkgContext\_Sizes**](secpkgcontext-sizes.md) structure. The size of the output buffer is the sum of the values in the **cbMaxSignature** and **cbBlockSize** members.

Applications that do not use SSL must supply a [**SecBuffer**](secbuffer.md) of type SECBUFFER\_PADDING.

</dd> <dt>

*MessageSeqNo* \[in\]
</dt> <dd>

The sequence number that the transport application assigned to the message. If the transport application does not maintain sequence numbers, this parameter must be zero.

When using the Digest SSP, this parameter must be set to zero. The Digest SSP manages sequence numbering internally.

When using the Schannel SSP, this parameter must be set to zero. The Schannel SSP does not use sequence numbers.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_BUFFER\_TOO\_SMALL**</dt> </dl>      | The output buffer is too small. For more information, see Remarks.<br/>                                                                                                                                                                 |
| <dl> <dt>**SEC\_E\_CONTEXT\_EXPIRED**</dt> </dl>        | The application is referencing a context that has already been closed. A properly written application should not receive this error.<br/>                                                                                               |
| <dl> <dt>**SEC\_E\_CRYPTO\_SYSTEM\_INVALID**</dt> </dl> | The [*cipher*](security.c_gly#-security-cipher-gly) chosen for the security context is not supported.<br/>                                                                                                         |
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl>    | There is not enough memory available to complete the requested action.<br/>                                                                                                                                                             |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>         | A context handle that is not valid was specified in the *phContext* parameter.<br/>                                                                                                                                                     |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>          | No SECBUFFER\_DATA type buffer was found.<br/>                                                                                                                                                                                          |
| <dl> <dt>**SEC\_E\_QOP\_NOT\_SUPPORTED**</dt> </dl>     | Neither confidentiality nor [*integrity*](security.i_gly#-security-integrity-gly) are supported by the [*security context*](security.s_gly#-security-security-context-gly).<br/> |



 

## Remarks

The **EncryptMessage (General)** function encrypts a message based on the message and the [*session key*](security.s_gly#-security-session-key-gly) from a [*security context*](security.s_gly#-security-security-context-gly).

If the transport application created the security context to support sequence detection and the caller provides a sequence number, the function includes this information with the encrypted message. Including this information protects against replay, insertion, and suppression of messages. The [*security package*](security.s_gly#-security-security-package-gly) incorporates the sequence number passed down from the transport application.

When you use the Digest SSP, get the size of the output buffer by calling the [**QueryContextAttributes (General)**](querycontextattributes--general-.md) function and specifying SECPKG\_ATTR\_SIZES. The function will return a [**SecPkgContext\_Sizes**](secpkgcontext-sizes.md) structure. The size of the output buffer is the sum of the values in the **cbMaxSignature** and **cbBlockSize** members.

When used with the Schannel SSP, the *pMessage* parameter must contain a [**SecBufferDesc**](secbufferdesc.md) structure with the following buffers.

> [!Note]  
> These buffers must be supplied in the order shown.

 



| Buffer type                | Description                                                                                                         |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| SECBUFFER\_STREAM\_HEADER  | Used internally. No initialization required.                                                                        |
| SECBUFFER\_DATA            | Contains the [*plaintext*](security.p_gly#-security-plaintext-gly) message to be encrypted. |
| SECBUFFER\_STREAM\_TRAILER | Used internally. No initialization required.                                                                        |
| SECBUFFER\_EMPTY           | Used internally. No initialization required. Size can be zero.                                                      |



 

When you use the Schannel SSP, determine the maximum size of each of the buffers by calling the [**QueryContextAttributes (General)**](querycontextattributes--general-.md) function and specifying the SECPKG\_ATTR\_STREAM\_SIZES attribute. This function returns a [**SecPkgContext\_StreamSizes**](secpkgcontext-streamsizes.md) structure whose members contain the maximum sizes for the header (**cbHeader** member), message (**cbMaximumMessage** member) and trailer (**cbTrailer** member) buffers.

For optimal performance, the *pMessage* structures should be allocated from contiguous memory.

**Windows XP/2000:** This function was also known as **SealMessage**. Applications should now use **EncryptMessage (General)** only.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**AcceptSecurityContext (General)**](acceptsecuritycontext--general-.md)
</dt> <dt>

[**DecryptMessage (General)**](decryptmessage--general-.md)
</dt> <dt>

[**InitializeSecurityContext (General)**](initializesecuritycontext--general-.md)
</dt> <dt>

[**QueryContextAttributes (General)**](querycontextattributes--general-.md)
</dt> <dt>

[**SecBuffer**](secbuffer.md)
</dt> <dt>

[**SecBufferDesc**](secbufferdesc.md)
</dt> </dl>

 

 




