---
Description: 'The AcquireCredentialsHandle (CredSSP) function acquires a handle to preexisting credentials of a security principal.'
ms.assetid: '3b73decf-75d4-4bc4-b7ca-5f16aaadff29'
title: 'AcquireCredentialsHandle (CredSSP) function'
---

# AcquireCredentialsHandle (CredSSP) function

The **AcquireCredentialsHandle (CredSSP)** function acquires a handle to preexisting [*credentials*](security.c_gly#-security-credentials-gly) of a [*security principal*](security.s_gly#-security-security-principal-gly). This handle is required by the [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) and [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) functions. These can be either preexisting *credentials*, which are established through a system logon that is not described here, or the caller can provide alternative credentials.

> [!Note]  
> This is not a "log on to the network" and does not imply gathering of credentials.

 

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*pszPrincipal* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the principal whose credentials the handle will reference.

> [!Note]  
> If the process that requests the handle does not have access to the credentials, the function returns an error. A null string indicates that the process requires a handle to the credentials of the user under whose [*security context*](security.s_gly#-security-security-context-gly) it is executing.

 

</dd> <dt>

*pszPackage* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the [*security package*](security.s_gly#-security-security-package-gly) with which these credentials will be used. This is a security package name returned in the **Name** member of a [**SecPkgInfo**](secpkginfo.md) structure returned by the [**EnumerateSecurityPackages**](enumeratesecuritypackages.md) function. After a context is established, [**QueryContextAttributes (CredSSP)**](querycontextattributes--credssp.md) can be called with *ulAttribute* set to **SECPKG\_ATTR\_PACKAGE\_INFO** to return information on the security package in use.

</dd> <dt>

*fCredentialUse* \[in\]
</dt> <dd>

A flag that indicates how these credentials will be used. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_CRED_INBOUND"></span><span id="secpkg_cred_inbound"></span><dl> <dt>**SECPKG\_CRED\_INBOUND**</dt> <dt>0x1</dt> </dl>    | Validate an incoming server credential. Inbound credentials might be validated by using an authenticating authority when [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) or [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) is called. If such an authority is not available, the function will fail and return **SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY**. Validation is package specific.<br/> |
| <span id="SECPKG_CRED_OUTBOUND"></span><span id="secpkg_cred_outbound"></span><dl> <dt>**SECPKG\_CRED\_OUTBOUND**</dt> <dt>0x0</dt> </dl> | Allow a local client credential to prepare an outgoing token.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

*pvLogonId* \[in, optional\]
</dt> <dd>

A pointer to a [*locally unique identifier*](security.l_gly#-security-locally-unique-identifier-gly) (LUID) that identifies the user. This parameter is provided for file-system processes such as network redirectors. This parameter can be **NULL**.

</dd> <dt>

*pAuthData* \[in, optional\]
</dt> <dd>

A pointer to a [**CREDSSP\_CRED**](credssp-cred.md) structure that specifies authentication data for both Schannel and Negotiate packages.

</dd> <dt>

*pGetKeyFn* \[in, optional\]
</dt> <dd>

Reserved. This parameter is not used and should be set to **NULL**.

</dd> <dt>

*pvGetKeyArgument* \[in, optional\]
</dt> <dd>

Reserved. This parameter must be set to **NULL**.

</dd> <dt>

*phCredential* \[out\]
</dt> <dd>

A pointer to the [CredHandle](sspi-handles.md) structure that will receive the credential handle.

</dd> <dt>

*ptsExpiry* \[out, optional\]
</dt> <dd>

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the time at which the returned credentials expire. The structure value received depends on the security package, which must specify the value in local time.

</dd> </dl>

## Return value

If the function succeeds, it returns **SEC\_E\_OK**.

If the function fails, it returns one of the following error codes.



| Return code                                                                                                 | Description                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl> | There is insufficient memory available to complete the requested action.<br/>                                                                |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>      | An error occurred that did not map to an SSPI error code.<br/>                                                                               |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>      | No credentials are available in the [*security package*](security.s_gly#-security-security-package-gly).<br/> |
| <dl> <dt>**SEC\_E\_NOT\_OWNER**</dt> </dl>           | The caller of the function does not have the necessary credentials.<br/>                                                                     |
| <dl> <dt>**SEC\_E\_SECPKG\_NOT\_FOUND**</dt> </dl>   | The requested security package does not exist.<br/>                                                                                          |
| <dl> <dt>**SEC\_E\_UNKNOWN\_CREDENTIALS**</dt> </dl> | The credentials supplied to the package were not recognized.<br/>                                                                            |



 

## Remarks

The **AcquireCredentialsHandle (CredSSP)** function returns a handle to the credentials of a principal, such as a user or client, as used by a specific [*security package*](security.s_gly#-security-security-package-gly). The function can return the handle to either preexisting credentials or newly created credentials and return it. This handle can be used in subsequent calls to the [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) and [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) functions.

In general, **AcquireCredentialsHandle (CredSSP)** does not provide the credentials of other users logged on to the same computer. However, a caller with SE\_TCB\_NAME [*privilege*](security.p_gly#-security-privilege-gly) can obtain the [*credentials*](security.c_gly#-security-credentials-gly) of an existing logon session by specifying the [*logon identifier*](security.l_gly#-security-logon-identifier-gly) (LUID) of that session. Typically, this is used by kernel-mode modules that must act on behalf of a logged-on user.

A package might call the function in *pGetKeyFn* provided by the RPC run-time transport. If the transport does not support the notion of callback to retrieve credentials, this parameter must be **NULL**.

For kernel mode callers, the following differences must be noted:

-   The two string parameters must be [*Unicode*](security.u_gly#-security-unicode-gly) strings.
-   The buffer values must be allocated in process virtual memory, not from the pool.

When you have finished using the returned credentials, free the memory used by the credentials by calling the [**FreeCredentialsHandle**](freecredentialshandle.md) function.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |
| Unicode and ANSI names<br/>   | **AcquireCredentialsHandleW** (Unicode) and **AcquireCredentialsHandleA** (ANSI)<br/>            |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md)
</dt> <dt>

[**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md)
</dt> <dt>

[**FreeCredentialsHandle**](freecredentialshandle.md)
</dt> </dl>

 

 




