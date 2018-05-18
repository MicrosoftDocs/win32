---
title: WvrRemoveVolumePartnerStretch method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9bdcc6d5-78d1-493f-8d85-5e179fa6d01e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WvrRemoveVolumePartnerStretch method", "WvrRemoveVolumePartnerStretch method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, WvrRemoveVolumePartnerStretch method"]
---

# WvrRemoveVolumePartnerStretch method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 WvrRemoveVolumePartnerStretch(
  [in] string SourceReplicationGroupName,
  [in] string SourceComputerName,
  [in] string SourceVolumeName[]
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The name of the target replication group.

</dd> <dt>

*SourceVolumeName* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





