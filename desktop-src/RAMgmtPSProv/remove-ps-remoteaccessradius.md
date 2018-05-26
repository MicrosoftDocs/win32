---
title: Remove method of the PS\_RemoteAccessRadius class
description: This cmdlet removes an external RADIUS server from being used for one of the following purposes1. VPN authentication2. Accounting for both DirectAccess and VPN3. OTP authentication for DirectAccess.
audience: developer
ms.assetid: a1b00937-139e-4dc3-8bc8-6ef6bf87ad6e
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_RemoteAccessRadius class
- PS_RemoteAccessRadius class, Remove method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRadius.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_RemoteAccessRadius class

This cmdlet removes an external RADIUS server from being used for one of the following purposes1. VPN authentication2. Accounting for both DirectAccess and VPN3. OTP authentication for DirectAccess

## Syntax


```mof
uint32 Remove(
  [in]  string                          ServerName,
  [in]  string                          Purpose,
  [in]  string                          ComputerName,
  [in]  boolean                         PassThru,
  [in]  string                          EntrypointName,
  [out] RemoteAccessRadiusServerPurpose cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the external RADIUS server that needs to be removed.

</dd> <dt>

*Purpose* \[in\]
</dt> <dd>

A Mandatory parameter that indicates the purpose for which the external RADIUS server is being removed. Can be one of the following: 1. Authentication 2. Accounting 3. Otp

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

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. If ComputerName is specified when removing a Radius server for authentication then it is removed for the VPN server represented by ComputerName.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

When this parameter is specified the cmdlet returns the Remote Access Radius Server object that represents the radius server that was removed. The cmdlet does not return an object if this parameter is not specified.

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment. It is applicable only to Radius server configuration for VPN authentication. It is not applicable to Radius accounting and OTP. When the parameter is specified it indicates that the Radius server for VPN authentication should be removed for that site. If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the radius server is removed from it

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output will be the address and the purpose of the RADIUS server that was removed and the purpose for which it was removed.

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

 

 





