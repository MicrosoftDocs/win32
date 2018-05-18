---
Description: 'Publishes a web application through Web Application Proxy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '82f711e0-dca7-4051-93a2-e4dc9b390457'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Add method of the CIM\_WebApplicationProxyApplication class'
---

# Add method of the CIM\_WebApplicationProxyApplication class

Publishes a web application through Web Application Proxy.

## Syntax


```mof
uint32 Add(
  [in] string  Name,
  [in] string  ExternalPreauthentication,
  [in] string  ClientCertificateAuthenticationBindingMode,
  [in] string  BackendServerCertificateValidation,
  [in] string  ExternalUrl,
  [in] string  ExternalCertificateThumbprint,
  [in] boolean EnableSignOut,
  [in] uint32  InactiveTransactionsTimeoutSec,
  [in] string  ClientCertificatePreauthenticationThumbprint,
  [in] boolean EnableHTTPRedirect,
  [in] string  ADFSUserCertificateStore,
  [in] boolean DisableHttpOnlyCookieProtection,
  [in] uint32  PersistentAccessCookieExpirationTimeSec,
  [in] string  BackendServerUrl,
  [in] boolean DisableTranslateUrlInRequestHeaders,
  [in] boolean DisableTranslateUrlInResponseHeaders,
  [in] string  BackendServerAuthenticationSPN,
  [in] string  ADFSRelyingPartyName,
  [in] boolean UseOAuthAuthentication
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The friendly name of the application.

</dd> <dt>

*ExternalPreauthentication* \[in\]
</dt> <dd>

The type of pre-authentication used by Web Application Proxy to identify the application.

This parameter can be set to one of the following values.

<dt>

PassThrough
</dt> <dd>

Do not perform pre-authentication.

</dd> <dt>

ADFS
</dt> <dd>

Use Active Directory Federation Services (AD FS).

</dd> <dt>

ClientCertificate
</dt> <dd>

Validate the client certificate.

</dd> <dt>

ADFSforBrowsersAndOffice
</dt> <dd>

Use Active Directory Federation Services (AD FS) for browsers and Microsoft Office clients.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> <dt>

ADFSforOAuth
</dt> <dd>

Use Active Directory Federation Services (AD FS) for OAuth.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> <dt>

ADFSforRichClients
</dt> <dd>

Use Active Directory Federation Services (AD FS) for rich clients.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> </dl> </dd> <dt>

*ClientCertificateAuthenticationBindingMode* \[in\]
</dt> <dd>

Indicates whether Web Application Proxy validates the client certificate during subsequent requests.

This parameter can be set to one of the following values.

<dt>

"None"
</dt> <dd>

Do not validate the certificate.

</dd> <dt>

*&lt;Any other value&gt;*
</dt> <dd>

Validate the certificate.

</dd> </dl> </dd> <dt>

*BackendServerCertificateValidation* \[in\]
</dt> <dd>

Indicates whether Web application proxy validates the certificate of the backend server.

This parameter can be set to one of the following values.

<dt>

"None"
</dt> <dd>

Do not validate the certificate.

</dd> <dt>

*&lt;Any other value&gt;*
</dt> <dd>

Validate the certificate.

</dd> </dl> </dd> <dt>

*ExternalUrl* \[in\]
</dt> <dd>

The fully qualified domain name (FQDN) that is used as the external address of the application.

</dd> <dt>

*ExternalCertificateThumbprint* \[in\]
</dt> <dd>

The thumbprint of the certificate for the *ExternalUrl* parameter. The certificate must be stored in the computer store and must be one of the following types:

-   simple certificate
-   subject alternative name (SAN) certificate
-   wildcard certificate

</dd> <dt>

*EnableSignOut* \[in\]
</dt> <dd>

Whether sign-out is enabled for this application.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*InactiveTransactionsTimeoutSec* \[in\]
</dt> <dd>

The interval, in seconds, after which incomplete HTTP transactions are immediately ended.

</dd> <dt>

*ClientCertificatePreauthenticationThumbprint* \[in\]
</dt> <dd>

The thumbprint of the client certificate to use for pre-authentication.

</dd> <dt>

*EnableHTTPRedirect* \[in\]
</dt> <dd>

Whether the web-application proxy should provide a redirect from HTTP URL to this URL.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*ADFSUserCertificateStore* \[in\]
</dt> <dd>

The certificate store to use when collecting certificate data for applications that are ADFS for rich clients. If not specified the DRS certificate store as indicated in ADFS configuration is used.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*DisableHttpOnlyCookieProtection* \[in\]
</dt> <dd>

**True** to disable the **HttpOnly** flag for the access cookie; otherwise, **false**.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*PersistentAccessCookieExpirationTimeSec* \[in\]
</dt> <dd>

The interval, in seconds, to persist the web-application-proxy-access cookie. You can use this parameter to enable single-sign-on for non-web-client applications.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*BackendServerUrl* \[in\]
</dt> <dd>

The corporate network address of the web application in the format: *&lt;protocol&gt;://&lt;hostname or IP address&gt;\[:port\]/\[path\]/*. For example:

-   http://sharepoint.contoso.com
-   http://mail.contoso.com/owa/
-   http://portal/

</dd> <dt>

*DisableTranslateUrlInRequestHeaders* \[in\]
</dt> <dd>

**True** to disable the translation of HTTP host headers from a public host header to an internal host header when the request is forwarded to a published application; otherwise, **false**.

</dd> <dt>

*DisableTranslateUrlInResponseHeaders* \[in\]
</dt> <dd>

**True** to disable hostname translation in HTTP redirect responses that are sent from internal hostnames to public hostnames; otherwise, **false**. Hostname translation is performed on the Content-Location, Location, and Set-Cookie response headers.

</dd> <dt>

*BackendServerAuthenticationSPN* \[in\]
</dt> <dd>

The service principal name (SPN) of the back end server.

</dd> <dt>

*ADFSRelyingPartyName* \[in\]
</dt> <dd>

The name of the relying party configured on the AD FS server.

</dd> <dt>

*UseOAuthAuthentication* \[in\]
</dt> <dd>

**True** to enable OAuth authentication for users that connect to this application with a Windows Store app; otherwise, **false**.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




