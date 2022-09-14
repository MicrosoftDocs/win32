---
title: HTTP_AUTH_ENABLE_ Constants (Http.h)
description: Define authentication schemes that can be enabled on a URL Group.
ms.assetid: db22645f-c9e4-427e-b3d5-91d568aec7c5
topic_type:
- apiref
api_name:
- HTTP_AUTH_ENABLE_BASIC
- HTTP_AUTH_ENABLE_DIGEST
- HTTP_AUTH_ENABLE_KERBEROS
- HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING
- HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL
- HTTP_AUTH_ENABLE_NTLM
- HTTP_AUTH_ENABLE_NEGOTIATE
- HTTP_AUTH_ENABLE_ALL
api_location:
- http.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP\_AUTH\_ENABLE\_ Constants

The **HTTP\_AUTH\_ENABLE** constants define authentication schemes that can be enabled on a URL Group.

These constants are used in the [**HTTP\_SERVER\_AUTHENTICATION\_INFO**](/windows/desktop/api/Http/ns-http-http_server_authentication_info) structure.

<dl> <dt>

<span id="HTTP_AUTH_ENABLE_BASIC"></span><span id="http_auth_enable_basic"></span>**HTTP\_AUTH\_ENABLE\_BASIC**
</dt> <dd> <dl> <dt>



The Basic authentication scheme is enabled.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_ENABLE_DIGEST"></span><span id="http_auth_enable_digest"></span>**HTTP\_AUTH\_ENABLE\_DIGEST**
</dt> <dd> <dl> <dt>



The Digest authentication scheme is enabled.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_ENABLE_KERBEROS"></span><span id="http_auth_enable_kerberos"></span>**HTTP\_AUTH\_ENABLE\_KERBEROS**
</dt> <dd> <dl> <dt>



The Kerberos authentication scheme is enabled.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING"></span><span id="http_auth_ex_flag_enable_kerberos_credential_caching"></span>**HTTP\_AUTH\_EX\_FLAG\_ENABLE\_KERBEROS\_CREDENTIAL\_CACHING**
</dt> <dd> <dl> <dt>



Kerberos credential caching is enabled.

**Windows Server 2003 and before:** Not available.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL"></span><span id="http_auth_ex_flag_capture_credential"></span>**HTTP\_AUTH\_EX\_FLAG\_CAPTURE\_CREDENTIAL**
</dt> <dd> <dl> <dt>



The HTTP Server API captures the caller identity and uses it for authentication for Negotiate and Kerberos schemes only.

**Windows Server 2003 and before:** Not available.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_ENABLE_NTLM"></span><span id="http_auth_enable_ntlm"></span>**HTTP\_AUTH\_ENABLE\_NTLM**
</dt> <dd> <dl> <dt>



The NTLM authentication scheme is enabled.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_ENABLE_NEGOTIATE"></span><span id="http_auth_enable_negotiate"></span>**HTTP\_AUTH\_ENABLE\_NEGOTIATE**
</dt> <dd> <dl> <dt>



The Negotiate authentication scheme is enabled.


</dt> </dl> </dd> <dt>

<span id="HTTP_AUTH_ENABLE_ALL"></span><span id="http_auth_enable_all"></span>**HTTP\_AUTH\_ENABLE\_ALL**
</dt> <dd> <dl> <dt>



All authentication schemes are enabled.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Http.h</dt> </dl> |



## See also

<dl> <dt>

[HTTP Server API Version 2.0 Constants](http-server-api-version-2-0-constants.md)
</dt> <dt>

[**HTTP\_SERVER\_AUTHENTICATION\_INFO**](/windows/desktop/api/Http/ns-http-http_server_authentication_info)
</dt> <dt>

[**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty)
</dt> <dt>

[**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty)
</dt> <dt>

[**HttpQueryUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpqueryurlgroupproperty)
</dt> <dt>

[**HttpQueryServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpqueryserversessionproperty)
</dt> </dl>

 

 





