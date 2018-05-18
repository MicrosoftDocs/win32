---
title: SetByEnableComputerCertAuth method of the PS\_DAServer class
description: This cmdlet sets the properties specific to the DA server.
audience: developer
ms.assetid: '9387937c-88a3-458a-91fb-ce5f3a32b49b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByEnableComputerCertAuth method", "SetByEnableComputerCertAuth method, PS_DAServer class", "PS_DAServer class, SetByEnableComputerCertAuth method"]
topic_type:
- apiref
api_name:
- PS_DAServer.SetByEnableComputerCertAuth
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# SetByEnableComputerCertAuth method of the PS\_DAServer class

This cmdlet sets the properties specific to the DA server.

## Syntax


```mof
uint32 SetByEnableComputerCertAuth(
  [in]  string   InternalIPv6Prefix[],
  [in]  string   UserAuthentication,
  [in]  string   ComputerName,
  [in]  string   TeredoState,
  [in]  string   ConnectToAddress,
  [in]  uint8    IPsecRootCertificate[],
  [in]  boolean  IntermediateRootCertificate,
  [in]  string   EntrypointName,
  [in]  string   ClientIPv6Prefix,
  [in]  boolean  Force,
  [in]  string   HealthCheck,
  [in]  boolean  PassThru,
  [out] DAServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*InternalIPv6Prefix* \[in\]
</dt> <dd>

Represents the native IPv6 prefixes used in the internal network (in corpnet). The list of prefixes specified always overwrites the existing list of prefixes. The list of internal IPv6 prefixes is a global configuration and applies to the entire DA deployment

</dd> <dt>

*UserAuthentication* \[in\]
</dt> <dd>

This parameter sets the type of authentication that is used to authenticate a DA user. It can take one of the following values 1. TwoFactor 2. UserPasswd Here two-factor refers to certificate authentication or OTP authentication. However, note that to setup OTP authentication enabling two-factor alone is not enough. It needs to be configured separately using the DAOtpAuth cmdlets User authentication is a global configuration that applies to the entire DA deployment

<dt>

<span id="TwoFactor"></span><span id="twofactor"></span><span id="TWOFACTOR"></span>

**TwoFactor** ("TwoFactor")


</dt> <dd></dd> <dt>

<span id="UserPasswd"></span><span id="userpasswd"></span><span id="USERPASSWD"></span>

**UserPasswd** ("UserPasswd")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*TeredoState* \[in\]
</dt> <dd>

This parameter is used to configure Teredo. Following are the behavioral aspects of Teredo State 1. Teredo can be enabled only if two consecutive IP addresses are present on the Internet interface of the server. 2. In a load balancing scenario a. If a 3rd party load balancer is being used and Teredo has to be enabled then the load balancer should have two consecutive IP addresses b. If Teredo needs to be enabled in a cluster then the cluster should be destroyed first and two consecutive IPs should be configured on the DA server 3. The Teredo configuration is applicable per-machine or per-site (in the case of multi-site deployments)

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*ConnectToAddress* \[in\]
</dt> <dd>

Indicates the DA server or NAT public (if DA server is deployed behind a NAT) address that clients connect to. Specified as hostname or IPv4 address When the **ConnectToAddress** is changed the SSL certificate is also changed appropriately. Following are the rules associated with assigning a proper cert 1. Cmdlet looks for an appropriate SSL certificate on the machine. 2. If an appropriate SSL cert is not found then a self-signed cert is created. 3. In a load balancing scenario if all machines are up and an appropriate SSL cert is found only on some machines then the cmdlet fails the operation of changing the **ConnectToAddress**. If none of the machines has a proper SSL cert then a self-signed cert is created on all machines and the **ConnectToAddress** change goes through. If one or more machines are down then the cert is updated only on the other machines. But the DA server GPO is updated to ensure that when these machines come up load balancing is in stopped state on them due to a cert mismatch. For the cert change (and in turn the **ConnectToAddress** change) to take effect the admin needs to install a similar cert on them and re-run this cmdlet 4. In a multi-site scenario, the cmdlet doesn't create a self-signed cert and always expects a proper cert to be present on the machine itself The **ConnectToAddress** is applicable per-machine or per-site (in the case of multi-site deployments)

</dd> <dt>

*IPsecRootCertificate* \[in\]
</dt> <dd>

Specifies the root certificate to which DA and VPN clients should chain. This parameter is used 1. to change the IPsec root certificate or 2. to enable PKI if there is no IPsec root certificate already configured IPsec root certificate is a global configuration, i.e. the same cert is found on all nodes in the DA deployment. Hence, configuring the root certificate updates it on all DA servers. If the specified cert is not found on one or more servers then the IPsec root cert is not updated on any of the servers and the cmdlet errors out. In a load balancing scenario if one or more nodes is down when the cmdlet is run then the cert is only updated on the nodes that are up. But the DA server GPO is updated to ensure that when these machines come up load balancing is in stopped state on them due to a cert mismatch. For the cert change to take effect, the admin needs to install a similar cert on them and re-run this cmdlet

</dd> <dt>

*IntermediateRootCertificate* \[in\]
</dt> <dd>

This switch parameter when specified indicates that the IPsec root certificate specified is an intermediate root certificate

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment and when specified indicates that the DA server properties should be configured for that site. Only the following properties are applicable at the site level. The rest of them are global properties and hence the entrypoint parameter has no meaning to them.

-   **ClientIPv6Prefix**
-   **ConnectToAddress**
-   **TeredoState**

If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter.

If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it.

</dd> <dt>

*ClientIPv6Prefix* \[in\]
</dt> <dd>

Represents the prefix from which IPv6 addresses are assigned to the connecting clients in case of IP-HTTPS.

The client IPv6 prefix configuration is applicable per-server or per-site (in the case of multisite deployments).

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes

1. ConnectTo change would result in a change in the SSL certificate

2. During SSL cert change if an appropriate cert is not found then a self-signed cert is created

3. Changing DirectAccess installation type

</dd> <dt>

*HealthCheck* \[in\]
</dt> <dd>

This parameter is not supported starting with Windows Server 2016.

**Windows Server 2012 R2 and Windows Server 2012:** Indicates whether health check for DirectAccess clients is enabled.

This parameter is used to enable/disable health checks for DirectAccess clients.

Following are important behavioral aspects for health checks:

-   In order to enable health checks machine cert authentication should already be enabled, i.e., an IPsec root certificate should be deployed
-   On disabling health checks if neither of the following is already enabled then machine certificate authentication is automatically disabled:

    -   Multi-site, i.e. multi-site is not deployed/enabled
    -   User authentication is not two-factor
    -   Support for down-level clients is not enabled

-   *Healthcheck* is a global configuration that applies to the entire DA deployment

<dt>



 ("Enabled")


</dt> <dd></dd> <dt>



 ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object that conveys the properties of the DA server. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DA server properties

1. Authentication type

2. Internal IPv6 prefix

3. Client IPHTTPS IPv6 prefix

4. Usage of machine cert auth for 1st tunnel

5. IPsec cert

6. IPsec intermediate cert usage

7. Status of health check

Common properties

1. SSL cert

2. ConnectTo address

3. Internal interface

4. Internet interface

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAServer**](ps-daserver.md)
</dt> </dl>

 

 





