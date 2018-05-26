---
title: SetByDisableComputerCertAuth method of the PS\_DAServer class
description: This cmdlet sets the properties specific to the DA server.
audience: developer
ms.assetid: 51a8420f-604d-4afd-a025-ecaee8598958
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByDisableComputerCertAuth method
- SetByDisableComputerCertAuth method, PS_DAServer class
- PS_DAServer class, SetByDisableComputerCertAuth method
topic_type:
- apiref
api_name:
- PS_DAServer.SetByDisableComputerCertAuth
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByDisableComputerCertAuth method of the PS\_DAServer class

This cmdlet sets the properties specific to the DA server.

## Syntax


```mof
uint32 SetByDisableComputerCertAuth(
  [in]  string   InternalIPv6Prefix[],
  [in]  string   ClientIPv6Prefix,
  [in]  string   ComputerName,
  [in]  string   TeredoState,
  [in]  string   ConnectToAddress,
  [in]  boolean  DisableComputerCertAuthentication,
  [in]  boolean  Force,
  [in]  boolean  PassThru,
  [out] DAServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*InternalIPv6Prefix* \[in\]
</dt> <dd>

Represents the native IPv6 prefixes used in the internal network (in corpnet). The list of prefixes specified always overwrites the existing list of prefixes. The list of internal IPv6 prefixes is a global configuration and applies to the entire DA deployment

</dd> <dt>

*ClientIPv6Prefix* \[in\]
</dt> <dd>

Represents the prefix from which IPv6 addresses are assigned to the connecting clients in case of IP-HTTPS.

The client IPv6 prefix configuration is applicable per-server or per-site (in the case of multisite deployments).

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*TeredoState* \[in\]
</dt> <dd>

This parameter is used to configure Teredo. It can take one of the following values 1. Enabled 2. Disabled Following are the behavioral aspects of Teredo State 1. Teredo can be enabled only if two consecutive IP addresses are present on the Internet interface of the server. 2. In a load balancing scenario a. If a 3rd party load balancer is being used and Teredo has to be enabled then the load balancer should have two consecutive IP addresses b. If Teredo needs to be enabled in a cluster then the cluster should be destroyed first and two consecutive IPs should be configured on the DA server 3. The Teredo configuration is applicable per-machine or per-site (in the case of multi-site deployments)

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*ConnectToAddress* \[in\]
</dt> <dd>

Indicates the DA server or NAT public (if DA server is deployed behind a NAT) address that clients connect to. Specified as hostname or IPv4 address When the ConnectTo address is changed the SSL certificate is also changed appropriately. Following are the rules associated with assigning a proper cert 1. Cmdlet looks for an appropriate SSL certificate on the machine. 2. If an appropriate SSL cert is not found then a self-signed cert is created. 3. In a load balancing scenario if all machines are up and an appropriate SSL cert is found only on some machines then the cmdlet fails the operation of changing the ConnectTo address. If none of the machines has a proper SSL cert then a self-signed cert is created on all machines and the ConnectTo change goes through. If one or more machines are down then the cert is updated only on the other machines. But the DA server GPO is updated to ensure that when these machines come up load balancing is in stopped state on them due to a cert mismatch. For the cert change (and in turn the ConnectTo address change) to take effect the admin needs to install a similar cert on them and re-run this cmdlet 4. In a multi-site scenario, the cmdlet doesn't create a self-signed cert and always expects a proper cert to be present on the machine itself The ConnectTo address is applicable per-machine or per-site (in the case of multi-site deployments)

</dd> <dt>

*DisableComputerCertAuthentication* \[in\]
</dt> <dd>

Using this switch parameter indicates that computer certificate authentication is to be disabled. 1. Computer certificate authentication cannot be disabled if health checks are enabled (HealthCheck parameter) 2. User authentication configuration is automatically changed to UserPasswd when computer cert authentication is disabled Computer certificate authentication is re-enabled by configured an IPsec root certificate using the IPsecRootCertificate parameter Disabling of computer certificate authentication is a global configuration that applies to the entire DA deployment

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes 1. ConnectTo change would result in a change in the SSL certificate 2. During SSL cert change if an appropriate cert is not found then a self-signed cert is created 3. Changing DirectAccess installation type

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object that conveys the properties of the DA server. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DA server properties 1. Authentication type 2. Internal IPv6 prefix 3. Client IPHTTPS IPv6 prefix 4. Usage of machine cert auth for 1st tunnel 5. IPsec cert 6. IPsec intermediate cert usage 7. Status of health check Common properties 1. SSL cert 2. ConnectTo address 3. Internal interface 4. Internet interface

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

[**PS\_DAServer**](ps-daserver.md)
</dt> </dl>

 

 





