---
title: SetPartnershipAddVolumes method of the MSFT\_WvrAdminTasks class
description: Adds source and destination volumes to replication groups in an existing partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7444284a-ebe7-462e-956d-b86fea2a0cfe
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPartnershipAddVolumes method
- SetPartnershipAddVolumes method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetPartnershipAddVolumes method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPartnershipAddVolumes method of the MSFT\_WvrAdminTasks class

Adds source and destination volumes to replication groups in an existing partnership.

## Syntax


```mof
uint32 SetPartnershipAddVolumes(
  [in] string  SourceRGName,
  [in] string  SourceComputerName,
  [in] string  SourceAddVolumePartnership[],
  [in] string  DestinationRGName,
  [in] string  DestinationComputerName,
  [in] string  DestinationAddVolumePartnership[],
  [in] boolean Seeded
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

*SourceAddVolumePartnership* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*DestinationAddVolumePartnership* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Seeded* \[in\]
</dt> <dd>

TBD

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

 

 





