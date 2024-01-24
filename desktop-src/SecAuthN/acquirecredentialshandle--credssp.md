---
description: The AcquireCredentialsHandle (CredSSP) function acquires a handle to preexisting credentials of a security principal.
ms.assetid: 3b73decf-75d4-4bc4-b7ca-5f16aaadff29
title: AcquireCredentialsHandle (CredSSP) function
ms.topic: reference
ms.date: 07/25/2019
---

# AcquireCredentialsHandle (CredSSP) function

The **AcquireCredentialsHandle (CredSSP)** function acquires a handle to preexisting credentials of a security principal. This handle is required by the [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) and [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) functions. These can be either preexisting *credentials*, which are established through a system logon that is not described here, or the caller can provide alternative credentials.

> [!Note]  
> This is not a "log on to the network" and does not imply gathering of credentials.

## Syntax

```C++
SECURITY_STATUS SEC_ENTRY AcquireCredentialsHandle(
  _In_opt_   SEC_CHAR       *pszPrincipal,
  _In_       SEC_CHAR       *pszPackage,
  _In_       unsigned long  fCredentialUse,
  _In_opt_   void           *pvLogonID,
  _In_opt_   void           *pAuthData,
  _In_opt_   SEC_GET_KEY_FN pGetKeyFn,
  _Reserved_ void           *pvGetKeyArgument,
  _Out_      PCredHandle    phCredential,
  _Out_opt_  PTimeStamp     ptsExpiry
);
```

## Parameters

*pszPrincipal* \[in, optional\]

A pointer to a null-terminated string that specifies the name of the principal whose credentials the handle will reference.

> [!Note]  
> If the process that requests the handle does not have access to the credentials, the function returns an error. A null string indicates that the process requires a handle to the credentials of the user under whose security context it is executing.

*pszPackage* \[in\]

A pointer to a null-terminated string that specifies the name of the security package with which these credentials will be used. This is a security package name returned in the **Name** member of a [**SecPkgInfo**](/windows/win32/api/sspi/ns-sspi-secpkginfoa) structure returned by the [**EnumerateSecurityPackages**](/windows/win32/api/sspi/nf-sspi-enumeratesecuritypackagesa) function. After a context is established, [**QueryContextAttributes (CredSSP)**](querycontextattributes--credssp.md) can be called with *ulAttribute* set to **SECPKG\_ATTR\_PACKAGE\_INFO** to return information on the security package in use.

*fCredentialUse* \[in\]

A flag that indicates how these credentials will be used. This parameter can be one of the following values.

| Value                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SECPKG\_CRED\_INBOUND**<br/>0x1  | Validate an incoming server credential. Inbound credentials might be validated by using an authenticating authority when [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) or [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) is called. If such an authority is not available, the function will fail and return **SEC\_E\_NO\_AUTHENTICATING\_AUTHORITY**. Validation is package specific |
| **SECPKG\_CRED\_OUTBOUND**<br/>0x0 | Allow a local client credential to prepare an outgoing token. |

*pvLogonId* \[in, optional\]

A pointer to a [*locally unique identifier*](../secgloss/l-gly.md#_security_locally_unique_identifier_gly) (LUID) that identifies the user. This parameter is provided for file-system processes such as network redirectors. This parameter can be **NULL**.

*pAuthData* \[in, optional\]

A pointer to a [**CREDSSP\_CRED**](/windows/win32/api/credssp/ns-credssp-credssp_cred) structure that specifies authentication data for both Schannel and Negotiate packages.

*pGetKeyFn* \[in, optional\]

Reserved. This parameter is not used and should be set to **NULL**.

*pvGetKeyArgument* \[in, optional\]

Reserved. This parameter must be set to **NULL**.

*phCredential* \[out\]

A pointer to the [CredHandle](sspi-handles.md) structure that will receive the credential handle.

*ptsExpiry* \[out, optional\]

A pointer to a [**TimeStamp**](timestamp.md) structure that receives the time at which the returned credentials expire. The structure value received depends on the security package, which must specify the value in local time.

## Return value

If the function succeeds, it returns **SEC\_E\_OK**.

If the function fails, it returns one of the following error codes.

| Return code                      | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| **SEC\_E\_INSUFFICIENT\_MEMORY** | There is insufficient memory available to complete the requested action. |
| **SEC\_E\_INTERNAL\_ERROR**      | An error occurred that did not map to an SSPI error code.                |
| **SEC\_E\_NO\_CREDENTIALS**      | No credentials are available in the security package.                    |
| **SEC\_E\_NOT\_OWNER**           | The caller of the function does not have the necessary credentials.      |
| **SEC\_E\_SECPKG\_NOT\_FOUND**   | The requested security package does not exist.                           |
| **SEC\_E\_UNKNOWN\_CREDENTIALS** | The credentials supplied to the package were not recognized.             |

## Remarks

The **AcquireCredentialsHandle (CredSSP)** function returns a handle to the credentials of a principal, such as a user or client, as used by a specific security package. The function can return the handle to either preexisting credentials or newly created credentials and return it. This handle can be used in subsequent calls to the [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md) and [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md) functions.

In general, **AcquireCredentialsHandle (CredSSP)** does not provide the credentials of other users logged on to the same computer. However, a caller with SE\_TCB\_NAME [*privilege*](../secgloss/p-gly.md#_security_privilege_gly) can obtain the credentials of an existing logon session by specifying the [*logon identifier*](../secgloss/l-gly.md#_security_logon_identifier_gly) (LUID) of that session. Typically, this is used by kernel-mode modules that must act on behalf of a logged-on user.

A package might call the function in *pGetKeyFn* provided by the RPC run-time transport. If the transport does not support the notion of callback to retrieve credentials, this parameter must be **NULL**.

For kernel mode callers, the following differences must be noted:

- The two string parameters must be [*Unicode*](../secgloss/u-gly.md#_security_unicode_gly) strings.
- The buffer values must be allocated in process virtual memory, not from the pool.

When you have finished using the returned credentials, free the memory used by the credentials by calling the [**FreeCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-freecredentialshandle) function.

## Requirements

| Requirement | Value |
|--------------------------|----------------------------------------------------------------------------------|
| Minimum supported client | Windows Vista \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2008 \[desktop apps only\]                                        |
| Header                   | Sspi.h (include Security.h)                                                      |
| Library                  | Secur32.lib                                                                      |
| DLL                      | Secur32.dll                                                                      |
| Unicode and ANSI names   | **AcquireCredentialsHandleW** (Unicode) and **AcquireCredentialsHandleA** (ANSI) |

## See also

- [SSPI Functions](authentication-functions.md#sspi-functions)
- [**AcceptSecurityContext (CredSSP)**](acceptsecuritycontext--credssp.md)
- [**InitializeSecurityContext (CredSSP)**](initializesecuritycontext--credssp.md)
- [**FreeCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-freecredentialshandle)
