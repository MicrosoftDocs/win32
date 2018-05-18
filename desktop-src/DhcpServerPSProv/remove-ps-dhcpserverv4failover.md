---
title: Remove method of the PS\_DhcpServerv4Failover class
description: Removes the specified failover relationship(s). The failover relationship will be removed from both the DHCP servers which are part of this failover relationship.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '40a52f29-d0a7-45d1-89dd-3460e19dff76'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerv4Failover class", "PS_DhcpServerv4Failover class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerv4Failover class

Removes the specified failover relationship(s). The failover relationship will be removed from both the DHCP servers which are part of this failover relationship.

## Syntax


```mof
uint32 Remove(
  [in]  string               Name[],
  [in]  boolean              Force,
  [in]  boolean              PassThru,
  [in]  string               ComputerName,
  [out] DhcpServerv4Failover cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name(s) of the failover relationships which are to be removed

</dd> <dt>

*Force* \[in\]
</dt> <dd>

User confirmation of this action is sought by default. If -Force is specified, default user confirmation will not be sought.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Failover**](dhcpserverv4failover.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Failover**](ps-dhcpserverv4failover.md)
</dt> </dl>

 

 





