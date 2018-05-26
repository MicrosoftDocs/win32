---
title: GetStretchPartnership method of the MSFT\_WvrAdminTasks class
description: Retrieves a replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c43f8f3-aafe-4819-843e-1b453e92f385
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetStretchPartnership method
- GetStretchPartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, GetStretchPartnership method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.GetStretchPartnership
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetStretchPartnership method of the MSFT\_WvrAdminTasks class

Retrieves a replication partnership.

## Syntax


```mof
uint32 GetStretchPartnership(
  [in]  string                         SourceRGName,
  [in]  string                         SourceComputerName,
  [in]  string                         DestinationRGName,
  [in]  string                         DestinationComputerName,
  [out] MSFT_WvrReplicationPartnership Output[]
);
```



## Parameters

<dl> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the source computer.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns a collection of resulting [**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





