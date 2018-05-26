---
title: Remove method of the PS\_DhcpServerv4FailoverScope class
description: Removes the specified scopes from the failover relationship.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13d3c83f-15b1-43b4-b793-3c5d3592e23e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4FailoverScope class
- PS_DhcpServerv4FailoverScope class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FailoverScope.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4FailoverScope class

Removes the specified scopes from the failover relationship. For any specified scope which is not part of the specified failover relationship or which do not exist, a NTE will be returned. This processing will be done up front before adding the valid scopes to the failover relationship.

## Syntax


```mof
uint32 Remove(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  string               ScopeId[],
  [in]  boolean              Force,
  [in]  boolean              PassThru,
  [out] DhcpServerv4Failover cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the failover relationships from which the scopes are to be removed.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifiers, in IPv4 address format, which are to be removed from the failover relationship.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, removes the failover relationship even if the failover relationship is not in **Normal** state.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Failover**](dhcpserverv4failover.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4FailoverScope**](ps-dhcpserverv4failoverscope.md)
</dt> </dl>

 

 





