---
description: Acquires a handle to preexisting credentials of a security principal that is using Schannel.
ms.assetid: 0f006670-a1e5-47ed-baf5-ed55bd42b468
title: AcquireCredentialsHandle (Schannel) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---

# AcquireCredentialsHandle (Schannel) function

The **AcquireCredentialsHandle (Schannel)** function acquires a handle to preexisting credentials of a [*security principal*](../secgloss/s-gly.md). This handle is required by the [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md) and [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md) functions. These can be either preexisting *credentials*, which are established through a system logon that is not described here, or the caller can provide alternative credentials.

> [!Note]  
> This is not a "log on to the network" and does not imply gathering of credentials.

 

## Syntax


```C++
SECURITY_STATUS SEC_Entry AcquireCredentialsHandle(
  _In_opt_  SEC_CHAR       *pszPrincipal,
  _In_      SEC_CHAR       *pszPackage,
  _In_      ULONG          fCredentialUse,
  _In_opt_  PLUID          pvLogonID,
  _In_opt_  PVOID          pAuthData,
  _In_opt_  SEC_GET_KEY_FN pGetKeyFn,
  _In_opt_  PVOID          pvGetKeyArgument,
  _Out_     PCredHandle    phCredential,
  _Out_opt_ PTimeStamp     ptsExpiry
);
```



## Parameters

<dl> <dt>

*pszPrincipal* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the principal whose credentials the handle will reference.

When using the Schannel SSP, this parameter is not used and should be set to **NULL**.

> [!Note]  
> If the process that requests the handle does not have access to the credentials, the function returns an error. A null string indicates that the process requires a handle to the credentials of the user under whose [*security context*](../secgloss/s-gly.md) it is executing.

 

</dd> <dt>

*pszPackage* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the [*security package*](../secgloss/s-gly.md) with which these credentials will be used. This is a [*security package*](../secgloss/s-gly.md) name returned in the **Name** member of a [**SecPkgInfo**](/windows/win32/api/sspi/ns-sspi-secpkginfoa) structure returned by the [**EnumerateSecurityPackages**](/windows/win32/api/sspi/ns-sspi-secpkginfoa) function. After a context is established, [**QueryContextAttributes (Schannel)**](querycontextattributes--schannel.md) can be called with *ulAttribute* set to SECPKG\_ATTR\_PACKAGE\_INFO to return information on the [*security package*](../secgloss/s-gly.md) in use.

When using the Schannel SSP, set this parameter to UNISP\_NAME.

</dd> <dt>

*fCredentialUse* \[in\]
</dt> <dd>

A flag that indicates how these credentials will be used. This parameter can be one of the following values.



| Value                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_CRED_INBOUND"></span><span id="secpkg_cred_inbound"></span><dl> <dt>**SECPKG\_CRED\_INBOUND**</dt> </dl>    | Validate an incoming server credential. Inbound credentials might be validated by using an authenticating authority when [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md) or [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md) is called. If such an authority is not available, the function will fail and return SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY. Validation is package specific.<br/> |
| <span id="SECPKG_CRED_OUTBOUND"></span><span id="secpkg_cred_outbound"></span><dl> <dt>**SECPKG\_CRED\_OUTBOUND**</dt> </dl> | Allow a local client credential to prepare an outgoing token.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

*pvLogonID* \[in, optional\]
</dt> <dd>

A pointer to a [*locally unique identifier*](../secgloss/l-gly.md) (LUID) that identifies the user. This parameter is provided for file-system processes such as network redirectors. This parameter can be **NULL**.

When using the Schannel SSP, this parameter is not used and should be set to **NULL**.

</dd> <dt>

*pAuthData* \[in, optional\]
</dt> <dd>

A pointer to package-specific data. This parameter can be **NULL**, which indicates that the default credentials for that [*security package*](../secgloss/s-gly.md) must be used. To use supplied credentials, pass a [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/win32/api/sspi/ns-sspi-sec_winnt_auth_identity_a) structure that includes those credentials in this parameter. The RPC run time passes whatever was provided in [**RpcBindingSetAuthInfo**](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo).

When using the Schannel SSP, specify an [**SCH_CREDENTIALS**](/windows/win32/api/schannel/ns-schannel-sch_credentials) structure that indicates the protocol to use and the settings for various customizable channel features.

</dd> <dt>

*pGetKeyFn* \[in, optional\]
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*pvGetKeyArgument* \[in, optional\]
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*phCredential* \[out\]
</dt> <dd>

A pointer to a [CredHandle](sspi-handles.md) structure to receive the credential handle.

</dd> <dt>

*ptsExpiry* \[out, optional\]
</dt> <dd>

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the time at which the returned credentials expire. The value returned in this **TimeStamp** structure depends on the [*constrained delegation*](../secgloss/s-gly.md). The [*security package*](../secgloss/s-gly.md) must return this value in local time.

When using the Schannel SSP, this parameter is optional. When the credential to be used for authentication is a certificate, this parameter receives the expiration time for that certificate. If no certificate was supplied, then a maximum time value is returned.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.



| Return code                                                                                                 | Description                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl> | There is not enough memory available to complete the requested action.<br/>                                                                  |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>      | An error occurred that did not map to an SSPI error code.<br/>                                                                               |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>      | No credentials are available in the [*constrained delegation*](../secgloss/s-gly.md).<br/> |
| <dl> <dt>**SEC\_E\_NOT\_OWNER**</dt> </dl>           | The caller of the function does not have the necessary credentials.<br/>                                                                     |
| <dl> <dt>**SEC\_E\_SECPKG\_NOT\_FOUND**</dt> </dl>   | The requested [*security package*](../secgloss/s-gly.md) does not exist.<br/>                                                                                          |
| <dl> <dt>**SEC\_E\_UNKNOWN\_CREDENTIALS**</dt> </dl> | The credentials supplied to the package were not recognized.<br/>                                                                            |



 

## Remarks

The **AcquireCredentialsHandle (Schannel)** function returns a handle to the credentials of a principal, such as a user or client, as used by a specific [*constrained delegation*](../secgloss/s-gly.md). This can be the handle to preexisting credentials, or the function can create a new set of credentials and return it. This handle can be used in subsequent calls to the [**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md) and [**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md) functions.

In general, **AcquireCredentialsHandle (Schannel)** does not allow a process to obtain a handle to the credentials of other users logged on to the same computer. However, a caller with SE\_TCB\_NAME [*privilege*](../secgloss/s-gly.md) has the option of specifying the [*logon identifier*](../secgloss/l-gly.md) (LUID) of any existing logon session token to get a handle to that session's credentials. Typically, this is used by kernel-mode modules that must act on behalf of a logged-on user.

A package might call the function in *pGetKeyFn* provided by the RPC run-time transport. If the transport does not support the notion of callback to retrieve credentials, this parameter must be **NULL**.

For kernel mode callers, the following differences must be noted:

-   The two string parameters must be [*Unicode*](../secgloss/u-gly.md) strings.
-   The buffer values must be allocated in process virtual memory, not from the pool.

When you have finished using the returned credentials, free the memory used by the credentials by calling the [**FreeCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-freecredentialshandle) function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |
| Unicode and ANSI names<br/>   | **AcquireCredentialsHandleW** (Unicode) and **AcquireCredentialsHandleA** (ANSI)<br/>            |



## See also

<dl> <dt>

[**AcceptSecurityContext (Schannel)**](acceptsecuritycontext--schannel.md)
</dt> <dt>

[**FreeCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-freecredentialshandle)
</dt> </dl>

[**InitializeSecurityContext (Schannel)**](initializesecuritycontext--schannel.md)
</dt> <dt>

[**SCH_CREDENTIALS**](/windows/win32/api/schannel/ns-schannel-sch_credentials)
</dt> <dt>

[**SSPI Functions**](authentication-functions.md#sspi-functions)
</dt> <dt>
 

 
