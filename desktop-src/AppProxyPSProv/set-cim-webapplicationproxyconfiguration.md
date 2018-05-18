---
Description: 'Updates the server configuration for Web Application Proxy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ee97e53d-fab8-4233-a24f-d1b0e2100142'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Set method of the CIM\_WebApplicationProxyConfiguration class'
---

# Set method of the CIM\_WebApplicationProxyConfiguration class

Updates the server configuration for Web Application Proxy.

## Syntax


```mof
uint32 Set(
  [in] string  ADFSUrl,
  [in] string  ADFSTokenSigningCertificatePublicKey,
  [in] string  ADFSWebApplicationProxyRelyingPartyUri,
  [in] boolean RegenerateAccessCookiesEncryptionKey,
  [in] string  ConnectedServersName[],
  [in] string  OAuthAuthenticationURL,
  [in] uint32  ConfigurationChangesPollingIntervalSec,
  [in] boolean UpgradeConfigurationVersion,
  [in] uint32  ADFSTokenAcceptanceDurationSec,
  [in] string  ADFSSignOutURL,
  [in] uint32  UserIdleTimeoutSec,
  [in] string  UserIdleTimeoutAction
);
```



## Parameters

<dl> <dt>

*ADFSUrl* \[in\]
</dt> <dd>

The URL of the Active Directory Federation Services (AD FS) server that performs authentication for Web Application Proxy.

</dd> <dt>

*ADFSTokenSigningCertificatePublicKey* \[in\]
</dt> <dd>

The thumbprint of the certificate that is used to authenticate connections to the AD FS server that performs authentication for the proxy service.

</dd> <dt>

*ADFSWebApplicationProxyRelyingPartyUri* \[in\]
</dt> <dd>

The URI of the Web Application Proxy server.

</dd> <dt>

*RegenerateAccessCookiesEncryptionKey* \[in\]
</dt> <dd>

**TRUE** to create a new encryption key that Web Application Proxy servers use to encrypt proxy cookies; otherwise, **FALSE**.

</dd> <dt>

*ConnectedServersName* \[in\]
</dt> <dd>

An array that contains the names of the proxy servers that are configured with Web Application Proxy.

</dd> <dt>

*OAuthAuthenticationURL* \[in\]
</dt> <dd>

The URL of the AD FS server that performs OAuth authentication for the Web Application Proxy.

</dd> <dt>

*ConfigurationChangesPollingIntervalSec* \[in\]
</dt> <dd>

The interval, in seconds, in which the Web Application Proxy servers query the AD FS server for changes to the configuration data.

</dd> <dt>

*UpgradeConfigurationVersion* \[in\]
</dt> <dd>

**TRUE** to force an upgrade of the Web Application Proxy configuration version; otherwise, **FALSE**. Set this parameter to **TRUE** after all Web Application Proxy servers on a cluster are upgraded.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*ADFSTokenAcceptanceDurationSec* \[in\]
</dt> <dd>

Specifies the maximum duration in seconds until which the Web Application Proxy server accepts the edge token issued by the AD FS server.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*ADFSSignOutURL* \[in\]
</dt> <dd>

Specifies the Sign-Out URL of the AD FS server used by Web Application Proxy.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*UserIdleTimeoutSec* \[in\]
</dt> <dd>

Specifies the inactivity time interval, in seconds, after which Web Application Proxy will redirect user to AD FS.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*UserIdleTimeoutAction* \[in\]
</dt> <dd>

Specifies whether inactive user will be redirected to the AD FS for signout or reauthentication.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

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

[**CIM\_WebApplicationProxyConfiguration**](cim-webapplicationproxyconfiguration.md)
</dt> </dl>

 

 




