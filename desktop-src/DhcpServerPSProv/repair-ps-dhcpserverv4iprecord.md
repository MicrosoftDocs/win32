---
title: Repair method of the PS\_DhcpServerv4IPRecord class
description: Reconciles DHCP server database for the specified scopes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e442215f-8068-40ef-9603-7dd542b378fc
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Repair method
- Repair method, PS_DhcpServerv4IPRecord class
- PS_DhcpServerv4IPRecord class, Repair method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4IPRecord.Repair
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Repair method of the PS\_DhcpServerv4IPRecord class

Reconciles DHCP server database for the specified scopes.The cmdlet alias is Reconcile-DhcpServerv4IPRecord.

## Syntax


```mof
uint32 Repair(
  [in]  string                ComputerName,
  [in]  string                ScopeId[],
  [in]  boolean               ReportOnly,
  [in]  boolean               Force,
  [out] DhcpServerv4IPRecords cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

List of scopes to be reconciled.

</dd> <dt>

*ReportOnly* \[in\]
</dt> <dd>

If specified, all the lease inconsistencies for specified scopes will be listed in a DhcpServerv4IPRecord\[\] object.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified default confirmation should not be sought.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4IPRecord**](dhcpserverv4iprecords.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                           |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4IPRecord**](ps-dhcpserverv4iprecord.md)
</dt> </dl>

 

 





