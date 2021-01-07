---
description: Decrypts a message.
ms.assetid: ea271d0c-9167-41c5-8919-09611206fc71
title: DecryptMessage (General) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---

# DecryptMessage (General) function

The **DecryptMessage (General)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](../secgloss/h-gly.md).

The Digest [*security support provider*](../secgloss/s-gly.md) (SSP) provides encryption and decryption confidentiality for messages exchanged between client and server as a SASL mechanism only.

This function is also used with the Schannel SSP to signal a request from a message sender for a renegotiation (redo) of the connection attributes or for a shutdown of the connection.

> [!Note]  
> [**EncryptMessage (General)**](encryptmessage--general.md) and **DecryptMessage (General)** can be called at the same time from two different threads in a single [*security support provider interface*](../secgloss/s-gly.md) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

 

For information about using this function with a specific SSP, see the following topics.



| Topic                                                            | Description                            |
|------------------------------------------------------------------|----------------------------------------|
| [**DecryptMessage (Digest)**](decryptmessage--digest.md)       | Decrypts a message by using Digest.    |
| [**DecryptMessage (Kerberos)**](decryptmessage--kerberos.md)   | Decrypts a message by using Kerberos.  |
| [**DecryptMessage (Negotiate)**](decryptmessage--negotiate.md) | Decrypts a message by using Negotiate. |
| [**DecryptMessage (NTLM)**](decryptmessage--ntlm.md)           | Decrypts a message by using NTLM.      |
| [**DecryptMessage (Schannel)**](decryptmessage--schannel.md)   | Decrypts a message by using Schannel.  |



 

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

<dl> <dt>

*phContext* \[in\]
</dt> <dd>

A handle to the [*security context*](../secgloss/s-gly.md) to be used to decrypt the message.

</dd> <dt>

*pMessage* \[in, out\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. One of these may be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

When using the Digest SSP, on input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. One of these must be of type SECBUFFER\_DATA or SECBUFFER\_STREAM, and it must contain the encrypted message.

When using the Schannel SSP with contexts that are not connection oriented, on input, the structure must contain four [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. Exactly one buffer must be of type SECBUFFER\_DATA and contain an encrypted message, which is decrypted in place. The remaining buffers are used for output and must be of type SECBUFFER\_EMPTY. For connection-oriented contexts, a SECBUFFER\_DATA type buffer must be supplied, as noted for nonconnection-oriented contexts. Additionally, a second SECBUFFER\_TOKEN type buffer that contains a security token must also be supplied.

</dd> <dt>

*MessageSeqNo* \[in\]
</dt> <dd>

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

When using the Digest SSP, this parameter must be set to zero. The Digest SSP manages sequence numbering internally.

When using the Schannel SSP, this parameter must be set to zero. The Schannel SSP does not use sequence numbers.

</dd> <dt>

*pfQOP* \[out\]
</dt> <dd>

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

When using the Schannel SSP, this parameter is not used and should be set to **NULL**.

This parameter can be one of the following flags.



<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Value</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td><span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl> <dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt> </dl></td><td>The message was not encrypted, but a header or trailer was produced.<br/><blockquote>[!Note]<br />
KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br/></td></tr><tr class="even"><td><span id="SIGN_ONLY_"></span><span id="sign_only_"></span><dl> <dt><strong>SIGN_ONLY</strong> </dt> </dl></td><td>When using the Digest SSP, use this flag when the [*security context*](../secgloss/s-gly.md) is set to verify the [*signature*](../secgloss/s-gly.md) only. For more information, see [Quality of Protection](quality-of-protection.md).<br/></td></tr></tbody></table>



 

</dd> </dl>

## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_BUFFER\_TOO\_SMALL**</dt> </dl>      | The message buffer is too small. Used with the Digest SSP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**SEC\_E\_CRYPTO\_SYSTEM\_INVALID**</dt> </dl> | The [*cipher*](../secgloss/c-gly.md) chosen for the [*security context*](../secgloss/s-gly.md) is not supported. Used with the Digest SSP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**SEC\_E\_INCOMPLETE\_MESSAGE**</dt> </dl>     | The data in the input buffer is incomplete. The application needs to read more data from the server and call [**DecryptMessage (General)**](decryptmessage--general.md) again.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>         | A context handle that is not valid was specified in the *phContext* parameter. Used with the Digest and Schannel SSPs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>          | The buffers are of the wrong type or no buffer of type SECBUFFER\_DATA was found. Used with the Schannel SSP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**SEC\_E\_MESSAGE\_ALTERED**</dt> </dl>        | The message has been altered. Used with the Digest and Schannel SSPs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**SEC\_E\_OUT\_OF\_SEQUENCE**</dt> </dl>       | The message was not received in the correct sequence.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**SEC\_E\_QOP\_NOT\_SUPPORTED**</dt> </dl>     | Neither confidentiality nor [*integrity*](../secgloss/i-gly.md) are supported by the [*security context*](../secgloss/s-gly.md). Used with the Digest SSP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**SEC\_I\_CONTEXT\_EXPIRED**</dt> </dl>        | The message sender has finished using the connection and has initiated a shutdown. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md). Used with the Schannel SSP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**SEC\_I\_RENEGOTIATE**</dt> </dl>             | The remote party requires a new handshake sequence or the application has just initiated a shutdown. Return to the negotiation loop and call [**AcceptSecurityContext (General)**](acceptsecuritycontext--general.md) or [**InitializeSecurityContext (General)**](initializesecuritycontext--general.md), passing empty input buffers. <br/> If the function returns a buffer of type **SEC\_BUFFER\_EXTRA**, this should be passed to the [**AcceptSecurityContext (General)**](acceptsecuritycontext--general.md) function as an input buffer.<br/> Used with the Schannel SSP.<br/> Renegotiation is not supported for Schannel kernel mode. The caller should either ignore this return value or shut down the connection. If the value is ignored, either the client or the server might shut down the connection as a result.<br/> |



 

## Remarks

When you use the Schannel SSP, the **DecryptMessage (General)** function returns SEC\_I\_CONTEXT\_EXPIRED when the message sender has shut down the connection. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md).

When you use the Schannel SSP, **DecryptMessage (General)** returns SEC\_I\_RENEGOTIATE when the message sender wants to renegotiate the connection ([*security context*](../secgloss/s-gly.md)). An application handles a requested renegotiation by calling [**AcceptSecurityContext (General)**](acceptsecuritycontext--general.md) (server side) or [**InitializeSecurityContext (General)**](initializesecuritycontext--general.md) (client side) and passing in empty input buffers. After this initial call returns a value, proceed as though your application were creating a new connection. For more information, see [Creating an Schannel [*security context*](../secgloss/s-gly.md)](creating-an-schannel-security-context.md).

For information about interoperating with GSSAPI, see [SSPI/Kerberos Interoperability with GSSAPI](sspi-kerberos-interoperability-with-gssapi.md).

## Requirements



| Requirement | Value |
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

[**EncryptMessage (General)**](encryptmessage--general.md)
</dt> <dt>

[**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
</dt> <dt>

[**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
</dt> </dl>

 

 
