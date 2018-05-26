---
title: Update method of the PS\_DAMgmtServer class
description: This cmdlet updates the list of Management servers of the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.
audience: developer
ms.assetid: 75432686-6195-4b96-9548-07f171fc5ae1
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Update method
- Update method, PS_DAMgmtServer class
- PS_DAMgmtServer class, Update method
topic_type:
- apiref
api_name:
- PS_DAMgmtServer.Update
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Update method of the PS\_DAMgmtServer class

This cmdlet updates the list of Management servers of the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.

## Syntax


```mof
uint32 Update(
  [in]  boolean      PassThru,
  [in]  string       ComputerName,
  [out] DAMgmtServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the DAMgmtServers object which contains the list of changes to the management server list and the list of unchanged management servers. This cmdlet doesn't generate an object by default.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Output contains the following: 1) List of added domain controllers 2) List of removed domain controllers 3) List of unchanged domain controllers 4) List of added SCCM servers 5) List of removed SCCM servers 6) List of unchanged SCCM servers 7) List of manually entered servers that have resolved to new IP addresses 8) List of unchanged manually entered servers.

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

[**PS\_DAMgmtServer**](ps-damgmtserver.md)
</dt> </dl>

 

 





