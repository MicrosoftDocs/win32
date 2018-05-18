---
title: ExportSnapshot method of the Msvm\_CollectionSnapshotService class
description: Exports a snapshot of a virtual system collection to a file. The snapshot collection, its associated configuration settings, and its associated resource settings are preserved in the resulting file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56c5c651-8a55-4b9b-ba66-97f9213c45af'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExportSnapshot method", "ExportSnapshot method, Msvm_CollectionSnapshotService class", "Msvm_CollectionSnapshotService class, ExportSnapshot method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotService.ExportSnapshot
api_location:
- VMMS.exe
api_type:
- COM
---

# ExportSnapshot method of the Msvm\_CollectionSnapshotService class

Exports a snapshot of a virtual system collection to a file. The snapshot collection, its associated configuration settings, and its associated resource settings are preserved in the resulting file.

## Syntax


```mof
uint32 ExportSnapshot(
  [in]  CIM_Collection  REF SnapshotCollection,
  [in]  string              ExportDirectory,
  [in]  string              ExportSettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SnapshotCollection* \[in\]
</dt> <dd>

A reference to a [**CIM\_Collection**](cim-collection.md) object that represents the snapshot collection to export.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully-qualified path of the directory that receives the exported virtual system collection. If the **CreateVmExportSubdirectory** property in the *ExportSettingData* parameter is set to **true**, then this directory can be reused for exporting multiple virtual system collections, and this method places each virtual system collection in a separate subdirectory under this path.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An instance of [**Msvm\_CollectionSnapshotExportSettingData**](msvm-collectionsnapshotexportsettingdata.md) that represents the settings for the export operation.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional job to use for this operation if it is performed asynchronously.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns "0" if it succeeds. If this method is executed asynchronously, it returns "4096" and the **Job** output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 





