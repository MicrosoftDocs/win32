---
title: InstallByDirectAccess method of the PS\_RemoteAccess class
description: This cmdlet does the following 1.
audience: developer
ms.assetid: a57cd840-34d7-4a41-96e0-cf02f5f42d6f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InstallByDirectAccess method
- InstallByDirectAccess method, PS_RemoteAccess class
- PS_RemoteAccess class, InstallByDirectAccess method
topic_type:
- apiref
api_name:
- PS_RemoteAccess.InstallByDirectAccess
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InstallByDirectAccess method of the PS\_RemoteAccess class

This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN).

## Syntax


```mof
uint32 InstallByDirectAccess(
  [in]  string             ComputerName,
  [in]  string             DAInstallType,
  [in]  string             ClientGpoName,
  [in]  string             InternalInterface,
  [in]  string             InternetInterface,
  [in]  uint8              NlsCertificate[],
  [in]  string             NlsUrl,
  [in]  boolean            NoPrerequisite,
  [in]  string             ServerGpoName,
  [in]  string             ConnectToAddress,
  [in]  boolean            DeployNat,
  [in]  boolean            PassThru,
  [in]  boolean            Force,
  [out] RemoteAccessCommon cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed.

</dd> <dt>

*DAInstallType* \[in\]
</dt> <dd>

Indicates the configuration in which DirectAccess should be installed. Can take one of the following values. 1. FullInstall - DirectAccess is installed for both remote access and for the management of remote clients. 2. ManageOut - DirectAccess is installed only for the management of remote clients.

</dd> <dt>

*ClientGpoName* \[in\]
</dt> <dd>

Names of the client GPO. The GPO name is specified in DOMAIN\\GPO\_NAME format. Domain can be one of the domains deployed in the corporate network. If a GPO name is not specified then by default a GPO with following name is created in the DA server's domain: \[domain\] client policy for DirectAccess connection to workplace.

</dd> <dt>

*InternalInterface* \[in\]
</dt> <dd>

Name of the corpnet facing interface. In a single-NIC configuration the same name is specified for both internal and Internet interfaces. If name is not specified then cmdlet tries to detect the internal interface automatically.

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

Name of the Internet facing interface. In a single-NIC configuration the same name is specified for both internal and Internet interfaces. If name is not specified then cmdlet tries to detect the Internet interface automatically.

</dd> <dt>

*NlsCertificate* \[in\]
</dt> <dd>

Indicates that the Network Location Server should be configured on the DirectAccess server itself and represents the certificate to be used. The subject name of the cert should match the internal interface of the DA server.

</dd> <dt>

*NlsUrl* \[in\]
</dt> <dd>

Specifying this parameter indicates that the NLS is present on a different and represents the URL on the server that will be used to provide clients with location information.

</dd> <dt>

*NoPrerequisite* \[in\]
</dt> <dd>

This parameter when specified indicates that a prerequisite check should not be performed for DirectAccess.

</dd> <dt>

*ServerGpoName* \[in\]
</dt> <dd>

Name of the GPO for the DirectAccess server. Specified in the format DOMAIN\\GPO\_NAME. If a name is not specified then a GPO with the following name is created in the DA server's domain: \[domain\] server policy for DirectAccess connection to workplace.

</dd> <dt>

*ConnectToAddress* \[in\]
</dt> <dd>

Indicates the DA server or NAT public address that clients connect to. Specified as hostname or IPv4 address.

</dd> <dt>

*DeployNat* \[in\]
</dt> <dd>

Specifying this switch parameter indicates that DA should be deployed behind a NAT. In a single-NIC configuration scenario the DA server is always deployed behind a NAT and hence there is no need to specify this switch parameter.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the Remote Access object which contains the entire Remote Access (DA and VPN) configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes. 1. If an appropriate cert for NLS is not found then a self-signed cert is created. 2. If an appropriate SSL cert is not found then a self-signed cert is created.

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

 

 





