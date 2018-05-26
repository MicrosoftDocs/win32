---
title: SetPartnershipSetSourcePartnership method of the MSFT\_WvrAdminTasks class
description: Changes the source and destination replication direction between two replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34ecb108-93eb-4833-b162-06c45bad95cc
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPartnershipSetSourcePartnership method
- SetPartnershipSetSourcePartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetPartnershipSetSourcePartnership method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SetPartnershipSetSourcePartnership
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPartnershipSetSourcePartnership method of the MSFT\_WvrAdminTasks class

Changes the source and destination replication direction between two replication groups.

## Syntax


```mof
uint32 SetPartnershipSetSourcePartnership(
  [in] string SourceRGName,
  [in] string NewSourceComputerName,
  [in] string DestinationRGName,
  [in] string DestinationComputerName
);
```



## Parameters

<dl> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*NewSourceComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the new source computer.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

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

 

 





