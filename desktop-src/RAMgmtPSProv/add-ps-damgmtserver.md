---
title: Add method of the PS\_DAMgmtServer class
description: This cmdlet adds the specified Management servers to the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.
audience: developer
ms.assetid: f35e6054-c7f6-4914-adc1-a4e5f1b402e1
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DAMgmtServer class
- PS_DAMgmtServer class, Add method
topic_type:
- apiref
api_name:
- PS_DAMgmtServer.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DAMgmtServer class

This cmdlet adds the specified Management servers to the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.

## Syntax


```mof
uint32 Add(
  [in]  string  MgmtServer[],
  [in]  string  ComputerName,
  [in]  boolean PassThru,
  [out] string  cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*MgmtServer* \[in\]
</dt> <dd>

List of management servers specified by IPv4/IPv6 address, subnet or hostname

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the management server object which is the list of configured management servers. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

List of management servers that were successfully added to the DA deployment

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

 

 





