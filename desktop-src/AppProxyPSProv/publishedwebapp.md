---
Description: Retrieves the configuration data of a published web application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 07166f74-93e0-4b56-bd12-4e1711949361
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: PublishedWebApp class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PublishedWebApp class

Retrieves the configuration data of a published web application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class PublishedWebApp
{
  string  Name;
  string  ID;
  string  ADFSRelyingPartyName;
  string  ADFSRelyingPartyID;
  string  ADFSUserCertificateStore;
  string  ExternalPreauthentication;
  string  BackendServerAuthenticationMode;
  string  BackendServerAuthenticationSPN;
  string  ClientCertificateAuthenticationBindingMode;
  string  BackendServerCertificateValidation;
  string  ExternalUrl;
  string  ExternalCertificateThumbprint;
  string  ClientCertificatePreauthenticationThumbprint;
  string  BackendServerUrl;
  boolean DisableTranslateUrlInRequestHeaders;
  boolean DisableTranslateUrlInResponseHeaders;
  boolean UseOAuthAuthentication;
  boolean EnableHTTPRedirect;
  boolean EnableSignOut;
  boolean DisableHttpOnlyCookieProtection;
  uint32  InactiveTransactionsTimeoutSec;
  uint32  PersistentAccessCookieExpirationTimeSec;
};
```

## Members

The **PublishedWebApp** class has these types of members:

-   [Properties](#properties)

### Properties

The **PublishedWebApp** class has these properties.

<dl> <dt>

**ADFSRelyingPartyID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ID of the relying party configured on the AD FS server.

</dd> <dt>

**ADFSRelyingPartyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the relying party configured on the AD FS server.

</dd> <dt>

**ADFSUserCertificateStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the AD FS user certificate store.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**BackendServerAuthenticationMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the authentication mode for the back end server.

This property contains one of the following values.

<dt>

<span id="NoAuthentication"></span><span id="noauthentication"></span><span id="NOAUTHENTICATION"></span>

<span id="NoAuthentication"></span><span id="noauthentication"></span><span id="NOAUTHENTICATION"></span>**NoAuthentication** ("NoAuthentication")


</dt> <dd>

Do not perform authentication.

</dd> <dt>

<span id="IntegratedWindowsAuthentication"></span><span id="integratedwindowsauthentication"></span><span id="INTEGRATEDWINDOWSAUTHENTICATION"></span>

<span id="IntegratedWindowsAuthentication"></span><span id="integratedwindowsauthentication"></span><span id="INTEGRATEDWINDOWSAUTHENTICATION"></span>**IntegratedWindowsAuthentication** ("IntegratedWindowsAuthentication")


</dt> <dd>

Perform Windows authentication.

</dd> </dl>

</dd> <dt>

**BackendServerAuthenticationSPN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the service principal name (SPN) of the back end server.

</dd> <dt>

**BackendServerCertificateValidation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether Web application proxy validates the certificate of the back end server.

This parameter can be set to one of the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** ("None")


</dt> <dd>

Do not validate the certificate.

</dd> <dt>

<span id="ValidateCertificate"></span><span id="validatecertificate"></span><span id="VALIDATECERTIFICATE"></span>

<span id="ValidateCertificate"></span><span id="validatecertificate"></span><span id="VALIDATECERTIFICATE"></span>**ValidateCertificate** ("ValidateCertificate")


</dt> <dd>

Validate the certificate.

</dd> </dl>

</dd> <dt>

**BackendServerUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the URL of the back end server for the application.

</dd> <dt>

**ClientCertificateAuthenticationBindingMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether Web Application Proxy validates the client certificate during subsequent requests.

This parameter can be set to one of the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** ("None")


</dt> <dd>

Do not validate the certificate.

</dd> <dt>

<span id="ValidateCertificate"></span><span id="validatecertificate"></span><span id="VALIDATECERTIFICATE"></span>

<span id="ValidateCertificate"></span><span id="validatecertificate"></span><span id="VALIDATECERTIFICATE"></span>**ValidateCertificate** ("ValidateCertificate")


</dt> <dd>

Validate the certificate.

</dd> </dl>

</dd> <dt>

**ClientCertificatePreauthenticationThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the thumbprint of the client certificate to use for pre-authentication.

</dd> <dt>

**DisableHttpOnlyCookieProtection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether to disable the HttpOnly flag for the access cookie. **True** to disable the HttpOnly flag; otherwise, **false**.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**DisableTranslateUrlInRequestHeaders**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether to disable the translation of HTTP host headers from a public host header to an internal host header when the request is forwarded to a published application. **True** to disable the translation of HTTP host headers; otherwise, **false**.

</dd> <dt>

**DisableTranslateUrlInResponseHeaders**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether to disable hostname translation in HTTP redirect responses that are sent from internal hostnames to public hostnames. **True** to disable hostname translation in HTTP redirect responses; otherwise, **false**.

Hostname translation is performed on the Content-Location, Location, and Set-Cookie response headers.

</dd> <dt>

**EnableHTTPRedirect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the web-application proxy provides a redirect from HTTP URL to this URL.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**EnableSignOut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether sign-out is enabled for this application.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**ExternalCertificateThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the thumbprint of the certificate for the *ExternalUrl* parameter.

</dd> <dt>

**ExternalPreauthentication**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of pre-authentication used by Web Application Proxy to identify the application.

This property contains one of the following values.

<dt>

<span id="PassThrough"></span><span id="passthrough"></span><span id="PASSTHROUGH"></span>

<span id="PassThrough"></span><span id="passthrough"></span><span id="PASSTHROUGH"></span>**PassThrough** ("PassThrough")


</dt> <dd>

Do not perform pre-authentication.

</dd> <dt>

<span id="ADFS"></span><span id="adfs"></span>

<span id="ADFS"></span><span id="adfs"></span>**ADFS** ("ADFS")


</dt> <dd>

Use Active Directory Federation Services (AD FS).

</dd> <dt>

<span id="ClientCertificate"></span><span id="clientcertificate"></span><span id="CLIENTCERTIFICATE"></span>

<span id="ClientCertificate"></span><span id="clientcertificate"></span><span id="CLIENTCERTIFICATE"></span>**ClientCertificate** ("ClientCertificate")


</dt> <dd>

Validate the client certificate.

</dd> <dt>

<span id="ADFSforRichClients"></span><span id="adfsforrichclients"></span><span id="ADFSFORRICHCLIENTS"></span>

<span id="ADFSforRichClients"></span><span id="adfsforrichclients"></span><span id="ADFSFORRICHCLIENTS"></span>**ADFSforRichClients** ("ADFSforRichClients")


</dt> <dd>

Use Active Directory Federation Services (AD FS) for rich clients.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> <dt>

<span id="ADFSforOAuth"></span><span id="adfsforoauth"></span><span id="ADFSFOROAUTH"></span>

<span id="ADFSforOAuth"></span><span id="adfsforoauth"></span><span id="ADFSFOROAUTH"></span>**ADFSforOAuth** ("ADFSforOAuth")


</dt> <dd>

Use Active Directory Federation Services (AD FS) for OAuth.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> <dt>

<span id="ADFSforBrowsersAndOffice"></span><span id="adfsforbrowsersandoffice"></span><span id="ADFSFORBROWSERSANDOFFICE"></span>

<span id="ADFSforBrowsersAndOffice"></span><span id="adfsforbrowsersandoffice"></span><span id="ADFSFORBROWSERSANDOFFICE"></span>**ADFSforBrowsersAndOffice** ("ADFSforBrowsersAndOffice")


</dt> <dd>

Use Active Directory Federation Services (AD FS) for browsers and Microsoft Office clients.

**Windows Server 2012 R2:** This value is not available before Windows Server 2016.

</dd> </dl>

</dd> <dt>

**ExternalUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the fully qualified domain name (FQDN) that is the external address of the application.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ID of the application.

</dd> <dt>

**InactiveTransactionsTimeoutSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interval, in seconds, after which incomplete HTTP transactions with the application are immediately ended.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the application.

</dd> <dt>

**PersistentAccessCookieExpirationTimeSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interval, in seconds, that the web-application-proxy-access cookie is persisted.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

**UseOAuthAuthentication**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether to enable OAuth authentication for users that connect to this application with a Windows Store app. **True** to enable OAuth authentication; otherwise, **false**.

</dd> </dl>

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

[Application Proxy WMI Provider Reference](application-proxy-wmi-provider-reference.md)
</dt> </dl>

 

 




