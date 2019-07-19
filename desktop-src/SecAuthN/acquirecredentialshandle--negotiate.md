---
Description: 'Acquires a handle to preexisting credentials of a security principal that is using Negotiate.'
ms.assetid: 'ff372163-c73b-41bb-afcb-7d5de7720967'
title: 'AcquireCredentialsHandle (Negotiate) function'
---

# AcquireCredentialsHandle (Negotiate) function

The **AcquireCredentialsHandle (Negotiate)** function acquires a handle to preexisting [*credentials*](security.c_gly#-security-credentials-gly) of a [*security principal*](security.s_gly#-security-security-principal-gly). This handle is required by the [**InitializeSecurityContext (Negotiate)**](initializesecuritycontext--negotiate.md) and [**AcceptSecurityContext (Negotiate)**](acceptsecuritycontext--negotiate.md) functions. These can be either preexisting *credentials*, which are established through a system logon that is not described here, or the caller can provide alternative credentials.

> [!Note]  
> This is not a "log on to the network" and does not imply gathering of credentials.

 

## Syntax


```C++
SECURITY_STATUS SEC_Entry AcquireCredentialsHandle(
  _In_  SEC_CHAR       *pszPrincipal,
  _In_  SEC_CHAR       *pszPackage,
  _In_  ULONG          fCredentialUse,
  _In_  PLUID          pvLogonID,
  _In_  PVOID          pAuthData,
  _In_  SEC_GET_KEY_FN pGetKeyFn,
  _In_  PVOID          pvGetKeyArgument,
  _Out_ PCredHandle    phCredential,
  _Out_ PTimeStamp     ptsExpiry
);
```



## Parameters

<dl> <dt>

*pszPrincipal* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the principal whose credentials the handle will reference.

> [!Note]  
> If the process that requests the handle does not have access to the credentials, the function returns an error. A null string indicates that the process requires a handle to the credentials of the user under whose [*security context*](security.s_gly#-security-security-context-gly) it is executing.

 

</dd> <dt>

*pszPackage* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the [*security package*](security.s_gly#-security-security-package-gly) with which these credentials will be used. This is a security package name returned in the **Name** member of a [**SecPkgInfo**](secpkginfo.md) structure returned by the [**EnumerateSecurityPackages**](enumeratesecuritypackages.md) function. After a context is established, [**QueryContextAttributes (Negotiate)**](querycontextattributes--negotiate.md) can be called with *ulAttribute* set to SECPKG\_ATTR\_PACKAGE\_INFO to return information on the security package in use.

To successfully call this function using the Schannel SSP, set this parameter to "Negotiate".

</dd> <dt>

*fCredentialUse* \[in\]
</dt> <dd>

A flag that indicates how these credentials will be used. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_CRED_AUTOLOGON_RESTRICTED"></span><span id="secpkg_cred_autologon_restricted"></span><dl> <dt>**SECPKG\_CRED\_AUTOLOGON\_RESTRICTED**</dt> <dt>0x00000010</dt> </dl> | The security does not use default logon credentials or credentials from [Credential Manager](credential-manager.md).<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                                                    |
| <span id="SECPKG_CRED_BOTH"></span><span id="secpkg_cred_both"></span><dl> <dt>**SECPKG\_CRED\_BOTH**</dt> </dl>                                                                                                                  | Validate an incoming credential or use a local credential to prepare an outgoing token. This flag enables both other flags.<br/>                                                                                                                                                                                                                                                                                                                                  |
| <span id="SECPKG_CRED_INBOUND"></span><span id="secpkg_cred_inbound"></span><dl> <dt>**SECPKG\_CRED\_INBOUND**</dt> </dl>                                                                                                         | Validate an incoming server credential. Inbound credentials might be validated by using an authenticating authority when [**InitializeSecurityContext (Negotiate)**](initializesecuritycontext--negotiate.md) or [**AcceptSecurityContext (Negotiate)**](acceptsecuritycontext--negotiate.md) is called. If such an authority is not available, the function will fail and return SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY. Validation is package specific.<br/> |
| <span id="SECPKG_CRED_OUTBOUND"></span><span id="secpkg_cred_outbound"></span><dl> <dt>**SECPKG\_CRED\_OUTBOUND**</dt> </dl>                                                                                                      | Allow a local client credential to prepare an outgoing token.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="SECPKG_CRED_PROCESS_POLICY_ONLY"></span><span id="secpkg_cred_process_policy_only"></span><dl> <dt>**SECPKG\_CRED\_PROCESS\_POLICY\_ONLY**</dt> <dt>0x00000020</dt> </dl>   | The function processes server policy and returns **SEC\_E\_NO\_CREDENTIALS**, indicating that the application should prompt for credentials.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                             |



 

</dd> <dt>

*pvLogonID* \[in\]
</dt> <dd>

A pointer to a [*locally unique identifier*](security.l_gly#-security-locally-unique-identifier-gly) (LUID) that identifies the user. This parameter is provided for file-system processes such as network redirectors. This parameter can be **NULL**.

</dd> <dt>

*pAuthData* \[in\]
</dt> <dd>

A pointer to package-specific data. This parameter can be **NULL**, which indicates that the default credentials for that [*package*](security.s_gly#-security-security-package-gly) must be used. To use supplied credentials, pass a **PSEC\_WINNT\_AUTH\_IDENTITY\_OPAQUE** structure returned from a previous call to the [**SspiPromptForCredentials**](sspipromptforcredentials.md) function.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** The **PSEC\_WINNT\_AUTH\_IDENTITY\_OPAQUE** type and the [**SspiPromptForCredentials**](sspipromptforcredentials.md) function are not supported. To use supplied credentials, pass a pointer to either a [**SEC\_WINNT\_AUTH\_IDENTITY**](sec-winnt-auth-identity.md) or [**SEC\_WINNT\_AUTH\_IDENTITY\_EX**](sec-winnt-auth-identity-ex.md) structure that includes those credentials.

The RPC run time passes whatever was provided in [**RpcBindingSetAuthInfo**](rpc.rpcbindingsetauthinfo).

When using the Negotiate package, the maximum character lengths for user name, password, and domain are 256, 256, and 15, respectively.

</dd> <dt>

*pGetKeyFn* \[in\]
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*pvGetKeyArgument* \[in\]
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*phCredential* \[out\]
</dt> <dd>

A pointer to a [CredHandle](sspi-handles.md) structure to receive the credential handle.

</dd> <dt>

*ptsExpiry* \[out\]
</dt> <dd>

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the time at which the returned credentials expire. The value returned in this **TimeStamp** structure depends on the security package. The security package must return this value in local time.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.



| Return code                                                                                                 | Description                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl> | There is not enough memory available to complete the requested action.<br/>                                                                  |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>      | An error occurred that did not map to an SSPI error code.<br/>                                                                               |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>      | No credentials are available in the [*security package*](security.s_gly#-security-security-package-gly).<br/> |
| <dl> <dt>**SEC\_E\_NOT\_OWNER**</dt> </dl>           | The caller of the function does not have the necessary credentials.<br/>                                                                     |
| <dl> <dt>**SEC\_E\_SECPKG\_NOT\_FOUND**</dt> </dl>   | The requested security package does not exist.<br/>                                                                                          |
| <dl> <dt>**SEC\_E\_UNKNOWN\_CREDENTIALS**</dt> </dl> | The credentials supplied to the package were not recognized.<br/>                                                                            |



 

## Remarks

The **AcquireCredentialsHandle (Negotiate)** function returns a handle to the credentials of a principal, such as a user or client, as used by a specific [*security package*](security.s_gly#-security-security-package-gly). This can be the handle to preexisting credentials, or the function can create a new set of credentials and return it. This handle can be used in subsequent calls to the [**AcceptSecurityContext (Negotiate)**](acceptsecuritycontext--negotiate.md) and [**InitializeSecurityContext (Negotiate)**](initializesecuritycontext--negotiate.md) functions.

In general, **AcquireCredentialsHandle (Negotiate)** does not allow a process to obtain a handle to the credentials of other users logged on to the same computer. However, a caller with SE\_TCB\_NAME [*privilege*](security.p_gly#-security-privilege-gly) has the option of specifying the [*logon identifier*](security.l_gly#-security-logon-identifier-gly) (LUID) of any existing logon session token to get a handle to that session's [*credentials*](security.c_gly#-security-credentials-gly). Typically, this is used by kernel-mode modules that must act on behalf of a logged-on user.

A package might call the function in *pGetKeyFn* provided by the RPC run-time transport. If the transport does not support the notion of callback to retrieve credentials, this parameter must be **NULL**.

For kernel mode callers, the following differences must be noted:

-   The two string parameters must be [*Unicode*](security.u_gly#-security-unicode-gly) strings.
-   The buffer values must be allocated in process virtual memory, not from the pool.

When you have finished using the returned credentials, free the memory used by the credentials by calling the [**FreeCredentialsHandle**](freecredentialshandle.md) function.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |
| Unicode and ANSI names<br/>   | **AcquireCredentialsHandleW** (Unicode) and **AcquireCredentialsHandleA** (ANSI)<br/>            |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**AcceptSecurityContext (Negotiate)**](acceptsecuritycontext--negotiate.md)
</dt> <dt>

[**InitializeSecurityContext (Negotiate)**](initializesecuritycontext--negotiate.md)
</dt> <dt>

[**FreeCredentialsHandle**](freecredentialshandle.md)
</dt> </dl>

 

 




