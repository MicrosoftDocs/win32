---
title: PollDsNow method of the DfsrConfig class
description: Polls the Active Directory for configuration changes and applies any changes to the service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9b463c24-f95a-4753-a1c8-a32b402d2ff4
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PollDsNow method Distributed File System Replication
- PollDsNow method Distributed File System Replication , DfsrConfig class
- DfsrConfig class Distributed File System Replication , PollDsNow method
topic_type:
- apiref
api_name:
- DfsrConfig.PollDsNow
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PollDsNow method of the DfsrConfig class

Polls the Active Directory for configuration changes and applies any changes to the service.

## Syntax


```mof
uint32 PollDsNow(
  [in] string DcDnsName
);
```



## Parameters

<dl> <dt>

*DcDnsName* \[in\]
</dt> <dd>

Fully qualified domain naming system (DNS) name of the domain controller to connect to. This parameter is optional.

</dd> </dl>

## Return value

This method returns one of the [CONFIG\_STATUS return codes](config-status-return-codes.md).

## Remarks

By default, DFSR polls the Active Directory every hour for changes in configuration.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrConfig**](dfsrconfig.md)
</dt> </dl>

 

 





