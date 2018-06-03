---
title: CheckConnectivity method of the DfsrConnectionInfo class
description: Checks connectivity with the partner's computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5eee2e5a-e101-4bc3-97dd-7f7b870289df
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CheckConnectivity method Distributed File System Replication
- CheckConnectivity method Distributed File System Replication , DfsrConnectionInfo class
- DfsrConnectionInfo class Distributed File System Replication , CheckConnectivity method
topic_type:
- apiref
api_name:
- DfsrConnectionInfo.CheckConnectivity
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CheckConnectivity method of the DfsrConnectionInfo class

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrConnectionInfo**](dfsrconnectioninfo.md)
</dt> </dl>

 

 





