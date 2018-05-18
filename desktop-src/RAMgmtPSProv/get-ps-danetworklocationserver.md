---
title: Get method of the PS\_DANetworkLocationServer class
description: This cmdlet displays the detailed Network Location Server configuration.
audience: developer
ms.assetid: 'd88c1075-804b-49f6-9bc0-29197c8f10a4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DANetworkLocationServer class", "PS_DANetworkLocationServer class, Get method"]
topic_type:
- apiref
api_name:
- PS_DANetworkLocationServer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DANetworkLocationServer class

This cmdlet displays the detailed Network Location Server configuration.

## Syntax


```mof
uint32 Get(
  [in]  boolean                 CheckReachability,
  [in]  string                  ComputerName,
  [out] DANetworkLocationServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*CheckReachability* \[in\]
</dt> <dd>

If this parameter is specified then the cmdlet will perform a reachability check to the specified URL

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Where the Network Location Server is configured - on the DA server itself or on a different server. 2. URL (if it is configured on a different server). 3. Certificate (if it is configured on the DA server). 4. Reachability to Network Location Server (if on a different server whether the URL is reachable or not)

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

[**PS\_DANetworkLocationServer**](ps-danetworklocationserver.md)
</dt> </dl>

 

 





