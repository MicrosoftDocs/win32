---
description: Lets a transport application query the Credential Security Support Provider (CredSSP) security package for certain attributes of a security context.
ms.assetid: 4956c4ab-b71e-4960-b750-f3a79b87baac
title: QueryContextAttributes (CredSSP) function (Sspi.h)
ms.topic: reference
ms.date: 07/25/2019
---


# QueryContextAttributes (CredSSP) function

The **QueryContextAttributes (CredSSP)** function lets a transport application query the Credential Security Support Provider (CredSSP) security package for certain [*attributes*](../secgloss/a-gly.md#_security_attribute_gly) of a security context.

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

A handle to the security context to be queried.

</dd> <dt>

*ulAttribute* \[in\]
</dt> <dd>

The attribute of the context to be returned. This parameter can be one of the following values. Unless otherwise specified, the attributes are applicable to both client and server.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SECPKG_ATTR_C_ACCESS_TOKEN"></span><span id="secpkg_attr_c_access_token"></span><dl> <dt>**SECPKG\_ATTR\_C\_ACCESS\_TOKEN**</dt> <dt>0x80000012</dt> </dl>                                 | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_AccessToken**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_accesstoken) structure that specifies the access token for the current security context.<br/> This attribute is supported only on the server.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="SECPKG_ATTR_C_FULL_ACCESS_TOKEN"></span><span id="secpkg_attr_c_full_access_token"></span><dl> <dt>**SECPKG\_ATTR\_C\_FULL\_ACCESS\_TOKEN**</dt> <dt>0x80000082</dt> </dl>                 | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_AccessToken**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_accesstoken) structure that specifies the access token for the current security context.<br/> This attribute is supported only on the server.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="SECPKG_ATTR_CERT_TRUST_STATUS"></span><span id="secpkg_attr_cert_trust_status"></span><dl> <dt>**SECPKG\_ATTR\_CERT\_TRUST\_STATUS**</dt> <dt>0x80000084</dt> </dl>                        | The *pBuffer* parameter contains a pointer to a [**CERT\_TRUST\_STATUS**](/windows/win32/api/wincrypt/ns-wincrypt-cert_trust_status) structure that specifies trust information about the certificate.<br/> This attribute is supported only on the client.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="SECPKG_ATTR_CREDS"></span><span id="secpkg_attr_creds"></span><dl> <dt>**SECPKG\_ATTR\_CREDS**</dt> <dt>0x80000080</dt> </dl>                                                              | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_ClientCreds**](/windows/win32/api/credssp/ns-credssp-secpkgcontext_clientcreds) structure that specifies client credentials.<br/> The client credentials can be either user name and password or user name and smart card PIN.<br/> This attribute is supported only on the server.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SECPKG_ATTR_CREDS_2"></span><span id="secpkg_attr_creds_2"></span><dl> <dt>**SECPKG\_ATTR\_CREDS\_2**</dt> <dt>0x80000086</dt> </dl>                                                       | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_ClientCreds**](/windows/win32/api/credssp/ns-credssp-secpkgcontext_clientcreds) structure that specifies client credentials. <br/> If the client credential is user name and password, the buffer is a packed [**KERB\_INTERACTIVE\_LOGON**](/windows/win32/api/ntsecapi/ns-ntsecapi-kerb_interactive_logon) structure.<br/> If the client credential is user name and smart card PIN, the buffer is a packed [**KERB\_CERTIFICATE\_LOGON**](/windows/win32/api/ntsecapi/ns-ntsecapi-kerb_certificate_logon) structure.<br/> If the client credential is an online identity credential, the buffer is a marshaled [**SEC\_WINNT\_AUTH\_IDENTITY\_EX2**](/windows/win32/api/sspi/ns-sspi-sec_winnt_auth_identity_ex2) structure.<br/> This attribute is supported only on the CredSSP server.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/> |
| <span id="SECPKG_ATTR_NEGOTIATION_PACKAGE"></span><span id="secpkg_attr_negotiation_package"></span><dl> <dt>**SECPKG\_ATTR\_NEGOTIATION\_PACKAGE**</dt> <dt>0x80000081</dt> </dl>                   | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_PackageInfo**](/windows/win32/api/sspi/ns-sspi-secpkginfoa) structure that specifies the name of the authentication package negotiated by the [Microsoft Negotiate](microsoft-negotiate.md) provider.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="SECPKG_ATTR_PACKAGE_INFO"></span><span id="secpkg_attr_package_info"></span><dl> <dt>**SECPKG\_ATTR\_PACKAGE\_INFO**</dt> <dt>10</dt> </dl>                                                | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_PackageInfo**](/windows/win32/api/sspi/ns-sspi-secpkginfoa)structure.<br/> Returns information on the SSP in use.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="SECPKG_ATTR_SERVER_AUTH_FLAGS"></span><span id="secpkg_attr_server_auth_flags"></span><dl> <dt>**SECPKG\_ATTR\_SERVER\_AUTH\_FLAGS**</dt> <dt>0x80000083</dt> </dl>                        | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Flags**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_flags) structure that specifies information about the flags in the current security context.<br/> This attribute is supported only on the client.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="SECPKG_ATTR_SIZES"></span><span id="secpkg_attr_sizes"></span><dl> <dt>**SECPKG\_ATTR\_SIZES**</dt> <dt>0x0</dt> </dl>                                                                     | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_Sizes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_sizes) structure.<br/> Queries the sizes of the structures used in the per-message functions and authentication exchanges.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="SECPKG_ATTR_SUBJECT_SECURITY_ATTRIBUTES"></span><span id="secpkg_attr_subject_security_attributes"></span><dl> <dt>**SECPKG\_ATTR\_SUBJECT\_SECURITY\_ATTRIBUTES**</dt> <dt>124</dt> </dl> | The *pBuffer* parameter contains a pointer to a [**SecPkgContext\_SubjectAttributes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_subjectattributes) structure.<br/> This value returns information about the security attributes for the connection.<br/> This value is supported only on the CredSSP server.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

A pointer to a structure that receives the attributes. The structure type depends on the value of the *ulAttribute* parameter.

</dd> </dl>

## Return value

If the function succeeds, it returns SEC\_E\_OK.

If the function fails, it can return the following error codes.



| Return code/value                                                                                                                                                            | Description                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INVALID\_HANDLE**</dt> <dt>0x80100003</dt> </dl>       | The function failed. The *phContext* parameter specifies a handle to an incomplete context.<br/> |
| <dl> <dt>**SEC\_E\_UNSUPPORTED\_FUNCTION**</dt> <dt>0x80090302</dt> </dl> | The function failed. The value of the *ulAttribute* parameter is not valid.<br/>                 |



 

## Remarks

The structure pointed to by the *pBuffer* parameter varies depending on the attribute being queried.

While the caller must allocate the *pBuffer* structure itself, the SSP allocates any memory required to hold variable-sized members of the *pBuffer* structure. Memory allocated by the SSP must be freed by calling the [**FreeContextBuffer**](/windows/win32/api/sspi/nf-sspi-freecontextbuffer) function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                   |
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

[**SecPkgContext\_ClientCreds**](/windows/win32/api/credssp/ns-credssp-secpkgcontext_clientcreds)
</dt> <dt>

[**SecPkgContext\_Sizes**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_sizes)
</dt> </dl>

 

 
