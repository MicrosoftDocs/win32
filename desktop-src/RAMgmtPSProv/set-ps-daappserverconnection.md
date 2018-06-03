---
title: Set method of the PS\_DAAppServerConnection class
description: This cmdlet configures the properties of the connection to application servers and the IPsec security traffic protection policies for the connection.
audience: developer
ms.assetid: 5a87771b-35df-4187-984d-cb6216505220
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DAAppServerConnection class
- PS_DAAppServerConnection class, Set method
topic_type:
- apiref
api_name:
- PS_DAAppServerConnection.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DAAppServerConnection class

This cmdlet configures the properties of the connection to application servers and the IPsec security traffic protection policies for the connection. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients and when no application servers have been configured.

## Syntax


```mof
uint32 Set(
  [in]  string                ConnectionType,
  [in]  string                TrafficProtection,
  [in]  string                ComputerName,
  [in]  boolean               PassThru,
  [out] DAAppServerConnection cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionType* \[in\]
</dt> <dd>

This parameter specifies the type of connection to corpnet and can take one of the following values: 1. NoE2EAuth: No end-to-end authentication required. 2. E2EAuthOnlyToAppServer: End-to-end authentication required only to the configured application servers and not to other servers in corpnet. 3. E2EAuthRequiredToAllServers: Access allowed only to the configured application servers via end-to-end authentication and no access to other servers in corpnet. If NoE2EAuth is specified the cmdlet automatically remove all the app server SGs and GPOs from the DA deployment and user has access to all corpnet servers over a full tunnel to the DA server. IPsec traffic protection is not applicable when the connection type is NoE2EAuth and hence cannot be configured

<dt>

<span id="NoE2EAuth"></span><span id="noe2eauth"></span><span id="NOE2EAUTH"></span>

**NoE2EAuth** ("NoE2EAuth")


</dt> <dd></dd> <dt>

<span id="E2EAuthOnlyToAppServer"></span><span id="e2eauthonlytoappserver"></span><span id="E2EAUTHONLYTOAPPSERVER"></span>

**E2EAuthOnlyToAppServer** ("E2EAuthOnlyToAppServer")


</dt> <dd></dd> <dt>

<span id="E2EAuthRequiredToAllServers"></span><span id="e2eauthrequiredtoallservers"></span><span id="E2EAUTHREQUIREDTOALLSERVERS"></span>

**E2EAuthRequiredToAllServers** ("E2EAuthRequiredToAllServers")


</dt> <dd></dd> </dl> </dd> <dt>

*TrafficProtection* \[in\]
</dt> <dd>

This parameter determines the property of the IPsec connection to the application servers and can take one of the following values. 1. Enable: This means traffic protection is enabled. 2. Disable: This means that traffic protection is disabled and only authentication will be performed. IPsec traffic protection is not applicable when the connection type is NoE2EAuth and hence cannot be configured

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the application server connection object which contains the properties of the connectivity to. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The application server connectivity properties are applicable to all app servers in the DA deployment

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAAppServerConnection**](ps-daappserverconnection.md)
</dt> </dl>

 

 





