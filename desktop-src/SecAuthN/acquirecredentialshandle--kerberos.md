---
Description: 'Acquires a handle to preexisting credentials of a security principal that is using Kerberos.'
ms.assetid: '2612bbe9-856b-4a81-bffb-6c761035883d'
title: 'AcquireCredentialsHandle (Kerberos) function'
ms.topic: article
ms.date: 07/25/2019
---

# AcquireCredentialsHandle (Kerberos) function

The **AcquireCredentialsHandle (Kerberos)** function acquires a handle to preexisting credentials of a [*security principal*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly). This handle is required by the [**InitializeSecurityContext (Kerberos)**](initializesecuritycontext--kerberos.md) and [**AcceptSecurityContext (Kerberos)**](acceptsecuritycontext--kerberos.md) functions. These can be either preexisting *credentials*, which are established through a system logon that is not described here, or the caller can provide alternative credentials.

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
> If the process that requests the handle does not have access to the credentials, the function returns an error. A null string indicates that the process requires a handle to the credentials of the user under whose [*security context*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) it is executing.

 

</dd> <dt>

*pszPackage* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) with which these credentials will be used. This is a [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) name returned in the **Name** member of a [**SecPkgInfo**](secpkginfo.md) structure returned by the [**EnumerateSecurityPackages**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/ns-sspi-_secpkginfoa) function. After a context is established, [**QueryContextAttributes (Kerberos)**](querycontextattributes--kerberos.md) can be called with *ulAttribute* set to SECPKG\_ATTR\_PACKAGE\_INFO to return information on the [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) in use.

</dd> <dt>

*fCredentialUse* \[in\]
</dt> <dd>

A flag that indicates how these credentials will be used. This parameter can be one of the following values.



| Value                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_CRED_BOTH"></span><span id="secpkg_cred_both"></span><dl> <dt>**SECPKG\_CRED\_BOTH**</dt> </dl>             | Validate an incoming credential or use a local credential to prepare an outgoing token. This flag enables both other flags.<br/>                                                                                                                                                                                                                                                                                                                              |
| <span id="SECPKG_CRED_INBOUND"></span><span id="secpkg_cred_inbound"></span><dl> <dt>**SECPKG\_CRED\_INBOUND**</dt> </dl>    | Validate an incoming server credential. Inbound credentials might be validated by using an authenticating authority when [**InitializeSecurityContext (Kerberos)**](initializesecuritycontext--kerberos.md) or [**AcceptSecurityContext (Kerberos)**](acceptsecuritycontext--kerberos.md) is called. If such an authority is not available, the function will fail and return SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY. Validation is package specific.<br/> |
| <span id="SECPKG_CRED_OUTBOUND"></span><span id="secpkg_cred_outbound"></span><dl> <dt>**SECPKG\_CRED\_OUTBOUND**</dt> </dl> | Allow a local client credential to prepare an outgoing token.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

*pvLogonID* \[in\]
</dt> <dd>

A pointer to a [*locally unique identifier*](https://docs.microsoft.com/en-us/windows/win32/secgloss/l-gly) (LUID) that identifies the user. This parameter is provided for file-system processes such as network redirectors. This parameter can be **NULL**.

</dd> <dt>

*pAuthData* \[in\]
</dt> <dd>

A pointer to package-specific data. This parameter can be **NULL**, which indicates that the default credentials for that [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) must be used. To use supplied credentials, pass a [**SEC\_WINNT\_AUTH\_IDENTITY**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/ns-sspi-_sec_winnt_auth_identity_a) structure that includes those credentials in this parameter. The RPC run time passes whatever was provided in [**RpcBindingSetAuthInfo**](https://docs.microsoft.com/en-us/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo).

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

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the time at which the returned credentials expire. The value returned in this **TimeStamp** structure depends on the [*constrained delegation*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly). The [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) must return this value in local time.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, it returns one of the following error codes.



| Return code                                                                                                 | Description                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INSUFFICIENT\_MEMORY**</dt> </dl> | There is not enough memory available to complete the requested action.<br/>                                                                  |
| <dl> <dt>**SEC\_E\_INTERNAL\_ERROR**</dt> </dl>      | An error occurred that did not map to an SSPI error code.<br/>                                                                               |
| <dl> <dt>**SEC\_E\_NO\_CREDENTIALS**</dt> </dl>      | No credentials are available in the [*constrained delegation*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly).<br/> |
| <dl> <dt>**SEC\_E\_NOT\_OWNER**</dt> </dl>           | The caller of the function does not have the necessary credentials.<br/>                                                                     |
| <dl> <dt>**SEC\_E\_SECPKG\_NOT\_FOUND**</dt> </dl>   | The requested [*security package*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) does not exist.<br/>                                                                                          |
| <dl> <dt>**SEC\_E\_UNKNOWN\_CREDENTIALS**</dt> </dl> | The credentials supplied to the package were not recognized.<br/>                                                                            |



 

## Remarks

The **AcquireCredentialsHandle (Kerberos)** function returns a handle to the credentials of a principal, such as a user or client, as used by a specific [*constrained delegation*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly). This can be the handle to preexisting credentials, or the function can create a new set of credentials and return it. This handle can be used in subsequent calls to the [**AcceptSecurityContext (Kerberos)**](acceptsecuritycontext--kerberos.md) and [**InitializeSecurityContext (Kerberos)**](initializesecuritycontext--kerberos.md) functions.

In general, **AcquireCredentialsHandle (Kerberos)** does not allow a process to obtain a handle to the credentials of other users logged on to the same computer. However, a caller with SE\_TCB\_NAME [*privilege*](https://docs.microsoft.com/en-us/windows/win32/secgloss/s-gly) has the option of specifying the [*logon identifier*](https://docs.microsoft.com/en-us/windows/win32/secgloss/l-gly) (LUID) of any existing logon session token to get a handle to that session's credentials. Typically, this is used by kernel-mode modules that must act on behalf of a logged-on user.

A package might call the function in *pGetKeyFn* provided by the RPC run-time transport. If the transport does not support the notion of callback to retrieve credentials, this parameter must be **NULL**.

For kernel mode callers, the following differences must be noted:

-   The two string parameters must be [*Unicode*](https://docs.microsoft.com/en-us/windows/win32/secgloss/u-gly) strings.
-   The buffer values must be allocated in process virtual memory, not from the pool.

When you have finished using the returned credentials, free the memory used by the credentials by calling the [**FreeCredentialsHandle**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-freecredentialshandle) function.

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

[**AcceptSecurityContext (Kerberos)**](acceptsecuritycontext--kerberos.md)
</dt> <dt>

[**InitializeSecurityContext (Kerberos)**](initializesecuritycontext--kerberos.md)
</dt> <dt>

[**FreeCredentialsHandle**](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-freecredentialshandle)
</dt> </dl>

 

 




