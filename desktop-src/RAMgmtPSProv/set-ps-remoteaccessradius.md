---
title: Set method of the PS\_RemoteAccessRadius class
description: This cmdlet edits the properties associated with an external RADIUS server being used for the following1. VPN authentication2. Accounting for DirectAccess and VPN 3. OTP authentication for DirectAccess.
audience: developer
ms.assetid: 43cb07b6-a7fb-49a3-81ad-d985e592791f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_RemoteAccessRadius class
- PS_RemoteAccessRadius class, Set method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRadius.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_RemoteAccessRadius class

This cmdlet edits the properties associated with an external RADIUS server being used for the following1. VPN authentication2. Accounting for DirectAccess and VPN 3. OTP authentication for DirectAccess.

## Syntax


```mof
uint32 Set(
  [in]  string                   ComputerName,
  [in]  string                   Purpose,
  [in]  uint16                   Port,
  [in]  uint8                    Score,
  [in]  string                   ServerName,
  [in]  uint32                   Timeout,
  [in]  string                   SharedSecret,
  [in]  string                   AccountingOnOffMsg,
  [in]  string                   MsgAuthenticator,
  [in]  string                   EntrypointName,
  [in]  boolean                  PassThru,
  [out] RemoteAccessRadiusServer cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed.

</dd> <dt>

*Purpose* \[in\]
</dt> <dd>

A mandatory parameter that indicates the purpose of the RADIUS server for which the settings are being modified. Can be one of the following. 1. Authentication. 2. Accounting. 3. Otp.

<dt>

<span id="Authentication"></span><span id="authentication"></span><span id="AUTHENTICATION"></span>

**Authentication** ("Authentication")


</dt> <dd></dd> <dt>

<span id="Accounting"></span><span id="accounting"></span><span id="ACCOUNTING"></span>

**Accounting** ("Accounting")


</dt> <dd></dd> <dt>

<span id="Otp"></span><span id="otp"></span><span id="OTP"></span>

**Otp** ("Otp")


</dt> <dd></dd> </dl> </dd> <dt>

*Port* \[in\]
</dt> <dd>

Indicates the port number on which the RADIUS server is accepting authentication requests

</dd> <dt>

*Score* \[in\]
</dt> <dd>

Indicates the initial score.

</dd> <dt>

*ServerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the external RADIUS server whose properties are being modified for the specified purpose.

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

The value is specified in seconds

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret between the VPN server and the specified external RADIUS server. Note that the secret is specified in clear text

</dd> <dt>

*AccountingOnOffMsg* \[in\]
</dt> <dd>

Indicates whether the sending of accounting on/off messages should be enabled or disabled. Can take one of the following values. 1. Enabled. 2. Disabled. This parameter is applicable only when the Radius server is being added for Remote Access accounting

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*MsgAuthenticator* \[in\]
</dt> <dd>

Indicates whether usage of message authenticator should be enabled or disabled. Can take one of the following values. 1. Enabled. 2. Disabled. This parameter is applicable only when the Radius server is being added for VPN authentication

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment. It is applicable only to Radius server configuration for VPN authentication. It is not applicable to Radius accounting and OTP. If this parameter is specified when editing it indicates that the properties of the Radius server for VPN authentication should be modified for that site. If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the radius server is added to it.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the remote access radius server object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Status of message authenticator: if the Radius server was modified for accounting or OTP then this property is always blank.

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

[**PS\_RemoteAccessRadius**](ps-remoteaccessradius.md)
</dt> </dl>

 

 





