---
title: Add method of the PS\_DhcpServerv4Filter class
description: Adds a MAC address filter to the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd1628363-bba1-4d2d-bdf8-2ada75437bd4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4Filter class", "PS_DhcpServerv4Filter class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Filter.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4Filter class

Adds a MAC address filter to the DHCP server.

## Syntax


```mof
uint32 Add(
  [in]  string             ComputerName,
  [in]  string             Description,
  [in]  string             MacAddress[],
  [in]  string             List,
  [in]  boolean            Force,
  [in]  boolean            PassThru,
  [out] DhcpServerv4Filter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string for the MAC address filter being added

</dd> <dt>

*MacAddress* \[in\]
</dt> <dd>

MAC address(es) which are to be added to the MAC address filter list

</dd> <dt>

*List* \[in\]
</dt> <dd>

The list to which the MAC address(es) is/are to be added. Permissible values for this parameter are Allow and Deny.

<dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** ("Allow")


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** ("Deny")


</dt> <dd></dd> </dl> </dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, if the MAC address(es) is already present in the allow or deny list, the same will be deleted and the new entry created for the same. This would be useful in the case where the MAC address specified is already present in one list (e.g. allow) and the same MAC address now needs to be added to the other list (e.g. deny) instead. If not specified, the cmdlet will fail if the specified MAC address is already present in any of the lists.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Filter**](dhcpserverv4filter.md) class.

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

[**PS\_DhcpServerv4Filter**](ps-dhcpserverv4filter.md)
</dt> </dl>

 

 





