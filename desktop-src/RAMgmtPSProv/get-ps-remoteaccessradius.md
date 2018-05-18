---
title: Get method of the PS\_RemoteAccessRadius class
description: This cmdlet displays the list of the following types of RADIUS servers 1. Radius for VPN authentication 2. Radius for DirectAccess and VPN Accounting3. Radius for OTP authentication for DirectAccess.
audience: developer
ms.assetid: 'aa1d79be-0189-4121-b906-19d728b52b67'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_RemoteAccessRadius class", "PS_RemoteAccessRadius class, Get method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessRadius.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_RemoteAccessRadius class

This cmdlet displays the list of the following types of RADIUS servers 1. Radius for VPN authentication 2. Radius for DirectAccess and VPN Accounting3. Radius for OTP authentication for DirectAccess

## Syntax


```mof
uint32 Get(
  [in]  string                   Purpose,
  [in]  string                   ComputerName,
  [in]  string                   EntrypointName,
  [out] RemoteAccessRadiusServer cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Purpose* \[in\]
</dt> <dd>

Indicates the purpose of the external RADIUS server. Can be one of the following: 1. Authentication. 2. Accounting. 3. Otp. If this parameter is omitted then RADIUS server(s) existing for all of the above purposes will be presented.

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

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Name of the entrypoint.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output consists of the list of external RADIUS servers being used for the specified purpose and their properties. If the server is used for both purposes then the RADIUS server is displayed twice with the properties for each purpose. 1. IPv4/IPv6 address or hostname of the RADIUS server. 2. Purpose (authentication (RRAS or OTP for DA) or accounting). 3. Properties of the RADIUS server for this purpose (Shared secret, time-out - for accounting and RRAS auth, initial score - for accounting and RRAS auth, port no., status of accounting on/off messages - for accounting RADIUS, status of message authenticator - for authentication RADIUS)

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

[**PS\_RemoteAccessRadius**](ps-remoteaccessradius.md)
</dt> </dl>

 

 





