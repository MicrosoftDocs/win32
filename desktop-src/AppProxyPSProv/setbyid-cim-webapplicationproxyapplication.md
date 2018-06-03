---
Description: Updates the settings of a published application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92976dd0-ebea-4329-80f3-d87e2280ea2a
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetByID method of the CIM\_WebApplicationProxyApplication class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByID method of the CIM\_WebApplicationProxyApplication class

Updates the settings of a published application.

## Syntax


```mof
uint32 SetByID(
  [in] string  ClientCertificateAuthenticationBindingMode,
  [in] string  BackendServerCertificateValidation,
  [in] string  ExternalUrl,
  [in] string  ExternalCertificateThumbprint,
  [in] string  BackendServerUrl,
  [in] boolean DisableTranslateUrlInRequestHeaders,
  [in] boolean EnableHTTPRedirect,
  [in] string  ADFSUserCertificateStore,
  [in] boolean DisableHttpOnlyCookieProtection,
  [in] uint32  PersistentAccessCookieExpirationTimeSec,
  [in] boolean EnableSignOut,
  [in] string  BackendServerAuthenticationMode,
  [in] boolean DisableTranslateUrlInResponseHeaders,
  [in] string  BackendServerAuthenticationSPN,
  [in] string  Name,
  [in] boolean UseOAuthAuthentication,
  [in] uint32  InactiveTransactionsTimeoutSec,
  [in] string  ClientCertificatePreauthenticationThumbprint,
  [in] string  ID
);
```



## Parameters

<dl> <dt>

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

*EnableHTTPRedirect* \[in\]
</dt> <dd>

Whether the web-application proxy should provide a redirect from HTTP URL to this URL.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*ADFSUserCertificateStore* \[in\]
</dt> <dd>

The certificate store to use when collecting certificate data for applications that are ADFS for rich clients. If not specified the DRS certificate store as indicated in ADFS configuration is used.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*DisableHttpOnlyCookieProtection* \[in\]
</dt> <dd>

**True** to disable the **HttpOnly** flag for the access cookie; otherwise, **false**.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*PersistentAccessCookieExpirationTimeSec* \[in\]
</dt> <dd>

The interval, in seconds, to persist the web-application-proxy-access cookie. You can use this parameter to enable single-sign-on for non-web-client applications.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*EnableSignOut* \[in\]
</dt> <dd>

Whether sign-out is enabled for this application.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*BackendServerAuthenticationMode* \[in\]
</dt> <dd>

Specifies the authentication method to be used by Web Application Proxy when contacting the backend server.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*DisableTranslateUrlInResponseHeaders* \[in\]
</dt> <dd>

**True** to disable hostname translation in HTTP redirect responses that are sent from internal hostnames to public hostnames; otherwise, **false**. Hostname translation is performed on the Content-Location, Location, and Set-Cookie response headers.

</dd> <dt>

*BackendServerAuthenticationSPN* \[in\]
</dt> <dd>

The service principal name (SPN) of the back end server.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The friendly name of the application.

</dd> <dt>

*UseOAuthAuthentication* \[in\]
</dt> <dd>

**True** to enable OAuth authentication for users that connect to this application with a Windows Store app; otherwise, **false**.

</dd> <dt>

*InactiveTransactionsTimeoutSec* \[in\]
</dt> <dd>

The interval, in seconds, after which incomplete HTTP transactions are immediately ended.

</dd> <dt>

*ClientCertificatePreauthenticationThumbprint* \[in\]
</dt> <dd>

The thumbprint of the client certificate to use for pre-authentication.

</dd> <dt>

*ID* \[in\]
</dt> <dd>

The ID of the application.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




