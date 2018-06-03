---
title: Set method of the PS\_DAMultiSite class
description: Configures global settings that are applied to all entry points in a multisite deployment.
audience: developer
ms.assetid: 52cb2f7e-dcdc-49c1-99cd-5a1e57f70d61
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DAMultiSite class
- PS_DAMultiSite class, Set method
topic_type:
- apiref
api_name:
- PS_DAMultiSite.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DAMultiSite class

Configures global settings that are applied to all entry points in a multisite deployment.

## Syntax


```mof
uint32 Set(
  [in]  string      ComputerName,
  [in]  string      GslbFqdn,
  [in]  string      ManualEntryPointSelectionAllowed,
  [in]  string      Name,
  [in]  boolean     PassThru,
  [out] DAMultiSite cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name or address (IPv4 or IPV6) of a server included in the multisite deployment for which parameters should be set. If no value is specified, the name of the local server on which the cmdlet runs is used.

</dd> <dt>

*GslbFqdn* \[in\]
</dt> <dd>

FQDN of the global load balancer configured to support the multisite deployment.

</dd> <dt>

*ManualEntryPointSelectionAllowed* \[in\]
</dt> <dd>

Specifies whether Windows 8 clients can manually select the entry point to which they connect. Can be set as Enabled or Disabled.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

The friendly name used to identify the multisite deployment.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the Multisite object which contains the entire Multisite configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Multisite deployment name. 2. Multisite deployment entry points each describes the list of servers associated with the entry points 3. Global load balancing FQDN (if required) 4. Whether remote access clients can manually select an entry point.

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

[**PS\_DAMultiSite**](ps-damultisite.md)
</dt> </dl>

 

 





