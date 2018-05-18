---
title: Set method of the PS\_DAClient class
description: This cmdlet configures the properties related to a DA client.
audience: developer
ms.assetid: 'a7752ac5-2e42-4683-a9dd-e1ea4ed100c6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DAClient class", "PS_DAClient class, Set method"]
topic_type:
- apiref
api_name:
- PS_DAClient.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DAClient class

This cmdlet configures the properties related to a DA client.

## Syntax


```mof
uint32 Set(
  [in]  string           ComputerName,
  [in]  string           ForceTunnel,
  [in]  string           OnlyRemoteComputers,
  [in]  string           Downlevel,
  [in]  boolean          PassThru,
  [out] DAClientSettings cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*ForceTunnel* \[in\]
</dt> <dd>

Indicates whether force tunneling should be enabled or disabled. Can take one of the following values: Enable, Disable

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*OnlyRemoteComputers* \[in\]
</dt> <dd>

Allows a user to enable or disable deployment of DA only on laptops and notebooks (essentially, remote computers). Can take one of the following values: Enable, Disable

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*Downlevel* \[in\]
</dt> <dd>

Indicates whether appropriate policies should be deployed on downlevel clients (W7) clients such that they too can connect to the W8 DA Server. Can take one of the following values: Enable, Disable. This property can be configured only when multi-site is not deployed. If a user tries to configure it in a multi-site deployment the cmdlet throws an error

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the client settings object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Status of force tunneling 2. NRPT object corresponding to force tunneling 3. Status of policy to deploy DA only on laptops and notebooks and not on all computers in the domain 4. Status of whether appropriate policies should be deployed on downlevel clients (W7) clients such that they too can connect to the W8 DA Server

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

[**PS\_DAClient**](ps-daclient.md)
</dt> </dl>

 

 





