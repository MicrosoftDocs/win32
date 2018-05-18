---
title: GetByName method of the PS\_DhcpServerv4Failover class
description: Gets the failover relationships configured on the server for the specific failover relationship name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb2def41-be81-42bb-ae53-b0be6a6f5369'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByName method", "GetByName method, PS_DhcpServerv4Failover class", "PS_DhcpServerv4Failover class, GetByName method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover.GetByName
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByName method of the PS\_DhcpServerv4Failover class

Gets the failover relationships configured on the server for the specific failover relationship name.

## Syntax


```mof
uint32 GetByName(
  [in]  string               ComputerName,
  [in]  string               Name[],
  [out] DhcpServerv4Failover cmdletOutput[]
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

Name(s) of the failover relationship(s) whose properties are to be returned

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
| Header<br/>                   | <dl> <dt>Wmp.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Failover**](ps-dhcpserverv4failover.md)
</dt> </dl>

 

 





