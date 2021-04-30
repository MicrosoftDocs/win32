---
title: Win32_TSGatewayServerSettings class
description: Provides methods and properties to view and configure Remote Desktop Gateway (RD Gateway) server settings.
ms.assetid: f772bf71-68ef-4345-8123-f6ad50ee4d61
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayServerSettings class Remote Desktop Services
- Win32_TSGatewayServerSettings class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings
- Win32_TSGatewayServerSettings.MaxConnections
- Win32_TSGatewayServerSettings.UnlimitedConnections
- Win32_TSGatewayServerSettings.MaximumAllowedConnectionsBySku
- Win32_TSGatewayServerSettings.SkuName
- Win32_TSGatewayServerSettings.MaxProtocols
- Win32_TSGatewayServerSettings.MaxLogEvents
- Win32_TSGatewayServerSettings.adminMessageText
- Win32_TSGatewayServerSettings.adminMessageStartTime
- Win32_TSGatewayServerSettings.adminMessageEndTime
- Win32_TSGatewayServerSettings.consentMessageText
- Win32_TSGatewayServerSettings.OnlyConsentCapableClients
- Win32_TSGatewayServerSettings.CentralCAPEnabled
- Win32_TSGatewayServerSettings.RequestSOH
- Win32_TSGatewayServerSettings.AuthenticationPluginName
- Win32_TSGatewayServerSettings.AuthenticationPluginCLSID
- Win32_TSGatewayServerSettings.AuthenticationPluginDescription
- Win32_TSGatewayServerSettings.AuthorizationPluginName
- Win32_TSGatewayServerSettings.AuthorizationPluginCLSID
- Win32_TSGatewayServerSettings.AuthorizationPluginDescription
- Win32_TSGatewayServerSettings.SslBridging
- Win32_TSGatewayServerSettings.IsConfigured
- Win32_TSGatewayServerSettings.CertHash
- Win32_TSGatewayServerSettings.EnforceChannelBinding
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayServerSettings class

Provides methods and properties to view and configure Remote Desktop Gateway (RD Gateway) server settings. An administrator can use this class to configure a set of protocols, the set of events that will be written to the event log, and the maximum number of connections through RD Gateway.

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayServerSettings
{
  uint32  MaxConnections;
  boolean UnlimitedConnections;
  uint32  MaximumAllowedConnectionsBySku;
  string  SkuName;
  uint32  MaxProtocols;
  uint32  MaxLogEvents;
  string  adminMessageText;
  string  adminMessageStartTime;
  string  adminMessageEndTime;
  string  consentMessageText;
  boolean OnlyConsentCapableClients;
  boolean CentralCAPEnabled;
  boolean RequestSOH;
  string  AuthenticationPluginName;
  string  AuthenticationPluginCLSID;
  string  AuthenticationPluginDescription;
  string  AuthorizationPluginName;
  string  AuthorizationPluginCLSID;
  string  AuthorizationPluginDescription;
  uint32  SslBridging;
  boolean IsConfigured;
  uint8   CertHash[];
  boolean EnforceChannelBinding;
};
```

## Members

The **Win32\_TSGatewayServerSettings** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayServerSettings** class has these methods.



| Method                                                                                                                                             | Description                                                                                                                                                                                                                                                      |
|:---------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Configure**](configure-win32-tsgatewayserversettings.md)                                                                                       | Configures the IIS and RPC settings required by the RD Gateway service.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                               |
| [**EnableCentralCAP**](enablecentralcap-win32-tsgatewayserversettings.md)                                                                         | Enables or disables the **CentralCAPEnabled** property, which controls whether central Remote Desktop connection authorization policy (RD CAP) servers are used for controlling connection authorization policies for this server.<br/>                    |
| [**EnableLogEvent**](enablelogevent-win32-tsgatewayserversettings.md)                                                                             | Enables or disables logging of the specified event type.<br/>                                                                                                                                                                                              |
| [**EnableOnlyConsentCapableClients**](enableonlyconsentcapableclients-win32-tsgatewayserversettings.md)                                           | Sets the **OnlyConsentCapableClients** property.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                                      |
| [**EnableRequestSOH**](win32-tsgatewayserversettings-enablerequestsoh.md)                                                                         | This method is not supported starting with Windows Server 2016.<br/> **Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:** Enables or disables requests for a Statement of Health (SoH).<br/> <br/> |
| [**EnableTransport**](enabletransport-win32-tsgatewayserversettings.md)                                                                           | Enables or disables the specified transport.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/>                                                                                  |
| [**EnumAuthenticationPlugins**](enumauthenticationplugins-win32-tsgatewayserversettings.md)                                                       | Enumerates all registered authentication plug-ins.<br/> **Windows Server 2008:** This method is not available.<br/>                                                                                                                                  |
| [**EnumAuthorizationPlugins**](enumauthorizationplugins-win32-tsgatewayserversettings.md)                                                         | Enumerates all registered authorization plug-ins.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                                     |
| [**GetIPAndPort**](getipandport-win32-tsgatewayserversettings.md)                                                                                 | Obtains the listening IP address and port number for the specified transport.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/>                                                 |
| [**GetLogEventName**](getlogeventname-win32-tsgatewayserversettings.md)                                                                           | Returns the log event name for the specified log event index.<br/>                                                                                                                                                                                         |
| [**GetProtocolName**](getprotocolname-win32-tsgatewayserversettings.md)                                                                           | Returns the protocol name for the specified protocol index.<br/>                                                                                                                                                                                           |
| [**IsLogEventEnabled**](islogeventenabled-win32-tsgatewayserversettings.md)                                                                       | Indicates whether the specified event log type is enabled.<br/>                                                                                                                                                                                            |
| [**IsTransportEnabled**](istransportenabled-win32-tsgatewayserversettings.md)                                                                     | Determines whether the specified transport is enabled.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/>                                                                        |
| [**QueryCertContext**](win32-tsgatewayserversettings-querycertcontext.md)                                                                         | Indicates whether the specified certificate is installed.<br/>                                                                                                                                                                                             |
| [**RecycleRpcApplicationPools**](recyclerpcapplicationpools-win32-tsgatewayserversettings.md)                                                     | Recycles the RPC application pools in IIS.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                                            |
| [**RefreshCertContext**](win32-tsgatewayserversettings-refreshcertcontext.md)                                                                     | Refreshes the certificate that is used by the RD Gateway server.<br/>                                                                                                                                                                                      |
| [**SetAuthenticationPlugin**](setauthenticationplugin-win32-tsgatewayserversettings.md)                                                           | Sets the current authentication plug-in for the RD Gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                    |
| [**SetAuthenticationPluginAndRecycleRpcApplicationPools**](setauthenticationpluginandrecyclerpcapplicationpools-win32-tsgatewayserversettings.md) | Sets the current authentication plug-in for the RD Gateway server and recycles the RPC application pools in IIS.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                      |
| [**SetAuthorizationPlugin**](setauthorizationplugin-win32-tsgatewayserversettings.md)                                                             | Sets the current authorization plug-in for the RD Gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                     |
| [**SetCertificate**](setcertificate-win32-tsgatewayserversettings.md)                                                                             | Sets the certificate hash for HTTPS binding on port 443 in IIS.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                       |
| [**SetCertificateACL**](setcertificateacl-win32-tsgatewayserversettings.md)                                                                       | Sets the certificate access control lists (ACLs) for this server.<br/>                                                                                                                                                                                     |
| [**SetDefaultPluginsAndRecycleRpcApplicationPools**](setdefaultpluginsandrecyclerpcapplicationpools-win32-tsgatewayserversettings.md)             | Sets the current authentication and authorization plug-ins for the RD Gateway server and recycles the RPC application pools in IIS.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                   |
| [**SetEnforceChannelBinding**](setenforcechannelbinding-win32-tsgatewayserversettings.md)                                                         | Sets the **EnforceChannelBinding** property.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/>                                                                                  |
| [**SetIPAndPort**](setipandport-win32-tsgatewayserversettings.md)                                                                                 | Sets the listening IP address and port number for the specified transport.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/>                                                    |
| [**SetMaxConnections**](setmaxconnections-win32-tsgatewayserversettings.md)                                                                       | Sets the maximum number of allowed connections through RD Gateway. This method changes the **MaxConnections** and **UnlimitedConnections** properties.<br/>                                                                                                |
| [**SetSslBridging**](setsslbridging-win32-tsgatewayserversettings.md)                                                                             | Sets the type of SSL bridging to be used by the RD Gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                    |
| [**TSGRemoveAdminMsg**](tsgremoveadminmsg-win32-tsgatewayserversettings.md)                                                                       | Removes the administrative message for the gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                            |
| [**TSGRemoveConsentMsg**](tsgremoveconsentmsg-win32-tsgatewayserversettings.md)                                                                   | Removes the administrative message for the gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                            |
| [**TSGStoreAdminMsg**](tsgstoreadminmsg-win32-tsgatewayserversettings.md)                                                                         | Updates the administrative message for the gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                            |
| [**TSGStoreConsentMsg**](tsgstoreconsentmsg-win32-tsgatewayserversettings.md)                                                                     | Updates the consent message for the gateway server.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                                                                                   |



 

### Properties

The **Win32\_TSGatewayServerSettings** class has these properties.

<dl> <dt>

**adminMessageEndTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The administrative message end time.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**adminMessageStartTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The administrative message start time.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**adminMessageText**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The administrative message text.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthenticationPluginCLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The CLSID of the current authentication plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthenticationPluginDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the current authentication plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthenticationPluginName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the current authentication plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthorizationPluginCLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The CLSID of the current authorization plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthorizationPluginDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the current authorization plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**AuthorizationPluginName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the current authorization plug-in.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**CentralCAPEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether central RD CAP servers are used for controlling this server. This property can be changed by calling the [**EnableCentralCAP**](enablecentralcap-win32-tsgatewayserversettings.md) method.

</dd> <dt>

**CertHash**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the certificate hash for HTTPS binding on port 443 in IIS.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**consentMessageText**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The consent message text.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**EnforceChannelBinding**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if channel binding is enforced for the HTTP transport. This property value can be changed by using the [**SetEnforceChannelBinding**](setenforcechannelbinding-win32-tsgatewayserversettings.md) method.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available before Windows Server 2012.

</dd> <dt>

**IsConfigured**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if IIS and RPC settings required by the RD Gateway service are configured.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**MaxConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Returns the maximum number of connections that are allowed through RD Gateway. This property can be set by using the [**SetMaxConnections**](setmaxconnections-win32-tsgatewayserversettings.md) method.

</dd> <dt>

**MaximumAllowedConnectionsBySku**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of connections that the stock-keeping unit (SKU) allows.

</dd> <dt>

**MaxLogEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the maximum number of log events.

</dd> <dt>

**MaxProtocols**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of protocols supported by RD Gateway.

</dd> <dt>

**OnlyConsentCapableClients**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if only clients capable of consent messages are allowed to connect to the RD Gateway.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

<dt>

nonzero
</dt> <dd>

Only consent message capable clients can connect.

</dd> <dt>

zero
</dt> <dd>

Clients that are not consent message capable can also connect.

</dd> </dl>

</dd> <dt>

**RequestSOH**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported starting with Windows Server 2016.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

Specifies whether the server must request a Statement of Health (SoH) from the client. This property can be changed by using the [**EnableRequestSOH**](win32-tsgatewayserversettings-enablerequestsoh.md) method.

</dd> <dt>

**SkuName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the SKU.

</dd> <dt>

**SslBridging**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies which type of SSL bridging to be used by the RD Gateway server. This can be one of the following values.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

<dt>

0
</dt> <dd>

No SSL bridging.

</dd> <dt>

1
</dt> <dd>

HTTPS to HTTP bridging.

</dd> <dt>

2
</dt> <dd>

HTTPS to HTTPS bridging.

</dd> </dl>

</dd> <dt>

**UnlimitedConnections**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether an unlimited number of connections are allowed through RD Gateway. This property can be set by using the [**SetMaxConnections**](setmaxconnections-win32-tsgatewayserversettings.md) method.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to use this class.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnection**](win32-tsgatewayconnection.md)
</dt> <dt>

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayLoadBalancer**](win32-tsgatewayloadbalancer.md)
</dt> <dt>

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> </dl>

 

