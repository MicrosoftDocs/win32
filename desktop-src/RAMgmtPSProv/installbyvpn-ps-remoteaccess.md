---
title: InstallByVpn method of the PS\_RemoteAccess class
description: This cmdlet does the following 1.
audience: developer
ms.assetid: 4043a1b3-ed8c-4712-b7ba-fe87b847dec8
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InstallByVpn method
- InstallByVpn method, PS_RemoteAccess class
- PS_RemoteAccess class, InstallByVpn method
topic_type:
- apiref
api_name:
- PS_RemoteAccess.InstallByVpn
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InstallByVpn method of the PS\_RemoteAccess class

This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN).

## Syntax


```mof
uint32 InstallByVpn(
  [in]  string             VpnType,
  [in]  string             ComputerName,
  [in]  string             IPAddressRange[],
  [in]  string             RadiusServer,
  [in]  boolean            Legacy,
  [in]  string             SharedSecret,
  [in]  uint32             RadiusTimeout,
  [in]  uint8              RadiusScore,
  [in]  uint16             RadiusPort,
  [in]  string             MsgAuthenticator,
  [in]  boolean            PassThru,
  [in]  string             IPv6Prefix,
  [in]  string             EntrypointName,
  [out] RemoteAccessCommon cmdletOutput
);
```



## Parameters

<dl> <dt>

*VpnType* \[in\]
</dt> <dd>

The type of VPN to installed. You can set this value to Vpn or VpnS2S.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed.

</dd> <dt>

*IPAddressRange* \[in\]
</dt> <dd>

Specifying this parameter indicates that static pool IPv4 addressing should be enabled. The parameter contains an IP address range (consisting of a start IP and an end IP) from which IP addresses are allocated to VPN clients. In load balancing scenario only static pool IPv4 addressing is supported for VPN (DHCP address assignment is not supported). Hence it is mandatory to specify this parameter and an IPv4 address range should be provided for every node in the cluster. The address are specified in the following format: StartIPRange1, EndIPRange1, StartIPRange2, EndIPRange2, StartIPRange3, EndIPRange3 ... Essentially the start and end IPs of each of the ranges are specified one after the other and separated by commas.

</dd> <dt>

*RadiusServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the RADIUS server that is to be used for authentication. Specifying this parameter indicates that Radius authentication should be used for VPN.

</dd> <dt>

*Legacy* \[in\]
</dt> <dd>

**true** to install the legacy stack.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret between the Remote Access server and the specified external RADIUS server which is required for successful communication between the two servers. Note that the secret is specified in clear text. It is mandatory to specify this parameter if a Radius server is being configured for authentication.

</dd> <dt>

*RadiusTimeout* \[in\]
</dt> <dd>

The value is specified in seconds. Default is 5 secs. This parameter is applicable only when a Radius server is being configured for authentication.

</dd> <dt>

*RadiusScore* \[in\]
</dt> <dd>

Indicates the initial score. The default is 30. This parameter is applicable only when a Radius server is being configured for authentication.

</dd> <dt>

*RadiusPort* \[in\]
</dt> <dd>

Indicates the port number on which the RADIUS server is accepting authentication requests. Default is 1813. This parameter is applicable only when a Radius server is being configured for authentication.

</dd> <dt>

*MsgAuthenticator* \[in\]
</dt> <dd>

Indicates whether usage of message authenticator should be enabled or disabled. Can take one of the following values. 1. Enabled 2. Disabled. By default it is disabled. This parameter is applicable only when a Radius server is being configured for authentication.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the Remote Access object which contains the entire Remote Access (DA and VPN) configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*IPv6Prefix* \[in\]
</dt> <dd>

Specifying this parameter enables IPv6 address assignment for VPN and specifies the prefix to use for the addressing.

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multisite deployment where VPN needs to be installed. This is required in a scenario where DirectAccess with multisite is already deployed and a user wants to additionally deploy VPN. If entrypoint is not specified then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented using the ComputerName parameter.

If both entrypoint and computername are specified and the ComputerName does not belong to the site represented by the entrypoint then the entrypoint takes precedence and VPN is deployed at the site indicated by it.

Note that in a multisite deployment case VPN can only be installed one site at a time.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. When only DirectAccess is installed output will be the DA status, DA deployment mode and DA configuration portions and common configuration portions. 2. When only VPN is installed output will be the VPN status and VPN configuration and common configuration portions.

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

[**PS\_RemoteAccess**](ps-remoteaccess.md)
</dt> </dl>

 

 





