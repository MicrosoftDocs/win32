---
title: Add method of the PS\_RemoteAccessRadius class
description: This cmdlet adds a new external RADIUS server for one of the following purposes1. VPN authentication2. Accounting for DirectAccess and VPN3. OTP authentication for DirectAccess.
audience: developer
ms.assetid: 70c9b6cb-29ac-4c94-9637-114a078e7aaa
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_RemoteAccessRadius class
- PS_RemoteAccessRadius class, Add method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRadius.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_RemoteAccessRadius class

This cmdlet adds a new external RADIUS server for one of the following purposes1. VPN authentication2. Accounting for DirectAccess and VPN3. OTP authentication for DirectAccess

## Syntax


```mof
uint32 Add(
  [in]  string                   ServerName,
  [in]  string                   SharedSecret,
  [in]  string                   ComputerName,
  [in]  uint16                   Port,
  [in]  uint8                    Score,
  [in]  uint32                   Timeout,
  [in]  string                   Purpose,
  [in]  string                   AccountingOnOffMsg,
  [in]  string                   MsgAuthenticator,
  [in]  string                   EntrypointName,
  [in]  boolean                  PassThru,
  [out] RemoteAccessRadiusServer cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the external RADIUS server.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret between the VPN server and the specified external RADIUS server. Note that the secret is specified in clear text

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. If ComputerName is specified when adding a Radius server for authentication then it is added for the VPN server represented by ComputerName

</dd> <dt>

*Port* \[in\]
</dt> <dd>

Indicates the port number on which the RADIUS server is accepting authentication requests. Default is 1813

</dd> <dt>

*Score* \[in\]
</dt> <dd>

Indicates the initial score. The default is 30

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

The value is specified in seconds. Default is 5 secs

</dd> <dt>

*Purpose* \[in\]
</dt> <dd>

A Mandatory parameter that indicates the purpose for which the external RADIUS server is being added. Can be one of the following. 1. Authentication 2. Accounting. 3. Otp

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

*AccountingOnOffMsg* \[in\]
</dt> <dd>

Indicates whether the sending of accounting on/off messages should be enabled or disabled. Can take one of the following values 1. Enabled 2. Disabled; By default it is disabled. This parameter is applicable only when the Radius server is being added for Remote Access accounting

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*MsgAuthenticator* \[in\]
</dt> <dd>

Indicates whether usage of message authenticator should be enabled or disabled. Can take one of the following values. 1. Enabled. 2. Disabled; By default it is disabled. This parameter is applicable only when the Radius server is being added for VPN authentication

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment. It is applicable only to Radius server configuration for VPN authentication. It is not applicable to Radius accounting and OTP and hence is ignored when a user tries to add a radius server for these purposes. When the parameter is specified it indicates that the Radius server for VPN authentication should be added for that site. If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the radius server is added to it

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the remote access radius server object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output consists of the following. 1. External RADIUS server address (IPv4/IPv6) or hostname. 2. Purpose (VPN authentication, accounting, Inbox OTP authentication for DA) 3. RADIUS server properties (Shared secret, time-out, initial score, port no., status of accounting on/off messages - for accounting RADIUS, status of message authenticator - for authentication RADIUS)

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

 

 





