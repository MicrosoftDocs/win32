---
description: Includes options that can be set or retrieved for the current Microsoft Windows HTTP Services (WinHTTP) session.
ms.assetid: 8464d794-b4a8-4c83-9e26-69257000102a
title: WinHttpRequestOption enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpRequestOption
api_type: 
- IDLDef
api_location: 
- HttpRequest.idl
---

# WinHttpRequestOption enumeration

The **WinHttpRequestOption** enumeration includes options that can be set or retrieved for the current Microsoft Windows HTTP Services (WinHTTP) session.

## Syntax


```C++
typedef enum WinHttpRequestOption { 
  WinHttpRequestOption_UserAgentString,
  WinHttpRequestOption_URL,
  WinHttpRequestOption_URLCodePage,
  WinHttpRequestOption_EscapePercentInURL,
  WinHttpRequestOption_SslErrorIgnoreFlags,
  WinHttpRequestOption_SelectCertificate,
  WinHttpRequestOption_EnableRedirects,
  WinHttpRequestOption_UrlEscapeDisable,
  WinHttpRequestOption_UrlEscapeDisableQuery,
  WinHttpRequestOption_SecureProtocols,
  WinHttpRequestOption_EnableTracing,
  WinHttpRequestOption_RevertImpersonationOverSsl,
  WinHttpRequestOption_EnableHttpsToHttpRedirects,
  WinHttpRequestOption_EnablePassportAuthentication,
  WinHttpRequestOption_MaxAutomaticRedirects,
  WinHttpRequestOption_MaxResponseHeaderSize,
  WinHttpRequestOption_MaxResponseDrainSize,
  WinHttpRequestOption_EnableHttp1_1,
  WinHttpRequestOption_EnableCertificateRevocationCheck
} WinHttpRequestOption;
```



## Constants

<dl> <dt>

<span id="WinHttpRequestOption_UserAgentString"></span><span id="winhttprequestoption_useragentstring"></span><span id="WINHTTPREQUESTOPTION_USERAGENTSTRING"></span>**WinHttpRequestOption\_UserAgentString**
</dt> <dd>

Sets or retrieves a **VARIANT** that contains the [*user agent*](glossary.md) string.

</dd> <dt>

<span id="WinHttpRequestOption_URL"></span><span id="winhttprequestoption_url"></span><span id="WINHTTPREQUESTOPTION_URL"></span>**WinHttpRequestOption\_URL**
</dt> <dd>

Retrieves a **VARIANT** that contains the URL of the resource. This value is read-only; you cannot set the URL using this property. The URL cannot be read until the [**Open**](iwinhttprequest-open.md) method is called. This option is useful for checking the URL after the [**Send**](iwinhttprequest-send.md) method is finished to verify that any redirection occurred.

</dd> <dt>

<span id="WinHttpRequestOption_URLCodePage"></span><span id="winhttprequestoption_urlcodepage"></span><span id="WINHTTPREQUESTOPTION_URLCODEPAGE"></span>**WinHttpRequestOption\_URLCodePage**
</dt> <dd>

Sets or retrieves a **VARIANT** that identifies the [*code page*](glossary.md) for the URL string. The default value is the UTF-8 code page. The code page is used to convert the Unicode URL string, passed in the [**Open**](iwinhttprequest-open.md) method, to a single-byte string representation.

</dd> <dt>

<span id="WinHttpRequestOption_EscapePercentInURL"></span><span id="winhttprequestoption_escapepercentinurl"></span><span id="WINHTTPREQUESTOPTION_ESCAPEPERCENTINURL"></span>**WinHttpRequestOption\_EscapePercentInURL**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates whether percent characters in the URL string are converted to an escape sequence. The default value of this option is **VARIANT\_TRUE** which specifies all unsafe American National Standards Institute (ANSI) characters except the percent symbol are converted to an escape sequence.

</dd> <dt>

<span id="WinHttpRequestOption_SslErrorIgnoreFlags"></span><span id="winhttprequestoption_sslerrorignoreflags"></span><span id="WINHTTPREQUESTOPTION_SSLERRORIGNOREFLAGS"></span>**WinHttpRequestOption\_SslErrorIgnoreFlags**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates which server certificate errors should be ignored. This can be a combination of one or more of the following flags.



| Error                                                  | Value  |
|--------------------------------------------------------|--------|
| Unknown certification authority (CA) or untrusted root | 0x0100 |
| Wrong usage                                            | 0x0200 |
| Invalid common name (CN)                               | 0x1000 |
| Invalid date or certificate expired                    | 0x2000 |



 

The default value of this option in Version 5.1 of WinHTTP is zero, which results in no errors being ignored. In earlier versions of WinHTTP, the default setting was 0x3300, which resulted in all server certificate errors being ignored by default.

</dd> <dt>

<span id="WinHttpRequestOption_SelectCertificate"></span><span id="winhttprequestoption_selectcertificate"></span><span id="WINHTTPREQUESTOPTION_SELECTCERTIFICATE"></span>**WinHttpRequestOption\_SelectCertificate**
</dt> <dd>

Sets a **VARIANT** that specifies the client certificate that is sent to a server for authentication. This option indicates the location, [*certificate store*](glossary.md), and subject of a client certificate delimited with backslashes. For more information about selecting a client certificate, see [SSL in WinHTTP](ssl-in-winhttp.md).

</dd> <dt>

<span id="WinHttpRequestOption_EnableRedirects"></span><span id="winhttprequestoption_enableredirects"></span><span id="WINHTTPREQUESTOPTION_ENABLEREDIRECTS"></span>**WinHttpRequestOption\_EnableRedirects**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates whether requests are automatically redirected when the server specifies a new location for the resource. The default value of this option is **VARIANT\_TRUE** to indicate that requests are automatically redirected.

</dd> <dt>

<span id="WinHttpRequestOption_UrlEscapeDisable"></span><span id="winhttprequestoption_urlescapedisable"></span><span id="WINHTTPREQUESTOPTION_URLESCAPEDISABLE"></span>**WinHttpRequestOption\_UrlEscapeDisable**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates whether unsafe characters in the path and query components of a URL are converted to escape sequences. The default value of this option is **VARIANT\_TRUE**, which specifies that characters in the path and query are converted.

</dd> <dt>

<span id="WinHttpRequestOption_UrlEscapeDisableQuery"></span><span id="winhttprequestoption_urlescapedisablequery"></span><span id="WINHTTPREQUESTOPTION_URLESCAPEDISABLEQUERY"></span>**WinHttpRequestOption\_UrlEscapeDisableQuery**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates whether unsafe characters in the query component of the URL are converted to escape sequences. The default value of this option is **VARIANT\_TRUE**, which specifies that characters in the query are converted.

</dd> <dt>

<span id="WinHttpRequestOption_SecureProtocols"></span><span id="winhttprequestoption_secureprotocols"></span><span id="WINHTTPREQUESTOPTION_SECUREPROTOCOLS"></span>**WinHttpRequestOption\_SecureProtocols**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates which secure protocols can be used. This option selects the protocols acceptable to the client. The protocol is negotiated during the Secure Sockets Layer (SSL) handshake. This can be a combination of one or more of the following flags.



| Protocol                           | Value  |
|------------------------------------|--------|
| SSL 2.0                            | 0x0008 |
| SSL 3.0                            | 0x0020 |
| Transport Layer Security (TLS) 1.0 | 0x0080 |



 

The default value of this option is 0x0028, which indicates that SSL 2.0 or SSL 3.0 can be used. If this option is set to zero, the client and server are not able to determine an acceptable security protocol and the next [**Send**](iwinhttprequest-send.md) results in an error.

</dd> <dt>

<span id="WinHttpRequestOption_EnableTracing"></span><span id="winhttprequestoption_enabletracing"></span><span id="WINHTTPREQUESTOPTION_ENABLETRACING"></span>**WinHttpRequestOption\_EnableTracing**
</dt> <dd>

Sets or retrieves a **VARIANT** that indicates whether tracing is currently enabled. Also see [Collect WinHTTP traces](collect-traces.md).

</dd> <dt>

<span id="WinHttpRequestOption_RevertImpersonationOverSsl"></span><span id="winhttprequestoption_revertimpersonationoverssl"></span><span id="WINHTTPREQUESTOPTION_REVERTIMPERSONATIONOVERSSL"></span>**WinHttpRequestOption\_RevertImpersonationOverSsl**
</dt> <dd>

Controls whether the [**WinHttpRequest**](winhttprequest.md) object temporarily reverts client impersonation for the duration of the SSL certificate authentication operations. The default setting for the **WinHttpRequest** object is **TRUE**. Set this option to **FALSE** to keep impersonation while performing certificate authentication operations.

</dd> <dt>

<span id="WinHttpRequestOption_EnableHttpsToHttpRedirects"></span><span id="winhttprequestoption_enablehttpstohttpredirects"></span><span id="WINHTTPREQUESTOPTION_ENABLEHTTPSTOHTTPREDIRECTS"></span>**WinHttpRequestOption\_EnableHttpsToHttpRedirects**
</dt> <dd>

Controls whether or not WinHTTP allows redirects. By default, all redirects are automatically followed, except those that transfer from a secure (https) URL to an non-secure (http) URL. Set this option to **TRUE** to enable HTTPS to HTTP redirects.

</dd> <dt>

<span id="WinHttpRequestOption_EnablePassportAuthentication"></span><span id="winhttprequestoption_enablepassportauthentication"></span><span id="WINHTTPREQUESTOPTION_ENABLEPASSPORTAUTHENTICATION"></span>**WinHttpRequestOption\_EnablePassportAuthentication**
</dt> <dd>

Enables or disables support for Passport authentication. By default, automatic support for Passport authentication is disabled; set this option to **TRUE** to enable Passport authentication support.

</dd> <dt>

<span id="WinHttpRequestOption_MaxAutomaticRedirects"></span><span id="winhttprequestoption_maxautomaticredirects"></span><span id="WINHTTPREQUESTOPTION_MAXAUTOMATICREDIRECTS"></span>**WinHttpRequestOption\_MaxAutomaticRedirects**
</dt> <dd>

Sets or retrieves the maximum number of redirects that WinHTTP follows; the default is 10. This limit prevents unauthorized sites from making the WinHTTP client stall following a large number of redirects.

**Windows XP with SP1 and Windows 2000 with SP3:** This enumeration value is not supported.

</dd> <dt>

<span id="WinHttpRequestOption_MaxResponseHeaderSize"></span><span id="winhttprequestoption_maxresponseheadersize"></span><span id="WINHTTPREQUESTOPTION_MAXRESPONSEHEADERSIZE"></span>**WinHttpRequestOption\_MaxResponseHeaderSize**
</dt> <dd>

Sets or retrieves a bound set on the maximum size of the header portion of the server's response. This bound protects the client from a malicious server attempting to stall the client by sending a response with an infinite amount of header data. The default value is 64 KB.

**Windows XP with SP1 and Windows 2000 with SP3:** This enumeration value is not supported.

</dd> <dt>

<span id="WinHttpRequestOption_MaxResponseDrainSize"></span><span id="winhttprequestoption_maxresponsedrainsize"></span><span id="WINHTTPREQUESTOPTION_MAXRESPONSEDRAINSIZE"></span>**WinHttpRequestOption\_MaxResponseDrainSize**
</dt> <dd>

Sets or retrieves a bound on the amount of data that will be drained from responses in order to reuse a connection. The default is 1 MB.

**Windows XP with SP1 and Windows 2000 with SP3:** This enumeration value is not supported.

</dd> <dt>

<span id="WinHttpRequestOption_EnableHttp1_1"></span><span id="winhttprequestoption_enablehttp1_1"></span><span id="WINHTTPREQUESTOPTION_ENABLEHTTP1_1"></span>**WinHttpRequestOption\_EnableHttp1\_1**
</dt> <dd>

Sets or retrieves a boolean value that indicates whether HTTP/1.1 or HTTP/1.0 should be used. The default is **TRUE**, so that HTTP/1.1 is used by default.

**Windows XP with SP1 and Windows 2000 with SP3:** This enumeration value is not supported.

</dd> <dt>

<span id="WinHttpRequestOption_EnableCertificateRevocationCheck"></span><span id="winhttprequestoption_enablecertificaterevocationcheck"></span><span id="WINHTTPREQUESTOPTION_ENABLECERTIFICATEREVOCATIONCHECK"></span>**WinHttpRequestOption\_EnableCertificateRevocationCheck**
</dt> <dd>

Enables server certificate revocation checking during SSL negotiation. When the server presents a certificate, a check is performed to determine whether the certificate has been revoked by its issuer. If the certificate is indeed revoked, or the revocation check fails because the Certificate Revocation List (CRL) cannot be downloaded, the request fails; such revocation errors cannot be suppressed.

**Windows XP with SP1 and Windows 2000 with SP3:** This enumeration value is not supported.

</dd> </dl>

## Remarks

Set an option by specifying one of the preceding constants as the parameter of the [**Option**](iwinhttprequest-option.md) property.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHttp start page.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| IDL<br/>                      | <dl> <dt>HttpRequest.idl</dt> </dl> |



## See also

<dl> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




