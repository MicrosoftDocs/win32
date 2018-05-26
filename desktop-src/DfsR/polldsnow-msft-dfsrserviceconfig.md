---
title: PollDsNow method of the MSFT\_DfsrServiceConfig class
description: Polls Active Directory Domain Services and applies any changes to the service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c8ce074-6f52-47b4-a986-79fc80d27ab1
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PollDsNow method Distributed File System Replication
- PollDsNow method Distributed File System Replication , MSFT_DfsrServiceConfig class
- MSFT_DfsrServiceConfig class Distributed File System Replication , PollDsNow method
topic_type:
- apiref
api_name:
- MSFT_DfsrServiceConfig.PollDsNow
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PollDsNow method of the MSFT\_DfsrServiceConfig class

Polls Active Directory Domain Services and applies any changes to the service.

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
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrServiceConfig**](msft-dfsrserviceconfig.md)
</dt> </dl>

 

 





