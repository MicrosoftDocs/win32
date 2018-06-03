---
title: Set method of the PS\_RemoteAccess class
description: Updates the configuration that is common to both DirectAccess and VPN viz. the following1. SSL certificate2. Internal interface 3. Internet interface.
audience: developer
ms.assetid: 67e87bdb-cc83-41d3-8030-3c237a782705
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_RemoteAccess class
- PS_RemoteAccess class, Set method
topic_type:
- apiref
api_name:
- PS_RemoteAccess.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_RemoteAccess class

Updates the configuration that is common to both DirectAccess and VPN viz. the following1. SSL certificate2. Internal interface 3. Internet interface.

## Syntax


```mof
uint32 Set(
  [in]  uint8              SslCertificate[],
  [in]  string             ComputerName,
  [in]  string             InternetInterface,
  [in]  string             InternalInterface,
  [in]  uint64             CapacityKbps,
  [in]  boolean            UseHttp,
  [in]  boolean            Force,
  [in]  boolean            PassThru,
  [out] RemoteAccessCommon cmdletOutput
);
```



## Parameters

<dl> <dt>

*SslCertificate* \[in\]
</dt> <dd>

Specifies the certificate that will be used to secure remote clients connectivity over HTTPS (in case of DirectAccess) or SSTP (in case of VPN): 1. SSL certificate changes are allowed only within the bounds of the current value of the ConnectTo address (configurable through the set-daserver cmdlet), i.e., the subject name of the new cert should always match ConnectTo. All other certs are rejected and the cmdlet errors out, even if all other criteria for an SSL certificate are satisfied. This behavior is applicable irrespective of whether NAT is deployed or not and whether the server has a single NIC or two NICs. 2. In a network load balancing scenario the changes take effect on all nodes. Hence, the specified certificate is required to be present on all nodes in the cluster. a. If the certificate is not found on one or more nodes then the cmdlet errors out. b. If one or more nodes are down when changing the certificate then the change applies only on the nodes that are up. But the DA server GPO is updated to ensure that when these machines come up load balancing is in stopped state on them due to a cert mismatch. For the cert change to take effect, the admin needs to install a similar cert on them and re-run this cmdlet.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. If ComputerName is specified then the configuration changes take place on that Remote Access server.

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

Name of the Internet facing interface. 1. In a single-NIC configuration if the admin wants to change the interface then the new name should be specified for both InternalInterface and InternetInterface parameters. 2. When changing the Internet interface, if the IP address of the ConnectTo is known, the IP address of the specified interface is compared with the ConnectTo address. If there is a mismatch then the the interface is not changed and the cmdlet errors out. If only the name of ConnectTo is known and it cannot be resolved or if the Remote Access server is deployed behind NAT then it is assumed that the new interface matches with the ConnectTo address.

</dd> <dt>

*InternalInterface* \[in\]
</dt> <dd>

Name of the corpnet facing interface. 1. In a single-NIC configuration if the admin wants to change the interface then the new name should be specified for both InternalInterface and InternetInterface parameters.

</dd> <dt>

*CapacityKbps* \[in\]
</dt> <dd>

The bandwidth capacity of the remote access configuration.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*UseHttp* \[in\]
</dt> <dd>

**True** to use HTTP; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes. 1. Changing the interfaces: this results in re-configuration which is time consuming and the server cannot accept connections during this time.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object the contains the configuration common to DA and VPN. By default this cmdlet does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Entire Remote Access configuration consisting of DA, VPN and common configuration: Object consists of the following. 1. Status of DirectAccess - installed or uninstalled. 2. Deployment mode for DirectAccess - Remote Access and management of remote clients OR Management of remote clients. 3. DirectAccess configuration. 4. Status of VPN - installed or uninstalled. 5. VPN configuration. 6. Configuration common to DirectAccess and VPN. Note that if either VPN or DA is not installed its configuration is not displayed. The DirectAccess configuration will be a collation of the output of all other DirectAccess configuration cmdlets. The VPN configuration contains the following. 1. Address Assignment type - DHCP or StaticPool. 2. Static Pool - all the configured IP address ranges, if static pool address assignment is configured. 3. Authentication type - Windows, LocalNPS or ExternalRADIUS. 4. External RADIUS servers - IPv4/IPv6 address or hostname of the RADIUS servers used for authentication, if external RADIUS authentication is configured. The common configuration contains the following. 1. Internet Interface - name of the Internet facing interface. 2. Internal Interface - name of the intranet facing interface, this will not be displayed in case of single NIC config. 3. ConnectTo address. 4. SSL certificate.

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

 

 





