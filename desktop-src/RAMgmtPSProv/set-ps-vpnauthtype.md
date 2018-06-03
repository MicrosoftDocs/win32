---
title: Set method of the PS\_VpnAuthType class
description: This cmdlet sets the authentication type to be used for VPN.
audience: developer
ms.assetid: 24fd58b2-234e-409d-b262-d09415db128b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnAuthType class
- PS_VpnAuthType class, Set method
topic_type:
- apiref
api_name:
- PS_VpnAuthType.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_VpnAuthType class

This cmdlet sets the authentication type to be used for VPN.

## Syntax


```mof
uint32 Set(
  [in]  string  Type,
  [in]  string  RadiusServer,
  [in]  string  SharedSecret,
  [in]  uint32  RadiusTimeout,
  [in]  uint8   RadiusScore,
  [in]  uint16  RadiusPort,
  [in]  string  ComputerName,
  [in]  string  MsgAuthenticator,
  [in]  string  EntrypointName,
  [in]  boolean PassThru,
  [out] VpnAuth cmdletOutput
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Indicates the authentication type. This can be one of the following values.

<dt>

<span id="Windows"></span><span id="windows"></span><span id="WINDOWS"></span>

**Windows** ("Windows")


</dt> <dd></dd> <dt>

<span id="ExternalRadius"></span><span id="externalradius"></span><span id="EXTERNALRADIUS"></span>

**ExternalRadius** ("ExternalRadius")


</dt> <dd></dd> </dl> </dd> <dt>

*RadiusServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the external RADIUS server that is used for accounting. This parameter can be configured only if the *Type* parameter is specified to be ExternalRADIUS. If there are no pre-existing RADIUS servers configured for authentication (see cmdlet description for more details), then it is mandatory to specify a Radius server and its corresponding shared secret. Default values can be used for the other parameters

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret between the Remote Access server and the specified external RADIUS server. This shared secret is required for successful communication between the two servers. Note that the secret is specified in clear text. This parameter can be configured only if the *Type* parameter is specified to be ExternalRADIUS. If there are no pre-existing RADIUS servers configured for authentication, then it is mandatory to configure one by specifying at least one Radius server and shared secret. Default values can be used for the other parameters.

</dd> <dt>

*RadiusTimeout* \[in\]
</dt> <dd>

The value is specified in seconds. Default is 5 secs. This parameter can be configured only if the *Type* parameter is specified to be ExternalRADIUS.

</dd> <dt>

*RadiusScore* \[in\]
</dt> <dd>

Indicates the initial score. The default is 30. This parameter can be configured only if the Type parameter is specified to be ExternalRADIUS

</dd> <dt>

*RadiusPort* \[in\]
</dt> <dd>

Indicates the port number on which the RADIUS server is accepting authentication requests. Default is 1813. This parameter can be configured only if the *Type* parameter is specified to be ExternalRADIUS.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the VPN server machine specific tasks should be executed. If ComputerName is specified then the authentication type is configured for that VPN server

</dd> <dt>

*MsgAuthenticator* \[in\]
</dt> <dd>

Indicates whether usage of message authenticator should be enabled or disabled. Can take one of the following values. 1. Enabled. 2. Disabled. By default it is disabled. This parameter can be configured only if the Type parameter is specified to be ExternalRADIUS

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment for which the authentication type needs to be configured. If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the VPN Auth policy object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Authentication type (Windows, ExternalRADIUS, LocalNPS). 2. Configured RADIUS servers (if external RADIUS authentication was set)

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

[**PS\_VpnAuthType**](ps-vpnauthtype.md)
</dt> </dl>

 

 





