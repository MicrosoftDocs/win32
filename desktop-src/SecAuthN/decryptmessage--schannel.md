---
description: Learn how to use the DecryptMessage (Schannel) function to decrypt messages securely with the Schannel SSP. Includes syntax, parameters, and error handling.
ms.assetid: 5d7c8598-2d6b-4839-ae98-dff964bc962c
title: DecryptMessage (Schannel) function
ms.topic: reference
ms.date: 11/06/2025
---

# DecryptMessage (Schannel) function

The **DecryptMessage (Schannel)** function decrypts a message. Some packages don't encrypt and decrypt messages but rather perform and check an integrity [hash](../secgloss/h-gly.md).

Use this function with the Schannel [security support provider](../secgloss/s-gly.md#_SECURITY_SECURITY_SUPPORT_PROVIDER_GLY) (SSP) to signal a request from a message sender for a renegotiation (redo) of the connection attributes or for a shutdown of the connection.

> [!NOTE]  
> You can call [EncryptMessage (Schannel)](encryptmessage--schannel.md) and **DecryptMessage (Schannel)** at the same time from two different threads in a single [security support provider interface](../secgloss/s-gly.md#_SECURITY_SECURITY_SUPPORT_PROVIDER_INTERFACE_GLY) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

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

A handle to the [security context](../secgloss/s-gly.md#_SECURITY_SECURITY_CONTEXT_GLY) to use for decrypting the message.

*pMessage* \[in, out\]

A pointer to a [SecBufferDesc](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. On input, the structure references one or more [SecBuffer](/windows/win32/api/sspi/ns-sspi-secbuffer) structures. One of these buffers can be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The function decrypts the encrypted message in place, overwriting the original contents of its buffer.

When you use the Schannel SSP with contexts that aren't connection oriented, the structure must contain four [SecBuffer](/windows/win32/api/sspi/ns-sspi-secbuffer) structures on input. Exactly one buffer must be of type SECBUFFER\_DATA and contain an encrypted message, which the function decrypts in place. The remaining buffers are used for output and must be of type SECBUFFER\_EMPTY. For connection-oriented contexts, you must supply a SECBUFFER\_DATA type buffer, as noted for nonconnection-oriented contexts. Additionally, you must supply a second SECBUFFER\_TOKEN type buffer that contains a security token.

*MessageSeqNo* \[in\]

The sequence number expected by the transport application, if any. If the transport application doesn't maintain sequence numbers, set this parameter to zero.

When you use the Schannel SSP, set this parameter to zero. The Schannel SSP doesn't use sequence numbers.

*pfQOP* \[out\]

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

When you use the Schannel SSP, don't use this parameter. Set it to **NULL**.

This parameter can be the following flag.

| Value | Meaning |
|-------|---------|
| **SECQOP_WRAP_NO_ENCRYPT** | The message wasn't encrypted, but the function produced a header or trailer.<br> **Note:** KERB_WRAP_NO_ENCRYPT has the same value and the same meaning. |

## Return value

If the function verifies that the message is received in the correct sequence, it returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.

| Return code                     | Description |
|---------------------------------|-------------|
| **SEC\_E\_INVALID\_HANDLE**     | The *phContext* parameter specifies an invalid context handle. Used with the Schannel SSP.     |
| **SEC\_E\_INVALID\_TOKEN**      | The buffers are of the wrong type or no buffer of type SECBUFFER\_DATA is found. Used with the Schannel SSP.  |
| **SEC\_E\_MESSAGE\_ALTERED**    | The message is altered. Used with the Schannel SSP.                                                      |
| **SEC\_E\_OUT\_OF\_SEQUENCE**   | The message isn't received in the correct sequence.                                                          |
| **SEC\_I\_CONTEXT\_EXPIRED**    | The message sender finishes using the connection and initiates a shutdown. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md). Used with the Schannel SSP. |
| **SEC\_I\_RENEGOTIATE**         | The remote party requires a new handshake sequence or the application initiates a shutdown. Return to the negotiation loop and call [AcceptSecurityContext (Schannel)](acceptsecuritycontext--schannel.md) or [InitializeSecurityContext (Schannel)](initializesecuritycontext--schannel.md), passing the same buffer as modified by DecryptMessage, ensuring that the SecBuffer type is set to SECBUFFER_TOKEN. |

## Remarks

Sometimes an application reads data from the remote party, attempts to decrypt it by using **DecryptMessage (Schannel)**, and discovers that **DecryptMessage (Schannel)** succeeds but the output buffers are empty. This behavior is normal, and applications must be able to handle it.

When you use the Schannel SSP, the [DecryptMessage (General)](decryptmessage--general.md) function returns SEC\_I\_CONTEXT\_EXPIRED when the message sender shuts down the connection. For information about initiating or recognizing a shutdown, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md).

If you're using TLS 1.0, you might need to call this function multiple times, adjusting the input buffer on each call, to decrypt a whole message.

The **DecryptMessage (Schannel)** function returns SEC\_I\_RENEGOTIATE when it receives a post-handshake TLS protocol message other than application data. Once **DecryptMessage (Schannel)** returns SEC\_I\_RENEGOTIATE, any further EncryptMessage() and DecryptMessage() calls fail with SEC\_E\_CONTEXT\_EXPIRED. An application handles this situation by calling [AcceptSecurityContext (Schannel)](acceptsecuritycontext--schannel.md) (server side) or [InitializeSecurityContext (Schannel)](initializesecuritycontext--schannel.md) (client side) and passing the same buffer as modified by **DecryptMessage**, ensuring that the `SecBuffer` type is set to `SECBUFFER_TOKEN`. Note that **DecryptMessage** doesn't always return an `SECBUFFER_EXTRA` buffer when `SEC_I_RENEGOTIATE` is returned. After this initial call returns a value, proceed as though your application is creating a new connection. Then the application can continue calling EncryptMessage() and DecryptMessage(). For more information, see [Creating an Schannel Security Context](creating-an-schannel-security-context.md).

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\]          |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header                   | Sspi.h (include Security.h)               |
| Library                  | Secur32.lib                               |
| DLL                      | Secur32.dll                               |

## Related content

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [EncryptMessage (Schannel)](encryptmessage--schannel.md)
- [SecBuffer](/windows/win32/api/sspi/ns-sspi-secbuffer)
