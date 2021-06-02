---
description: Enables a transport application to query the Negotiate [*security package*](../secgloss/s-gly.md) for certain attributes of a [*security context*](../secgloss/s-gly.md).
ms.assetid: 9e499161-d5fb-4a64-ac36-f82031a3a7c9
title: QueryContextAttributes (Negotiate) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---

# QueryContextAttributes (Negotiate) function

The **QueryContextAttributes (Negotiate)** function enables a transport application to query the Negotiate [*security package*](../secgloss/s-gly.md) for certain [*attributes*](../secgloss/a-gly.md#_security_attribute_gly) of a [*security context*](../secgloss/s-gly.md).

## Syntax


```C++
SECURITY_STATUS SEC_ENTRY QueryContextAttributes(
  _In_  PCtxtHandle phContext,
  _In_  ULONG       ulAttribute,
  _Out_ PVOID       pBuffer
);
```



## Parameters

<dl> <dt>

*phContext* \[in\]
</dt> <dd>

A handle to the [*security context*](../secgloss/s-gly.md) to be queried.

</dd> <dt>

*ulAttribute* \[in\]
</dt> <dd>

Specifies the attribute of the context to be returned. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_ATTR_ACCESS_TOKEN"></span><span id="secpkg_attr_access_token"></span><dl> <dt>**SECPKG\_ATTR\_ACCESS\_TOKEN**</dt> <dt>18</dt> </dl>                                       | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_AccessToken**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_accesstoken) structure.<br/> Returns a handle to the access token.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="SECPKG_ATTR_AUTHORITY"></span><span id="secpkg_attr_authority"></span><dl> <dt>**SECPKG\_ATTR\_AUTHORITY**</dt> <dt>6</dt> </dl>                                                  | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Authority**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_authoritya) structure.<br/> Queries the name of the authenticating authority.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="SECPKG_ATTR_CLIENT_SPECIFIED_TARGET"></span><span id="secpkg_attr_client_specified_target"></span><dl> <dt>**SECPKG\_ATTR\_CLIENT\_SPECIFIED\_TARGET**</dt> <dt>27</dt> </dl>     | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_ClientSpecifiedTarget**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_clientspecifiedtarget) structure that represents the service principal name (SPN) of the initial target supplied by the client. <br/> This value is supported only when using channel bindings.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="SECPKG_ATTR_CREDS_2"></span><span id="secpkg_attr_creds_2"></span><dl> <dt>**SECPKG\_ATTR\_CREDS\_2**</dt> <dt>0x80000086</dt> </dl>                                              | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_ClientCreds**](/windows/win32/api/credssp/ns-credssp-secpkgcontext_clientcreds) structure that specifies client credentials. <br/> If the client credential is user name and password, the buffer is a packed [**KERB\_INTERACTIVE\_LOGON**](/windows/win32/api/ntsecapi/ns-ntsecapi-kerb_interactive_logon) structure.<br/> If the client credential is user name and smart card PIN, the buffer is a packed [**KERB\_CERTIFICATE\_LOGON**](/windows/win32/api/ntsecapi/ns-ntsecapi-kerb_certificate_logon) structure.<br/> If the client credential is an online identity credential, the buffer is a marshaled [**SEC\_WINNT\_AUTH\_IDENTITY\_EX2**](/windows/win32/api/sspi/ns-sspi-sec_winnt_auth_identity_ex2) structure.<br/> This attribute is supported only on the CredSSP server.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/> |
| <span id="SECPKG_ATTR_DCE_INFO"></span><span id="secpkg_attr_dce_info"></span><dl> <dt>**SECPKG\_ATTR\_DCE\_INFO**</dt> <dt>3</dt> </dl>                                                    | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_DceInfo**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_dceinfo) structure.<br/> Queries for authorization data used by DCE services.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="SECPKG_ATTR_FLAGS"></span><span id="secpkg_attr_flags"></span><dl> <dt>**SECPKG\_ATTR\_FLAGS**</dt> <dt>14</dt> </dl>                                                             | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Flags**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_flags) structure.<br/> Returns information about the negotiated context flags.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="SECPKG_ATTR_KEY_INFO"></span><span id="secpkg_attr_key_info"></span><dl> <dt>**SECPKG\_ATTR\_KEY\_INFO**</dt> <dt>5</dt> </dl>                                                    | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_KeyInfo**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_keyinfoa) structure.<br/> Queries information about the keys used in a [*security context*](../secgloss/s-gly.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="SECPKG_ATTR_LAST_CLIENT_TOKEN_STATUS"></span><span id="secpkg_attr_last_client_token_status"></span><dl> <dt>**SECPKG\_ATTR\_LAST\_CLIENT\_TOKEN\_STATUS**</dt> <dt>30</dt> </dl> | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_LastClientTokenStatus**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_lastclienttokenstatus) structure that specifies whether the token from the most recent call to the [**InitializeSecurityContext**](initializesecuritycontext--general.md) function is the last token from the client.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="SECPKG_ATTR_LIFESPAN"></span><span id="secpkg_attr_lifespan"></span><dl> <dt>**SECPKG\_ATTR\_LIFESPAN**</dt> <dt>2</dt> </dl>                                                     | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Lifespan**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_lifespan) structure.<br/> Queries the life span of the context.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="SECPKG_ATTR_LOCAL_CRED"></span><span id="secpkg_attr_local_cred"></span><dl> <dt>**SECPKG\_ATTR\_LOCAL\_CRED**</dt> </dl>                                                                                                     | The *pBuffer* parameter contains a pointer to a **SecPkgContext\_LocalCredentialInfo** structure. (obsolete)<br/> Superseded by SECPKG\_ATTR\_LOCAL\_CERT\_CONTEXT.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="SECPKG_ATTR_NAMES"></span><span id="secpkg_attr_names"></span><dl> <dt>**SECPKG\_ATTR\_NAMES**</dt> <dt>1</dt> </dl>                                                              | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Names**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_namesa) structure.<br/> Queries the name associated with the context.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="SECPKG_ATTR_NATIVE_NAMES"></span><span id="secpkg_attr_native_names"></span><dl> <dt>**SECPKG\_ATTR\_NATIVE\_NAMES**</dt> <dt>13</dt> </dl>                                       | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_NativeNames**](https://docs.microsoft.com/windows/win32/api/sspi/ns-sspi-_secpkgcontext_nativenamesa) structure.<br/> Returns the principal name (CNAME) from the outbound ticket.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="SECPKG_ATTR_NEGOTIATION_INFO"></span><span id="secpkg_attr_negotiation_info"></span><dl> <dt>**SECPKG\_ATTR\_NEGOTIATION\_INFO**</dt> <dt>12</dt> </dl>                           | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_NegotiationInfo**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_negotiationinfoa) structure.<br/> Returns information about the [*security package*](../secgloss/s-gly.md) to be used with the negotiation process and the current state of the negotiation for the use of that package.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="SECPKG_ATTR_PACKAGE_INFO"></span><span id="secpkg_attr_package_info"></span><dl> <dt>**SECPKG\_ATTR\_PACKAGE\_INFO**</dt> <dt>10</dt> </dl>                                       | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_PackageInfo**](/windows/win32/api/sspi/ns-sspi-secpkginfoa) structure.<br/> Returns information on the SSP in use.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="SECPKG_ATTR_PASSWORD_EXPIRY"></span><span id="secpkg_attr_password_expiry"></span><dl> <dt>**SECPKG\_ATTR\_PASSWORD\_EXPIRY**</dt> <dt>8</dt> </dl>                               | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_PasswordExpiry**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_passwordexpiry) structure.<br/> Returns password expiration information.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="SECPKG_ATTR_ROOT_STORE"></span><span id="secpkg_attr_root_store"></span><dl> <dt>**SECPKG\_ATTR\_ROOT\_STORE**</dt> <dt>0x55</dt> </dl>                                           | The *pBuffer* parameter contains a pointer to a **HCERTCONTEXT**. <br/> Finds a certificate context that contains a certificate supplied by the Root store.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="SECPKG_ATTR_SESSION_KEY"></span><span id="secpkg_attr_session_key"></span><dl> <dt>**SECPKG\_ATTR\_SESSION\_KEY**</dt> <dt>9</dt> </dl>                                           | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_SessionKey**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_sessionkey) structure.<br/> Returns information about the [*session key*](../secgloss/s-gly.md)s.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SECPKG_ATTR_SIZES"></span><span id="secpkg_attr_sizes"></span><dl> <dt>**SECPKG\_ATTR\_SIZES**</dt> <dt>0</dt> </dl>                                                              | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Sizes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_sizes) structure.<br/> Queries the sizes of the structures used in the per-message functions.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="SECPKG_ATTR_TARGET_INFORMATION"></span><span id="secpkg_attr_target_information"></span><dl> <dt>**SECPKG\_ATTR\_TARGET\_INFORMATION**</dt> <dt>17</dt> </dl>                     | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_TargetInformation**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_targetinformation) structure.<br/> Returns information about the name of the remote server.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

A pointer to a structure that receives the attributes. The type of structure pointed to depends on the value specified in the *ulAttribute* parameter.

</dd> </dl>

## Return value

If the function succeeds, the return value is SEC\_E\_OK.

If the function fails, the return value is a nonzero error code.

## Remarks

The structure pointed to by the *pBuffer* parameter varies depending on the attribute being queried. The caller must allocate the *pBuffer* structure itself, but the SSP allocates any memory required to hold variable sized members of the *pBuffer* structure. Memory allocated by the SSP can be freed by calling the [**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.

After the SECPKG\_ATTR\_REMOTE\_CERT\_CONTEXT or SECPKG\_ATTR\_LOCAL\_CERT\_CONTEXT value has been read, the **hCertStore** member will be set to a handle to a certificate store that contains the intermediate certificates, if any. Also, the application is responsible for calling [**CertFreeCertificateContext**](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatecontext) to release the memory used by the certificate context.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |
| Unicode and ANSI names<br/>   | **QueryContextAttributesW** (Unicode) and **QueryContextAttributesA** (ANSI)<br/>                |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**CERT\_CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_context)
</dt> <dt>

[**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer)
</dt> <dt>

[**SecPkgContext\_Authority**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_authoritya)
</dt> <dt>

[**SecPkgContext\_ConnectionInfo**](/windows/win32/api/schannel/ns-schannel-secpkgcontext_connectioninfo)
</dt> <dt>

[**SecPkgContext\_DceInfo**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_dceinfo)
</dt> <dt>

[**SecPkgContext\_IssuerListInfoEx**](/windows/win32/api/schannel/ns-schannel-secpkgcontext_issuerlistinfoex)
</dt> <dt>

[**SecPkgContext\_KeyInfo**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_keyinfoa)
</dt> <dt>

[**SecPkgContext\_Lifespan**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_lifespan)
</dt> <dt>

[**SecPkgContext\_Names**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_namesa)
</dt> <dt>

[**SecPkgContext\_Sizes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_sizes)
</dt> <dt>

[**SecPkgContext\_StreamSizes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_streamsizes)
</dt> </dl>

 

 
