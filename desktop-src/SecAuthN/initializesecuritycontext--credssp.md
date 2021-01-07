---
description: Initiates the client side, outbound security context from a credential handle.
ms.assetid: f3d8c07b-db28-4f26-ba29-8733fc95bdb5
title: InitializeSecurityContext (CredSSP) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---

# InitializeSecurityContext (CredSSP) function

The **InitializeSecurityContext (CredSSP)** function initiates the client side, outbound security context from a credential handle. The function builds a security context between the client application and a remote peer. **InitializeSecurityContext (CredSSP)** returns a token that the client must pass to the remote peer; the peer in turn submits that token to the local security implementation through the [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) call. The token generated should be considered opaque by all callers.

Typically, the **InitializeSecurityContext (CredSSP)** function is called in a loop until a sufficient security context is established.

## Syntax


```C++
SECURITY_STATUS SEC_ENTRY InitializeSecurityContext(
  _In_opt_    PCredHandle    phCredential,
  _In_opt_    PCtxtHandle    phContext,
  _In_opt_    SEC_CHAR       *pszTargetName,
  _In_        unsigned long  fContextReq,
  _Reserved_  unsigned long  Reserved1,
  _In_        unsigned long  TargetDataRep,
  _Inout_opt_ PSecBufferDesc pInput,
  _In_        unsigned long  Reserved2,
  _Inout_opt_ PCtxtHandle    phNewContext,
  _Out_opt_   PSecBufferDesc pOutput,
  _Out_       unsigned long  *pfContextAttr,
  _Out_opt_   PTimeStamp     ptsExpiry
);
```



## Parameters

<dl> <dt>

*phCredential* \[in, optional\]
</dt> <dd>

A handle to the credentials returned by [**AcquireCredentialsHandle (CredSSP)**](acquirecredentialshandle--credssp.md). This handle is used to build the security context. The **InitializeSecurityContext (CredSSP)** function requires at least OUTBOUND credentials.

</dd> <dt>

*phContext* \[in, optional\]
</dt> <dd>

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (CredSSP)**, this pointer is **NULL**. On the second call, this parameter is a pointer to the handle to the partially formed context returned in the *phNewContext* parameter by the first call.

On the first call to **InitializeSecurityContext (CredSSP)**, specify **NULL**. On future calls, specify the token received in the *phNewContext* parameter after the first call to this function.

</dd> <dt>

*pTargetName* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that uniquely identifies the target server. Schannel uses this value to verify the server certificate. Schannel also uses this value to locate the session in the session cache when reestablishing a connection. The cached session is used only if all of the following conditions are met:

-   The target name is the same.
-   The cache entry has not expired.
-   The application process that calls the function is the same.
-   The logon session is the same.
-   The credential handle is the same.

</dd> <dt>

*fContextReq* \[in\]
</dt> <dd>

Bit flags that indicate requests for the context. Not all packages can support all requirements. Flags used for this parameter are prefixed with ISC\_REQ\_, for example, ISC\_REQ\_DELEGATE.

This parameter can be one or more of the following attributes flags.



| Value                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISC_REQ_ALLOCATE_MEMORY"></span><span id="isc_req_allocate_memory"></span><dl> <dt>**ISC\_REQ\_ALLOCATE\_MEMORY**</dt> <dt>0x100</dt> </dl>                         | The security package allocates output buffers for the caller. When you have finished using the output buffers, free them by calling the [**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.<br/>                                                        |
| <span id="ISC_REQ_CONNECTION"></span><span id="isc_req_connection"></span><dl> <dt>**ISC\_REQ\_CONNECTION**</dt> <dt>0x800</dt> </dl>                                         | The security context will not handle formatting messages.<br/>                                                                                                                                                                                               |
| <span id="ISC_REQ_EXTENDED_ERROR"></span><span id="isc_req_extended_error"></span><dl> <dt>**ISC\_REQ\_EXTENDED\_ERROR**</dt> <dt>0x4000</dt> </dl>                           | When errors occur, the remote party will be notified.<br/>                                                                                                                                                                                                   |
| <span id="ISC_REQ_MANUAL_CRED_VALIDATION"></span><span id="isc_req_manual_cred_validation"></span><dl> <dt>**ISC\_REQ\_MANUAL\_CRED\_VALIDATION**</dt> <dt>0x80000</dt> </dl> | Credential Security Support Provider (CredSSP) must not authenticate the server automatically. This flag is always set when using CredSSP.<br/>                                                                                                              |
| <span id="ISC_REQ_SEQUENCE_DETECT"></span><span id="isc_req_sequence_detect"></span><dl> <dt>**ISC\_REQ\_SEQUENCE\_DETECT**</dt> <dt>0x8</dt> </dl>                           | Detect messages received out of sequence.<br/>                                                                                                                                                                                                               |
| <span id="ISC_REQ_STREAM"></span><span id="isc_req_stream"></span><dl> <dt>**ISC\_REQ\_STREAM**</dt> <dt>0x8000</dt> </dl>                                                    | Support a stream-oriented connection.<br/>                                                                                                                                                                                                                   |
| <span id="ISC_REQ_USE_SUPPLIED_CREDS"></span><span id="isc_req_use_supplied_creds"></span><dl> <dt>**ISC\_REQ\_USE\_SUPPLIED\_CREDS**</dt> <dt>0x80</dt> </dl>                | CredSSP must not attempt to supply credentials for the client automatically.<br/>                                                                                                                                                                            |
| <span id="ISC_REQ_DELEGATE"></span><span id="isc_req_delegate"></span><dl> <dt>**ISC\_REQ\_DELEGATE**</dt> <dt>0x1</dt> </dl>                                                 | Indicates that the user's credentials are to be delegated to the server.<br/> If this flag is not specified, an empty set of credentials is delegated to the server.<br/> **Windows Server 2008 and Windows Vista:** This flag is required.<br/> |
| <span id="ISC_REQ_MUTUAL_AUTH"></span><span id="isc_req_mutual_auth"></span><dl> <dt>**ISC\_REQ\_MUTUAL\_AUTH**</dt> <dt>0x2</dt> </dl>                                       | Indicates that server authentication is not required. Delegation policies are still enforced if this flag is not specified.<br/> **Windows Server 2008 and Windows Vista:** This flag is ignored.<br/>                                                 |



 

The requested attributes may not be supported by the client. For more information, see the *pfContextAttr* parameter.

For further descriptions of the various attributes, see [Context Requirements](context-requirements.md).

</dd> <dt>

*Reserved1* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*TargetDataRep* \[in\]
</dt> <dd>

The data representation, such as byte ordering, on the target. This parameter can be either **SECURITY\_NATIVE\_DREP** or **SECURITY\_NETWORK\_DREP**.

</dd> <dt>

*pInput* \[in, out, optional\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure that contains pointers to the buffers supplied as input to the package. Unless the client context was initiated by the server, the value of this parameter must be **NULL** on the first call to the function. On subsequent calls to the function or when the client context was initiated by the server, the value of this parameter is a pointer to a buffer allocated with enough memory to hold the token returned by the remote computer.

On calls to this function after the initial call, there must be two buffers. The first has type **SECBUFFER\_TOKEN** and contains the token received from the server. The second buffer has type **SECBUFFER\_EMPTY**; set both the **pvBuffer** and **cbBuffer** members to zero.

</dd> <dt>

*Reserved2* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*phNewContext* \[in, out, optional\]
</dt> <dd>

A pointer to a [CtxtHandle](sspi-handles.md) structure. On the first call to **InitializeSecurityContext (CredSSP)**, this pointer receives the new context handle. On the second call, *phNewContext* can be the same as the handle specified in the *phContext* parameter.

On calls after the first call, pass the handle returned here as the *phContext* parameter and specify **NULL** for *phNewContext*.

</dd> <dt>

*pOutput* \[out, optional\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc) structure. This structure in turn contains pointers to the [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structure that receives the output data. If a buffer was typed as **SEC\_READWRITE** in the input, it will be there on output. The system will allocate a buffer for the security token if requested (through **ISC\_REQ\_ALLOCATE\_MEMORY**) and fill in the address in the buffer descriptor for the security token.

If the **ISC\_REQ\_ALLOCATE\_MEMORY** flag is specified, CredSSP will allocate memory for the buffer and put the appropriate information in the [**SecBufferDesc**](/windows/win32/api/sspi/ns-sspi-secbufferdesc).

</dd> <dt>

*pfContextAttr* \[out\]
</dt> <dd>

A pointer to a set of bit flags that indicate the [*attributes*](../secgloss/a-gly.md#_security_attribute_gly) of the established context. For a description of the various attributes, see [Context Requirements](context-requirements.md).

Flags used for this parameter are prefixed with ISC\_RET, such as **ISC\_RET\_DELEGATE**. For a list of valid values, see the *fContextReq* parameter.

Do not check for security-related attributes until the final function call returns successfully. Attribute flags that are not related to security, such as the **ASC\_RET\_ALLOCATED\_MEMORY** flag, can be checked before the final return.

> [!Note]  
> Particular context attributes can change during negotiation with a remote peer.

 

</dd> <dt>

*ptsExpiry* \[out, optional\]
</dt> <dd>

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the expiration time of the context. It is recommended that the security package always return this value in local time. This parameter is optional and **NULL** should be passed for short-lived clients.

</dd> </dl>

## Return value

If the function succeeds, it returns one of the following success codes.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INCOMPLETE\_MESSAGE**</dt> </dl>     | Data for the whole message was not read from the wire.<br/> When this value is returned, the *pInput* buffer contains a [**SecBuffer**](/windows/win32/api/sspi/ns-sspi-secbuffer) structure with a **BufferType** member of **SECBUFFER\_MISSING**. The **cbBuffer** member of **SecBuffer** specifies the number of additional bytes that the function must read from the client before this function succeeds. While this number is not always accurate, using it can help improve performance by avoiding multiple calls to this function.<br/> |
| <dl> <dt>**SEC\_E\_OK**</dt> </dl>                      | The security context was successfully initialized. There is no need for another [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) call. If the function returns an output token -- that is, if the **SECBUFFER\_TOKEN** in *pOutput* is of nonzero length -- that token must be sent to the server.<br/>                                                                                                   |
| <dl> <dt>**SEC\_I\_COMPLETE\_AND\_CONTINUE**</dt> </dl> | The client must call [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) and then pass the output to the server. The client then waits for a returned token and passes it, in another call, to [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md).<br/>                                                                                                                                                                                                                                            |
| <dl> <dt>**SEC\_I\_COMPLETE\_NEEDED**</dt> </dl>        | The client must finish building the message and then call the [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**SEC\_I\_CONTINUE\_NEEDED**</dt> </dl>        | The client must send the output token to the server and wait for a return token. The client passes the returned token in another call to [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md). The output token can be empty.<br/>                                                                                                                                                                                                                                                              |
| <dl> <dt>**SEC\_I\_INCOMPLETE\_CREDENTIALS**</dt> </dl> | The server has requested client authentication, but either the supplied credentials do not include a certificate, or the certificate was not issued by a certification authority that the server trusts. For more information, see Remarks.<br/>                                                                                                                                                                              |



 

If the function fails, the function returns one of the following error codes.



| Return code                                                                                                          | Description                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl>          | There is not enough memory available to complete the requested action.<br/>                                                                                                                                                                                                     |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>               | An error occurred that did not map to an SSPI error code.<br/>                                                                                                                                                                                                                  |
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> </dl>               | The handle passed to the function is not valid.<br/>                                                                                                                                                                                                                            |
| <dl> <dt>**SEC\_E\_INVALID\_TOKEN**</dt> </dl>                | The input token is malformed . Possible causes include a token corrupted in transit, a token of incorrect size, and a token passed into the wrong security package. This last condition can happen if the client and server did not negotiate the proper security package.<br/> |
| <dl> <dt>**SEC\_E\_LOGON\_DENIED**</dt> </dl>                 | The logon failed.<br/>                                                                                                                                                                                                                                                          |
| <dl> <dt>**SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY**</dt> </dl> | No authority could be contacted for authentication. The domain name of the authenticating party could be wrong, the domain could be unreachable, or there might have been a trust relationship failure.<br/>                                                                    |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>               | No credentials are available in the security package.<br/>                                                                                                                                    |
| <dl> <dt>**SEC\_E\_TARGET\_UNKNOWN**</dt> </dl>               | The target was not recognized.<br/>                                                                                                                                                                                                                                             |
| <dl> <dt>**SEC\_E\_UNSUPPORTED\_FUNCTION**</dt> </dl>         | The value of the *fContextReq* parameter is not valid. Either a required flag was not specified, or a flag that is not supported by CredSSP was specified.<br/>                                                                                                                 |
| <dl> <dt>**SEC\_E\_WRONG\_PRINCIPAL**</dt> </dl>              | The principal that received the authentication request is not the same as the one passed into the *pszTargetName* parameter. This error indicates a failure in mutual authentication.<br/>                                                                                      |
| <dl> <dt>**SEC\_E\_DELEGATION\_POLICY**</dt> </dl>            | The policy does not support delegation of credentials to the target server.<br/>                                                                                                                                                                                                |
| <dl> <dt>**SEC\_E\_POLICY\_NLTM\_ONLY**</dt> </dl>            | Delegation of credentials to the target server is not allowed when mutual authentication is not achieved.<br/>                                                                                                                                                                  |
| <dl> <dt>**SEC\_E\_MUTUAL\_AUTH\_FAILED**</dt> </dl>          | Server authentication failed when the ISC\_REQ\_MUTUAL\_AUTH flag is specified in the *fContextReq* parameter.<br/>                                                                                                                                                             |



 

## Remarks

The caller is responsible for determining whether the final context attributes are sufficient. If, for example, confidentiality was requested, but could not be established, some applications may choose to shut down the connection immediately.

If attributes of the security context are not sufficient, the client must free the partially created context by calling the [**DeleteSecurityContext**](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function.

The client calls the **InitializeSecurityContext (CredSSP)** function to initialize an outbound context.

For a two-leg security context, the calling sequence is as follows:

1.  The client calls the function with *phContext* set to **NULL** and fills in the buffer descriptor with the input message.
2.  The security package examines the parameters and constructs an opaque token, placing it in the TOKEN element in the buffer array. If the *fContextReq* parameter includes the **ISC\_REQ\_ALLOCATE\_MEMORY** flag, the security package allocates the memory and returns the pointer in the TOKEN element.
3.  The client sends the token returned in the *pOutput* buffer to the target server. The server then passes the token as an input argument in a call to the [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) function.
4.  [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) may return a token. The server sends this token to the client through a second **InitializeSecurityContext (CredSSP)** call if the first call returned **SEC\_I\_CONTINUE\_NEEDED**.

If the server has successfully responded, the security package returns **SEC\_E\_OK** and a secure session is established.

If the function returns one of the error responses, the server's response is not accepted, and the session is not established.

If the function returns **SEC\_I\_CONTINUE\_NEEDED**, **SEC\_I\_COMPLETE\_NEEDED**, or **SEC\_I\_COMPLETE\_AND\_CONTINUE**, steps 2 and 3 are repeated.

Security-context initialization may require more than one call to this function, depending on the underlying authentication mechanism as well as the choices specified in the *fContextReq* parameter.

The *fContextReq* and *pfContextAttributes* parameters are bitmasks that represent various context attributes. For a description of the various attributes, see [Context Requirements](context-requirements.md). While the *pfContextAttributes* parameter is valid on any successful return, you should examine the flags that pertain to security aspects of the context only on the final successful return. Intermediate returns can set, for example, the **ISC\_RET\_ALLOCATED\_MEMORY** flag.

If the **ISC\_REQ\_USE\_SUPPLIED\_CREDS** flag is set, the security package must look for a **SECBUFFER\_PKG\_PARAMS** buffer type in the *pInput* input buffer. While this is not a generic solution, it allows a strong pairing of security package and application when appropriate.

If **ISC\_REQ\_ALLOCATE\_MEMORY** was specified, the caller must free the memory by calling the [**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.

For example, the input token could be the challenge from a LAN Manager. In this case, the output token would be the NTLM-encrypted response to the challenge.

The action the client takes depends on the return code from this function. If the return code is **SEC\_E\_OK**, there will be no second **InitializeSecurityContext (CredSSP)** call, and no response from the server is expected. If the return code is **SEC\_I\_CONTINUE\_NEEDED**, the client expects a token in response from the server and passes it in a second call to **InitializeSecurityContext (CredSSP)**. The **SEC\_I\_COMPLETE\_NEEDED** return code indicates that the client must finish building the message and call the [**CompleteAuthToken**](/windows/win32/api/sspi/nf-sspi-completeauthtoken) function. The **SEC\_I\_COMPLETE\_AND\_CONTINUE** code incorporates both of these actions.

If **InitializeSecurityContext (CredSSP)** returns success on the first (or only) call, the caller must eventually call the [**DeleteSecurityContext**](/windows/win32/api/sspi/nf-sspi-deletesecuritycontext) function on the returned handle, even if the call fails on a later leg of the authentication exchange.

The client may call **InitializeSecurityContext (CredSSP)** again after it has completed successfully. This indicates to the security package that a reauthentication is wanted.

Kernel-mode callers have the following differences: the target name is a [*Unicode*](../secgloss/u-gly.md#_security_unicode_gly) string that must be allocated in virtual memory by using [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc); it must not be allocated from the pool. Buffers passed and supplied in *pInput* and *pOutput* must be in virtual memory, not in the pool.

If the function returns **SEC\_I\_INCOMPLETE\_CREDENTIALS**, check that the r credentials passed to the [**AcquireCredentialsHandle (CredSSP)**](acquirecredentialshandle--credssp.md) function specified a valid and trusted certificate The certificate must be a client authentication certificate issued by a certification authority trusted by the server. To obtain a list of the CAs trusted by the server, call the [**QueryContextAttributes (CredSSP)**](querycontextattributes--credssp.md) function with the **SECPKG\_ATTR\_ISSUER\_LIST\_EX** attribute.

After receiving an authentication certificate from a certification authority that the server trusts, the client application creates a new credential. It does so by calling the [**AcquireCredentialsHandle (CredSSP)**](acquirecredentialshandle--credssp.md) function and then calling **InitializeSecurityContext (CredSSP)** again, specifying the new credential in the *phCredential* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md)
</dt> <dt>

[**AcquireCredentialsHandle (CredSSP)**](acquirecredentialshandle--credssp.md)
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

 

 
