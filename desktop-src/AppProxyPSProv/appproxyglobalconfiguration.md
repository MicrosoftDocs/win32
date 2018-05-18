---
Description: 'Manages the global server configuration for Web Application Proxy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e600811d-9ab0-44a1-9025-a53448a41770'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: AppProxyGlobalConfiguration class
---

# AppProxyGlobalConfiguration class

Manages the global server configuration for Web Application Proxy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class AppProxyGlobalConfiguration
{
  string ADFSUrl;
  string ADFSSignOutUrl;
  string ADFSTokenSigningCertificatePublicKey;
  string ADFSWebApplicationProxyRelyingPartyUri;
  string ConnectedServersName[];
  string OAuthAuthenticationURL;
  uint32 ConfigurationChangesPollingIntervalSec;
  uint32 ADFSTokenAcceptanceDurationSec;
  string ConfigurationVersion;
  uint32 UserIdleTimeoutSec;
  string UserIdleTimeoutAction;
};
```

## Members

The **AppProxyGlobalConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **AppProxyGlobalConfiguration** class has these properties.

<dl> <dt>

**ADFSSignOutUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the AD FS signout url.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**ADFSTokenAcceptanceDurationSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ADFS token acceptance duration, in seconds.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**ADFSTokenSigningCertificatePublicKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the thumbprint of the certificate that is used to authenticate connections to the AD FS server that performs authentication for the proxy service.

</dd> <dt>

**ADFSUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the URL of the Active Directory Federation Services (AD FS) server that performs authentication for Web Application Proxy.

</dd> <dt>

**ADFSWebApplicationProxyRelyingPartyUri**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the URI that contains the relying party trust settings for Web Application Proxy.

</dd> <dt>

**ConfigurationChangesPollingIntervalSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interval, in seconds, in which the Web Application Proxy servers query the AD FS server for changes to the configuration data.

</dd> <dt>

**ConfigurationVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the configuration version.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**ConnectedServersName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets and sets an array that contains the names of the proxy servers that are configured with Web Application Proxy.

</dd> <dt>

**OAuthAuthenticationURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the URL of the AD FS server that performs OAuth authentication for the Web Application Proxy.

</dd> <dt>

**UserIdleTimeoutAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user idle timeout action.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

<dt>

<span id="Signout"></span><span id="signout"></span><span id="SIGNOUT"></span>

**Signout** ("Signout")


</dt> <dd></dd> <dt>

<span id="Reauthenticate"></span><span id="reauthenticate"></span><span id="REAUTHENTICATE"></span>

**Reauthenticate** ("Reauthenticate")


</dt> <dd></dd> </dl>

</dd> <dt>

**UserIdleTimeoutSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user idle timeout, in seconds.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> </dl>

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

[Application Proxy WMI Provider Reference](application-proxy-wmi-provider-reference.md)
</dt> </dl>

 

 




