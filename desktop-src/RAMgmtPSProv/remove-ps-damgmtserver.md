---
title: Remove method of the PS\_DAMgmtServer class
description: This cmdlet removes the specified Management servers from the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.
audience: developer
ms.assetid: 1718ebbd-6eec-4780-a13e-6e36a5802bc9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DAMgmtServer class
- PS_DAMgmtServer class, Remove method
topic_type:
- apiref
api_name:
- PS_DAMgmtServer.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DAMgmtServer class

This cmdlet removes the specified Management servers from the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers.

## Syntax


```mof
uint32 Remove(
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

List of management servers that were successfully removed from the DA deployment

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

 

 





