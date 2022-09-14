---
description: Initiates the client side, outbound [*security context*](../secgloss/s-gly.md) from a credential handle by using the Digest [*constrained delegation*](../secgloss/s-gly.md).
ms.assetid: 4b482dcc-3878-4bc6-85e4-229a1726cecc
title: InitializeSecurityContext (Digest) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---

# InitializeSecurityContext (Digest) function

The **InitializeSecurityContext (Digest)** function initiates the client side, outbound [*security context*](../secgloss/s-gly.md) from a credential handle. The function is used to build a [*security context*](../secgloss/s-gly.md) between the client application and a remote peer. **InitializeSecurityContext (Digest)** returns a token that the client must pass to the remote peer, which the peer in turn submits to the local security implementation through the [**AcceptSecurityContext (Digest)**](acceptsecuritycontext--digest.md) call. The token generated should be considered opaque by all callers.

Typically, the **InitializeSecurityContext (Digest)** function is called in a loop until a sufficient [*security context*](../secgloss/s-gly.md) is established.

## Syntax


```C++
SECURITY_STATUS SEC_Entry InitializeSecurityContext(
  _In_opt_    PCredHandle    phCredential,
  _In_opt_    PCtxtHandle    phContext,
  _In_opt_    SEC_CHAR       *pszTargetName,
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

<dl> <dt>

*phCredential* \[in, optional\]
</dt> <dd>

A handle to the credentials returned by [**AcquireCredentialsHandle (Digest)**](acquirecredentialshandle--digest.md). This handle is used to build the [*security context*](../secgloss/s-gly.md). The **InitializeSecurityContext (Digest)** function requires at least OUTBOUND credentials.

</dd> <dt>

*phContext* \[in, optional\]
</dt> <dd>

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (Digest)**, this pointer is **NULL**. On the second call, this parameter is a pointer to the handle to the partially formed context returned in the *phNewContext* parameter by the first call.

This parameter is optional and can be set to **NULL**.

</dd> <dt>

*pszTargetName* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that uniquely identifies the URI of the requested resource. The string must be composed of characters that are allowed in a URI and must be representable by the US ASCII code set. Percent encoding can be used to represent characters outside the US ASCII code set.

</dd> <dt>

*fContextReq* \[in\]
</dt> <dd>

Bit flags that indicate requests for the context. Not all packages can support all requirements. Flags used for this parameter are prefixed with ISC\_REQ\_, for example, ISC\_REQ\_DELEGATE. This parameter can be one or more of the following attributes flags.




| Value | Meaning | 
|-------|---------|
| <span id="ISC_REQ_ALLOCATE_MEMORY"></span><span id="isc_req_allocate_memory"></span><dl><dt><strong>ISC_REQ_ALLOCATE_MEMORY</strong></dt></dl> | The [*security package*](../secgloss/s-gly.md) allocates output buffers for you. When you have finished using the output buffers, free them by calling the [<strong>FreeContextBuffer</strong>](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.<br /> | 
| <span id="ISC_REQ_CONFIDENTIALITY"></span><span id="isc_req_confidentiality"></span><dl><dt><strong>ISC_REQ_CONFIDENTIALITY</strong></dt></dl> | Encrypt messages by using the [<strong>EncryptMessage</strong>](encryptmessage--general.md) function.<br /> | 
| <span id="ISC_REQ_EXTENDED_ERROR"></span><span id="isc_req_extended_error"></span><dl><dt><strong>ISC_REQ_EXTENDED_ERROR</strong></dt></dl> | When errors occur, the remote party will be notified.<br /> | 
| <span id="ISC_REQ_HTTP"></span><span id="isc_req_http"></span><dl><dt><strong>ISC_REQ_HTTP</strong></dt></dl> | Use Digest for HTTP. Omit this flag to use Digest as a SASL mechanism.<br /> | 
| <span id="ISC_REQ_INTEGRITY"></span><span id="isc_req_integrity"></span><dl><dt><strong>ISC_REQ_INTEGRITY</strong></dt></dl> | Sign messages and verify signatures by using the [<strong>EncryptMessage</strong>](encryptmessage--general.md) and [<strong>MakeSignature</strong>](/windows/win32/api/sspi/nf-sspi-makesignature) functions.<br /> | 
| <span id="ISC_REQ_MUTUAL_AUTH"></span><span id="isc_req_mutual_auth"></span><dl><dt><strong>ISC_REQ_MUTUAL_AUTH</strong></dt></dl> | The mutual authentication policy of the service will be satisfied.<br /><blockquote>[!Caution]<br />This does not necessarily mean that mutual authentication is performed, only that the authentication policy of the service is satisfied. To ensure that mutual authentication is performed, call the [<strong>QueryContextAttributes (Digest)</strong>](querycontextattributes--digest.md) function.</blockquote><br /> | 
| <span id="ISC_REQ_REPLAY_DETECT"></span><span id="isc_req_replay_detect"></span><dl><dt><strong>ISC_REQ_REPLAY_DETECT</strong></dt></dl> | Detect replayed messages that have been encoded by using the [<strong>EncryptMessage</strong>](encryptmessage--general.md) or [<strong>MakeSignature</strong>](/windows/win32/api/sspi/nf-sspi-makesignature) functions.<br /> | 
| <span id="ISC_REQ_SEQUENCE_DETECT"></span><span id="isc_req_sequence_detect"></span><dl><dt><strong>ISC_REQ_SEQUENCE_DETECT</strong></dt></dl> | Detect messages received out of sequence.<br /> | 
| <span id="ISC_REQ_STREAM"></span><span id="isc_req_stream"></span><dl><dt><strong>ISC_REQ_STREAM</strong></dt></dl> | Support a stream-oriented connection.<br /> | 




 

The requested attributes may not be supported by the client. For more information, see the *pfContextAttr* parameter.

For further descriptions of the various attributes, see [Context Requirements](context-requirements.md).

</dd> <dt>

*Reserved1* \[in\]
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> <dt>

*TargetDataRep* \[in\]
</dt> <dd>

This parameter is not used with Digest. Set it to zero.

</dd> <dt>

*pInput* \[in, optional\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure that contains pointers to the buffers supplied as input to the package. Unless the client context was initiated by the server, the value of this parameter must be **NULL** on the first call to the function. On subsequent calls to the function or when the client context was initiated by the server, the value of this parameter is a pointer to a buffer allocated with enough memory to hold the token returned by the remote computer.

For information about buffer configuration, see [Input Buffers for the Digest Challenge Response](input-buffers-for-the-digest-challenge-response.md).

</dd> <dt>

*Reserved2* \[in\]
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> <dt>

*phNewContext* \[in, out, optional\]
</dt> <dd>

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (Digest)**, this pointer receives the new context handle. On the second call, *phNewContext* can be the same as the handle specified in the *phContext* parameter.

</dd> <dt>

*pOutput* \[in, out, optional\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure that contains pointers to the [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structure that receives the output data. If a buffer was typed as SEC\_READWRITE in the input, it will be there on output. The system will allocate a buffer for the security token if requested (through ISC\_REQ\_ALLOCATE\_MEMORY) and fill in the address in the buffer descriptor for the security token.

This parameter receives the challenge response that must be sent to the server.

</dd> <dt>

*pfContextAttr* \[out\]
</dt> <dd>

A pointer to a variable to receive a set of bit flags that indicate the [*attributes*](../secgloss/a-gly.md#_security_attribute_gly) of the established context. For a description of the various attributes, see [Context Requirements](context-requirements.md).

Flags used for this parameter are prefixed with ISC\_RET, such as ISC\_RET\_DELEGATE. For a list of valid values, see the *fContextReq* parameter.

Do not check for security-related attributes until the final function call returns successfully. Attribute flags that are not related to security, such as the ASC\_RET\_ALLOCATED\_MEMORY flag, can be checked before the final return.

> [!Note]  
> Particular context attributes can change during negotiation with a remote peer.

 

</dd> <dt>

*ptsExpiry* \[out, optional\]
</dt> <dd>

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the expiration time of the context.

There is no expiration time for Microsoft Digest SSP [*security context*](../secgloss/s-gly.md)s or credentials.

</dd> </dl>

## Return value

If the function succeeds, the function returns one of the following success codes.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_OK**</dt> </dl>                      | The [*security context*](../secgloss/s-gly.md) was successfully initialized. There is no need for another [**InitializeSecurityContext (Digest)**](initializesecuritycontext--digest.md) call. If the function returns an output token, that is, if the SECBUFFER\_TOKEN in *pOutput* is of nonzero length, that token must be sent to the server.<br/> |
| <dl> <dt>**SEC\_I\_COMPLETE\_AND\_CONTINUE**</dt> </dl> | The client must call [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) and then pass the output to the server. The client then waits for a returned token and passes it, in another call, to [**InitializeSecurityContext (Digest)**](initializesecuritycontext--digest.md).<br/>                                                                                                                                  |
| <dl> <dt>**SEC\_I\_COMPLETE\_NEEDED**</dt> </dl>        | The client must finish building the message and then call the [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function.<br/>                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**SEC\_I\_CONTINUE\_NEEDED**</dt> </dl>        | The client must send the output token to the server and wait for a return token. The returned token is then passed in another call to [**InitializeSecurityContext (Digest)**](initializesecuritycontext--digest.md). The output token can be empty.<br/>                                                                                                                                                       |
| <dl> <dt>**SEC\_I\_INCOMPLETE\_CREDENTIALS**</dt> </dl> | Use with Schannel. The server has requested client authentication, and the supplied credentials either do not include a certificate or the certificate was not issued by a certification authority (CA) trusted by the server. For more information, see Remarks.<br/>                                            |



 

If the function fails, the function returns one of the following error codes.



| Return code                                                                                                          | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl>          | There is not enough memory available to complete the requested action.<br/>                                                                                                                                                                                                                   |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>               | An error occurred that did not map to an SSPI error code.<br/>                                                                                                                                                                                                                                |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>               | The handle passed to the function is not valid.<br/>                                                                                                                                                                                                                                          |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>                | The error is due to a malformed input token, such as a token corrupted in transit, a token of incorrect size, or a token passed into the wrong [*constrained delegation*](../secgloss/s-gly.md). Passing a token to the wrong package can happen if the client and server did not negotiate the proper [*constrained delegation*](../secgloss/s-gly.md).<br/> |
| <dl> <dt>**SEC\_E\_LOGON\_DENIED**</dt> </dl>                 | The logon failed.<br/>                                                                                                                                                                                                                                                                        |
| <dl> <dt>**SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY**</dt> </dl> | No authority could be contacted for authentication. The domain name of the authenticating party could be wrong, the domain could be unreachable, or there might have been a trust relationship failure.<br/>                                                                                  |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>               | No credentials are available in the [*constrained delegation*](../secgloss/s-gly.md).<br/>                                                                                                                                                  |
| <dl> <dt>**SEC\_E\_TARGET\_UNKNOWN**</dt> </dl>               | The target was not recognized.<br/>                                                                                                                                                                                                                                                           |
| <dl> <dt>**SEC\_E\_UNSUPPORTED\_FUNCTION**</dt> </dl>         | A context attribute flag that is not valid (ISC\_REQ\_DELEGATE or ISC\_REQ\_PROMPT\_FOR\_CREDS) was specified in the *fContextReq* parameter.<br/>                                                                                                                                            |
| <dl> <dt>**SEC\_E\_WRONG\_PRINCIPAL**</dt> </dl>              | The principal that received the authentication request is not the same as the one passed into the *pszTargetName* parameter. This indicates a failure in mutual authentication.<br/>                                                                                                          |



 

## Remarks

The caller is responsible for determining whether the final context attributes are sufficient. If, for example, confidentiality was requested, but could not be established, some applications may choose to shut down the connection immediately.

If attributes of the [*security context*](../secgloss/s-gly.md) are not sufficient, the client must free the partially created context by calling the [**DeleteSecurityContext**](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function.

The **InitializeSecurityContext (Digest)** function is used by a client to initialize an outbound context.

For a two-leg [*security context*](../secgloss/s-gly.md), the calling sequence is as follows:

1.  The client calls the function with *phContext* set to **NULL** and fills in the buffer descriptor with the input message.
2.  The [*security package*](../secgloss/s-gly.md) examines the parameters and constructs an opaque token, placing it in the TOKEN element in the buffer array. If the *fContextReq* parameter includes the ISC\_REQ\_ALLOCATE\_MEMORY flag, the [*security package*](../secgloss/s-gly.md) allocates the memory and returns the pointer in the TOKEN element.
3.  The client sends the token returned in the *pOutput* buffer to the target server. The server then passes the token as an input argument in a call to the [**AcceptSecurityContext (Digest)**](acceptsecuritycontext--digest.md) function.
4.  [**AcceptSecurityContext (Digest)**](acceptsecuritycontext--digest.md) may return a token, which the server sends to the client for a second call to **InitializeSecurityContext (Digest)** if the first call returned SEC\_I\_CONTINUE\_NEEDED.

For multiple-leg [*security context*](../secgloss/s-gly.md)s, such as mutual authentication, the calling sequence is as follows:

1.  The client calls the function as described earlier, but the package returns the SEC\_I\_CONTINUE\_NEEDED success code.
2.  The client sends the output token to the server and waits for the server's reply.
3.  Upon receipt of the server's response, the client calls **InitializeSecurityContext (Digest)** again, with *phContext* set to the handle that was returned from the last call. The token received from the server is supplied in the *pInput* parameter.

If the server has successfully responded, the [*security package*](../secgloss/s-gly.md) returns SEC\_E\_OK and a secure session is established.

If the function returns one of the error responses, the server's response is not accepted, and the session is not established.

If the function returns SEC\_I\_CONTINUE\_NEEDED, SEC\_I\_COMPLETE\_NEEDED, or SEC\_I\_COMPLETE\_AND\_CONTINUE, steps 2 and 3 are repeated.

To initialize a [*security context*](../secgloss/s-gly.md), more than one call to this function may be required, depending on the underlying authentication mechanism as well as the choices specified in the *fContextReq* parameter.

The *fContextReq* and *pfContextAttributes* parameters are bitmasks that represent various context attributes. For a description of the various attributes, see [Context Requirements](context-requirements.md). The *pfContextAttributes* parameter is valid on any successful return, but only on the final successful return should you examine the flags that pertain to security aspects of the context. Intermediate returns can set, for example, the ISC\_RET\_ALLOCATED\_MEMORY flag.

If the ISC\_REQ\_USE\_SUPPLIED\_CREDS flag is set, the [*security package*](../secgloss/s-gly.md) must look for a SECBUFFER\_PKG\_PARAMS buffer type in the *pInput* input buffer. This is not a generic solution, but it allows for a strong pairing of [*security package*](../secgloss/s-gly.md) and application when appropriate.

If ISC\_REQ\_ALLOCATE\_MEMORY was specified, the caller must free the memory by calling the [**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.

For example, the input token could be the challenge from a LAN Manager. In this case, the output token would be the NTLM-encrypted response to the challenge.

The action the client takes depends on the return code from this function. If the return code is SEC\_E\_OK, there will be no second **InitializeSecurityContext (Digest)** call, and no response from the server is expected. If the return code is SEC\_I\_CONTINUE\_NEEDED, the client expects a token in response from the server and passes it in a second call to **InitializeSecurityContext (Digest)**. The SEC\_I\_COMPLETE\_NEEDED return code indicates that the client must finish building the message and call the [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function. The SEC\_I\_COMPLETE\_AND\_CONTINUE code incorporates both of these actions.

If **InitializeSecurityContext (Digest)** returns success on the first (or only) call, then the caller must eventually call the [**DeleteSecurityContext**](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function on the returned handle, even if the call fails on a later leg of the authentication exchange.

The client may call **InitializeSecurityContext (Digest)** again after it has completed successfully. This indicates to the [*security package*](../secgloss/s-gly.md) that a reauthentication is wanted.

Kernel mode callers have the following differences: the target name is a [*Unicode*](../secgloss/u-gly.md) string that must be allocated in virtual memory by using [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc); it must not be allocated from the pool. Buffers passed and supplied in *pInput* and *pOutput* must be in virtual memory, not in the pool.

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

[**AcceptSecurityContext (Digest)**](acceptsecuritycontext--digest.md)
</dt> <dt>

[**AcquireCredentialsHandle (Digest)**](acquirecredentialshandle--digest.md)
</dt> <dt>

[**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken)
</dt> <dt>

[**DeleteSecurityContext**](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext)
</dt> <dt>

[**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer)
</dt> <dt>

[**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer)
</dt> <dt>

[**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc)
</dt> </dl>

 

 
