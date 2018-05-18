---
title: ClearMetadataAll method of the MSFT\_WvrAdminTasks class
description: Removes orphaned Storage Replica metadata from the registry, partition, and system volume information folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ADECB616-F4C5-4E89-8FED-E29B63D80E6E'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ClearMetadataAll method", "ClearMetadataAll method, MSFT_WvrAdminTasks interface", "MSFT_WvrAdminTasks interface, ClearMetadataAll method"]
---

# ClearMetadataAll method of the MSFT\_WvrAdminTasks class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Removes orphaned Storage Replica metadata from the registry, partition, and system volume information folder.

## Syntax


```mof
uint32 ClearMetadataAll(
  [in] string  ComputerName,
  [in] boolean AllConfiguration,
  [in] boolean AllLogs,
  [in] boolean AllPartitions,
  [in] boolean NoRestart
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*AllConfiguration* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AllLogs* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AllPartitions* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*NoRestart* \[in\]
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

 

 





