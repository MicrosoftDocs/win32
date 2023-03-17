---
description: Initiates the client side, outbound security context from a credential handle by using the Kerberos constrained delegation.
ms.assetid: b5c968dc-9343-44ed-acbc-a89c58c14e4a
title: InitializeSecurityContext (Kerberos) function (Sspi.h)
ms.topic: reference
ms.date: 03/17/2023
---

# InitializeSecurityContext (Kerberos) function

The **InitializeSecurityContext (Kerberos)** function initiates the client side, outbound [security context](../secgloss/s-gly.md) from a credential handle. The function is used to build a [security context](../secgloss/s-gly.md) between the client application and a remote peer. **InitializeSecurityContext (Kerberos)** returns a token that the client must pass to the remote peer, which the peer in turn submits to the local security implementation through the [AcceptSecurityContext (Kerberos)](acceptsecuritycontext--kerberos.md) call. The token generated should be considered opaque by all callers.

Typically, the **InitializeSecurityContext (Kerberos)** function is called in a loop until a sufficient [security context](../secgloss/s-gly.md) is established.

## Syntax

```C++
SECURITY_STATUS SEC_Entry InitializeSecurityContext(
  _In_opt_    PCredHandle    phCredential,
  _In_opt_    PCtxtHandle    phContext,
  _In_        SEC_CHAR       *pszTargetName,
  _In_        ULONG          fContextReq,
  _In_        ULONG          Reserved1,
  _In_        ULONG          TargetDataRep,
  _In_opt_    PSecBufferDesc pInput,
  _In_        ULONG          Reserved2,
  _Inout_opt_ PCtxtHandle    phNewContext,
  _Inout_opt_ PSecBufferDesc pOutput,
  _Out_       PULONG         pfContextAttr,
  _Out_opt_   PTimeStamp     ptsExpiry
);
```

## Parameters

*phCredential* `[in, optional]`

A handle to the credentials returned by [AcquireCredentialsHandle (Kerberos)](acquirecredentialshandle--kerberos.md). This handle is used to build the [*security context*](../secgloss/s-gly.md). The **InitializeSecurityContext (Kerberos)** function requires at least OUTBOUND credentials.

*phContext* `[in, optional]`

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (Kerberos)**, this pointer is `NULL`. On the second call, this parameter is a pointer to the handle to the partially formed context returned in the *phNewContext* parameter by the first call.

*pszTargetName* `[in]`

A pointer to a null-terminated string that indicates the service principal name (SPN) or the [security context](../secgloss/s-gly.md) of the destination server.

Use a fully qualified target name because short names are not supported across forests.

*fContextReq* `[in]`

Bit flags that indicate requests for the context. Not all packages can support all requirements. Flags used for this parameter are prefixed with ISC\_REQ\_, for example, ISC\_REQ\_DELEGATE. This parameter can be one or more of the following attributes flags.

| Value | Meaning |
|-------|---------|
| **ISC_REQ_ALLOCATE_MEMORY** | The [security package](../secgloss/s-gly.md) allocates output buffers for you. When you have finished using the output buffers, free them by calling the [FreeContextBuffer](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function. |
| **ISC_REQ_CONFIDENTIALITY** | Encrypt messages by using the [EncryptMessage](encryptmessage--general.md) function. |
| **ISC_REQ_CONNECTION** | The [security context](../secgloss/s-gly.md) will not handle formatting messages. This value is the default. |
| **ISC_REQ_DELEGATE** | The server can use the context to authenticate to other servers as the client. The ISC_REQ_MUTUAL_AUTH flag must be set for this flag to work. Valid for Kerberos. Ignore this flag for [constrained delegation](../secgloss/c-gly.md). |
| **ISC_REQ_EXTENDED_ERROR** | When errors occur, the remote party will be notified. |
| **ISC_REQ_INTEGRITY** | Sign messages and verify signatures by using the [EncryptMessage](encryptmessage--general.md) and [MakeSignature](/windows/win32/api/sspi/nf-sspi-makesignature) functions. |
| **ISC_REQ_MUTUAL_AUTH** | The mutual authentication policy of the service will be satisfied.<br/> **CAUTION:** This does not necessarily mean that mutual authentication is performed, only that the authentication policy of the service is satisfied. To ensure that mutual authentication is performed, call the [QueryContextAttributes (Kerberos)](querycontextattributes--kerberos.md) function. |
| **ISC_REQ_NO_INTEGRITY** | If this flag is set, the **ISC_REQ_INTEGRITY** flag is ignored. |
| **ISC_REQ_REPLAY_DETECT** | Detect replayed messages that have been encoded by using the [EncryptMessage](encryptmessage--general.md) or [MakeSignature](/windows/win32/api/sspi/nf-sspi-makesignature) functions. |
| **ISC_REQ_SEQUENCE_DETECT** | Detect messages received out of sequence. |
| **ISC_REQ_STREAM** | Support a stream-oriented connection. |
| **ISC_REQ_USE_SESSION_KEY** | A new [session key](../secgloss/s-gly.md) must be negotiated. |

The requested attributes may not be supported by the client. For more information, see the *pfContextAttr* parameter.

For further descriptions of the various attributes, see [Context Requirements](context-requirements.md).

*Reserved1* `[in]`

This parameter is reserved and must be set to zero.

*TargetDataRep* `[in]`

The data representation, such as byte ordering, on the target. This parameter can be either SECURITY\_NATIVE\_DREP or SECURITY\_NETWORK\_DREP.

*pInput* `[in, optional]`

A pointer to a [SecBufferDesc](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure that contains pointers to the buffers supplied as input to the package. Unless the client context was initiated by the server, the value of this parameter must be `NULL` on the first call to the function. On subsequent calls to the function or when the client context was initiated by the server, the value of this parameter is a pointer to a buffer allocated with enough memory to hold the token returned by the remote computer.

*Reserved2* `[in]`

This parameter is reserved and must be set to zero.

*phNewContext* `[in, out, optional]`

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (Kerberos)**, this pointer receives the new context handle. On the second call, *phNewContext* can be the same as the handle specified in the *phContext* parameter. *phNewContext* should never be `NULL`.

*pOutput* `[in, out, optional]`

A pointer to a [SecBufferDesc](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure that contains pointers to the [SecBuffer](/windows/win32/api/sspi/ns-sspi-secbuffer) structure that receives the output data. If a buffer was typed as SEC\_READWRITE in the input, it will be there on output. The system will allocate a buffer for the security token if requested (through ISC\_REQ\_ALLOCATE\_MEMORY) and fill in the address in the buffer descriptor for the security token.

*pfContextAttr* `[out]`

A pointer to a variable to receive a set of bit flags that indicate the [attributes](../secgloss/a-gly.md#_security_attribute_gly) of the established context. For a description of the various attributes, see [Context Requirements](context-requirements.md).

Flags used for this parameter are prefixed with ISC\_RET, such as ISC\_RET\_DELEGATE. For a list of valid values, see the *fContextReq* parameter.

Do not check for security-related attributes until the final function call returns successfully. Attribute flags that are not related to security, such as the ASC\_RET\_ALLOCATED\_MEMORY flag, can be checked before the final return.

> [!NOTE]
> Particular context attributes can change during negotiation with a remote peer.

*ptsExpiry* `[out, optional]`

A pointer to a [TimeStamp](timestamp.md) structure that receives the expiration time of the context. We recommend that the [security package](../secgloss/s-gly.md) always return this value in local time. Because this parameter is optional, `NULL` should be passed for short-lived clients.

## Return value

If the function succeeds, the function returns one of the following success codes.

| Return code | Description |
|--------|--------|
| **SEC\_E\_OK** | The [security context](../secgloss/s-gly.md) was successfully initialized. There is no need for another [InitializeSecurityContext (Kerberos)](initializesecuritycontext--kerberos.md) call. If the function returns an output token, that is, if the SECBUFFER\_TOKEN in *pOutput* is of nonzero length, that token must be sent to the server. |
| **SEC\_I\_COMPLETE\_AND\_CONTINUE** | The client must call [CompleteAuthToken](/windows/win32/api/sspi/nf-sspi-completeauthtoken) and then pass the output to the server. The client then waits for a returned token and passes it, in another call, to [InitializeSecurityContext (Kerberos)](initializesecuritycontext--kerberos.md). |
| **SEC\_I\_COMPLETE\_NEEDED** | The client must finish building the message and then call the [CompleteAuthToken](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function. |
| **SEC\_I\_CONTINUE\_NEEDED** | The client must send the output token to the server and wait for a return token. The returned token is then passed in another call to [InitializeSecurityContext (Kerberos)](initializesecuritycontext--kerberos.md). The output token can be empty. |
| **SEC\_I\_INCOMPLETE\_CREDENTIALS** | Use with Schannel. The server has requested client authentication, and the supplied credentials either do not include a certificate or the certificate was not issued by a certification authority (CA) trusted by the server. For more information, see [Remarks](#remarks). |

If the function fails, the function returns one of the following error codes.

| Return code | Description |
|--------|--------|
| **SEC\_E\_INSUFFICIENT\_MEMORY** | There is not enough memory available to complete the requested action. |
| **SEC\_E\_INTERNAL\_ERROR** | An error occurred that did not map to an SSPI error code. |
| **SEC\_E\_INVALID\_HANDLE** | The handle passed to the function is not valid. |
| **SEC\_E\_INVALID\_TOKEN** | The error is due to a malformed input token, such as a token corrupted in transit, a token of incorrect size, or a token passed into the wrong [*constrained delegation*](../secgloss/s-gly.md). Passing a token to the wrong package can happen if the client and server did not negotiate the proper [*constrained delegation*](../secgloss/s-gly.md). |
| **SEC\_E\_LOGON\_DENIED** | The logon failed. |
| **SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY** | No authority could be contacted for authentication. The domain name of the authenticating party could be wrong, the domain could be unreachable, or there might have been a trust relationship failure. |
| **SEC\_E\_NO\_CREDENTIALS** | No credentials are available in the [*constrained delegation*](../secgloss/s-gly.md). |
| **SEC\_E\_TARGET\_UNKNOWN** | The target was not recognized. |
| **SEC\_E\_UNSUPPORTED\_FUNCTION** | A context attribute flag that is not valid (ISC\_REQ\_DELEGATE or ISC\_REQ\_PROMPT\_FOR\_CREDS) was specified in the *fContextReq* parameter. |
| **SEC\_E\_WRONG\_PRINCIPAL** | The principal that received the authentication request is not the same as the one passed into the *pszTargetName* parameter. This indicates a failure in mutual authentication. |

## Remarks

The caller is responsible for determining whether the final context attributes are sufficient. If, for example, confidentiality was requested, but could not be established, some applications may choose to shut down the connection immediately.

If attributes of the [security context](../secgloss/s-gly.md) are not sufficient, the client must free the partially created context by calling the [DeleteSecurityContext](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function.

The **InitializeSecurityContext (Kerberos)** function is used by a client to initialize an outbound context.

For a two-leg [security context](../secgloss/s-gly.md), the calling sequence is as follows:

1. The client calls the function with *phContext* set to `NULL` and fills in the buffer descriptor with the input message.
2. The [security package](../secgloss/s-gly.md) examines the parameters and constructs an opaque token, placing it in the TOKEN element in the buffer array. If the *fContextReq* parameter includes the ISC\_REQ\_ALLOCATE\_MEMORY flag, the [security package](../secgloss/s-gly.md) allocates the memory and returns the pointer in the TOKEN element.
3. The client sends the token returned in the *pOutput* buffer to the target server. The server then passes the token as an input argument in a call to the [AcceptSecurityContext (Kerberos)](acceptsecuritycontext--kerberos.md) function.
4. [AcceptSecurityContext (Kerberos)](acceptsecuritycontext--kerberos.md) may return a token, which the server sends to the client for a second call to **InitializeSecurityContext (Kerberos)** if the first call returned SEC\_I\_CONTINUE\_NEEDED.

For multiple-leg [*security context*](../secgloss/s-gly.md)s, such as mutual authentication, the calling sequence is as follows:

1. The client calls the function as described earlier, but the package returns the SEC\_I\_CONTINUE\_NEEDED success code.
2. The client sends the output token to the server and waits for the server's reply.
3. Upon receipt of the server's response, the client calls **InitializeSecurityContext (Kerberos)** again, with *phContext* set to the handle that was returned from the last call. The token received from the server is supplied in the *pInput* parameter.

If the server has successfully responded, the [*security package*](../secgloss/s-gly.md) returns SEC\_E\_OK and a secure session is established.

If the function returns one of the error responses, the server's response is not accepted, and the session is not established.

If the function returns SEC\_I\_CONTINUE\_NEEDED, SEC\_I\_COMPLETE\_NEEDED, or SEC\_I\_COMPLETE\_AND\_CONTINUE, steps 2 and 3 are repeated.

To initialize a [security context](../secgloss/s-gly.md), more than one call to this function may be required, depending on the underlying authentication mechanism as well as the choices specified in the *fContextReq* parameter.

The *fContextReq* and *pfContextAttributes* parameters are bitmasks that represent various context attributes. For a description of the various attributes, see [Context Requirements](context-requirements.md). The *pfContextAttributes* parameter is valid on any successful return, but only on the final successful return should you examine the flags that pertain to security aspects of the context. Intermediate returns can set, for example, the ISC\_RET\_ALLOCATED\_MEMORY flag.

If the ISC\_REQ\_USE\_SUPPLIED\_CREDS flag is set, the [security package](../secgloss/s-gly.md) must look for a SECBUFFER\_PKG\_PARAMS buffer type in the *pInput* input buffer. This is not a generic solution, but it allows for a strong pairing of [security package](../secgloss/s-gly.md) and application when appropriate.

If ISC\_REQ\_ALLOCATE\_MEMORY was specified, the caller must free the memory by calling the [FreeContextBuffer](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.

For example, the input token could be the challenge from a LAN Manager. In this case, the output token would be the NTLM-encrypted response to the challenge.

The action the client takes depends on the return code from this function. If the return code is SEC\_E\_OK, there will be no second **InitializeSecurityContext (Kerberos)** call, and no response from the server is expected. If the return code is SEC\_I\_CONTINUE\_NEEDED, the client expects a token in response from the server and passes it in a second call to **InitializeSecurityContext (Kerberos)**. The SEC\_I\_COMPLETE\_NEEDED return code indicates that the client must finish building the message and call the [CompleteAuthToken](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function. The SEC\_I\_COMPLETE\_AND\_CONTINUE code incorporates both of these actions.

If **InitializeSecurityContext (Kerberos)** returns success on the first (or only) call, then the caller must eventually call the [DeleteSecurityContext](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function on the returned handle, even if the call fails on a later leg of the authentication exchange.

The client may call **InitializeSecurityContext (Kerberos)** again after it has completed successfully. This indicates to the [security package](../secgloss/s-gly.md) that a reauthentication is wanted.

Kernel mode callers have the following differences: the target name is a [Unicode](../secgloss/u-gly.md) string that must be allocated in virtual memory by using [VirtualAlloc](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc); it must not be allocated from the pool. Buffers passed and supplied in *pInput* and *pOutput* must be in virtual memory, not in the pool.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows XP \[desktop apps only\] |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header | Sspi.h (include Security.h) |
| Library | Secur32.lib |
| DLL | Secur32.dll |

## See also

[SSPI Functions](authentication-functions.md#sspi-functions)

[AcceptSecurityContext (Kerberos)](acceptsecuritycontext--kerberos.md)

[AcquireCredentialsHandle (Kerberos)](acquirecredentialshandle--kerberos.md)

[CompleteAuthToken](/windows/win32/api/sspi/nf-sspi-completeauthtoken)

[DeleteSecurityContext](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext)

[FreeContextBuffer](/windows/win32/api/sspi/nf-sspi-freecontextbuffer)

[SecBuffer](/windows/win32/api/sspi/ns-sspi-secbuffer)

[SecBufferDesc](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
