---
title: CheckConnectivity method of the MSFT\_DfsrConnectionInfo class
description: Checks connectivity with the partner's computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c161d73-5826-41b6-a6d3-45d914087b33
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CheckConnectivity method Distributed File System Replication
- CheckConnectivity method Distributed File System Replication , MSFT_DfsrConnectionInfo class
- MSFT_DfsrConnectionInfo class Distributed File System Replication , CheckConnectivity method
topic_type:
- apiref
api_name:
- MSFT_DfsrConnectionInfo.CheckConnectivity
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CheckConnectivity method of the MSFT\_DfsrConnectionInfo class

Checks connectivity with the partner's computer.

## Syntax


```mof
uint32 CheckConnectivity();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the [MONITOR\_STATUS return codes](monitor-status-return-codes.md) or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

This method is meaningful only for inbound connections. It always fails with an error on outbound connections.

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

[**MSFT\_DfsrConnectionInfo**](msft-dfsrconnectioninfo.md)
</dt> </dl>

 

 





