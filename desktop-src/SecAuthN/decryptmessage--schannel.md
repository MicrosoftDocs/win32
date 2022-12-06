---
description: Decrypts a message by using Schannel.
ms.assetid: 5d7c8598-2d6b-4839-ae98-dff964bc962c
title: DecryptMessage (Schannel) function
ms.topic: reference
ms.date: 07/25/2019
---

# DecryptMessage (Schannel) function

The **DecryptMessage (Schannel)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](../secgloss/h-gly.md).


This function is also used with the Schannel [*security support provider*](../secgloss/s-gly.md#_SECURITY_SECURITY_SUPPORT_PROVIDER_GLY) (SSP) to signal a request from a message sender for a renegotiation (redo) of the connection attributes or for a shutdown of the connection.

> [!Note]  
> [**EncryptMessage (Schannel)**](encryptmessage--schannel.md) and **DecryptMessage (Schannel)** can be called at the same time from two different threads in a single [*security support provider interface*](../secgloss/s-gly.md#_SECURITY_SECURITY_SUPPORT_PROVIDER_INTERFACE_GLY) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.


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


A handle to the [*security context*](../secgloss/s-gly.md#_SECURITY_SECURITY_CONTEXT_GLY) to be used to decrypt the message.

*pMessage* \[in, out\]

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. One of these may be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

When using the Schannel SSP with contexts that are not connection oriented, on input, the structure must contain four [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. Exactly one buffer must be of type SECBUFFER\_DATA and contain an encrypted message, which is decrypted in place. The remaining buffers are used for output and must be of type SECBUFFER\_EMPTY. For connection-oriented contexts, a SECBUFFER\_DATA type buffer must be supplied, as noted for nonconnection-oriented contexts. Additionally, a second SECBUFFER\_TOKEN type buffer that contains a security token must also be supplied.

*MessageSeqNo* \[in\]

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

When using the Schannel SSP, this parameter must be set to zero. The Schannel SSP does not use sequence numbers.

*pfQOP* \[out\]

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

When using the Schannel SSP, this parameter is not used and should be set to **NULL**.

This parameter can be the following flag.


| Value | Meaning | 
|-------|---------|
| <span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl><dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt></dl> | The message was not encrypted, but a header or trailer was produced.<br /><blockquote>[!Note]<br />KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br /> | 


## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.

| Return code                     | Description                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| **SEC\_E\_INVALID\_HANDLE**     | A context handle that is not valid was specified in the *phContext* parameter. Used with the Schannel SSP.     |
| **SEC\_E\_INVALID\_TOKEN**      | The buffers are of the wrong type or no buffer of type SECBUFFER\_DATA was found. Used with the Schannel SSP.  |
| **SEC\_E\_MESSAGE\_ALTERED**    | The message has been altered. Used with the Schannel SSP.                                                      |
| **SEC\_E\_OUT\_OF\_SEQUENCE**   | The message was not received in the correct sequence.                                                          |
| **SEC\_I\_CONTEXT\_EXPIRED**    | The message sender has finished using the connection and has initiated a shutdown. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md). Used with the Schannel SSP. |
| **SEC\_I\_RENEGOTIATE**         | The remote party requires a new handshake sequence or the application has just initiated a shutdown. Return to the negotiation loop and call [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md) or [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md), pass SECBUFFER_EXTRA returned from DecryptMessage(). |


## Remarks

Sometimes an application will read data from the remote party, attempt to decrypt it by using **DecryptMessage (Schannel)**, and discover that **DecryptMessage (Schannel)** succeeded but the output buffers are empty. This is normal behavior, and applications must be able to deal with it.

When you use the Schannel SSP, the [**DecryptMessage (General)**](decryptmessage--general.md) function returns SEC\_I\_CONTEXT\_EXPIRED when the message sender has shut down the connection. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md).

If you are using TLS 1.0, you may need to call this function multiple times, adjusting the input buffer on each call, to decrypt a whole message.


The **DecryptMessage (Schannel)** function returns SEC\_I\_RENEGOTIATE when a post-handshake TLS protocol message other than application data is received. Once **DecryptMessage (Schannel)** function has returned SEC\_I\_RENEGOTIATE, any further EncryptMessage() and DecryptMessage() calls will fail with SEC_E_CONTEXT_EXPIRED.  An application handles this situation by calling [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md) (server side) or [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md) (client side) and passing SECBUFFER_EXTRA returned from DecryptMessage(). After this initial call returns a value, proceed as though your application were creating a new connection. Then the application can continue calling EncryptMessage() and DecryptMessage(). For more information, see [Creating an Schannel Security Context](creating-an-schannel-security-context.md).


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
- [**EncryptMessage (Schannel)**](encryptmessage--schannel.md)
- [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
- [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
