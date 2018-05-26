---
title: Get method of the PS\_DAMgmtServer class
description: This cmdlet displays the configured Management servers. Management server here refers to patch servers, Domain Controllers and other servers.
audience: developer
ms.assetid: bf7d8960-02ba-4d61-9c31-e4b6fd5ed446
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAMgmtServer class
- PS_DAMgmtServer class, Get method
topic_type:
- apiref
api_name:
- PS_DAMgmtServer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DAMgmtServer class

This cmdlet displays the configured Management servers. Management server here refers to patch servers, Domain Controllers and other servers.

## Syntax


```mof
uint32 Get(
  [in]  string ComputerName,
  [in]  string Type,
  [out] string cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of management server to be listed. This can have the value of DC, SCCM, Manual or All. If not specified, only manual servers will be output.

<dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** ("Manual")


</dt> <dd></dd> <dt>

<span id="Sccm"></span><span id="sccm"></span><span id="SCCM"></span>

**Sccm** ("Sccm")


</dt> <dd></dd> <dt>

<span id="DC"></span><span id="dc"></span>

**DC** ("DC")


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** ("All")


</dt> <dd></dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

List of management servers configured

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

 

 





