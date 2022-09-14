---
description: Exports a snapshot collection of virtual computer systems to a file. The snapshot collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.
ms.assetid: 61fbc81c-c3e8-4058-b11a-4ed69481207c
title: ExportSnapshot method of the Msvm_CollectionSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionSnapshotService.ExportSnapshot
api_type: 
- COM
api_location: 
- vmms.exe
---

# ExportSnapshot method of the Msvm\_CollectionSnapshotService class

Exports a snapshot collection of virtual computer systems to a file. The snapshot collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportSnapshot(
  [in]  CIM_Collection  REF SnapshotCollection,
  [in]  string              ExportDirectory,
  [in]  string              ExportSettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SnapshotCollection* \[in\]
</dt> <dd>

A reference to a [**CIM\_Collection**](cim-collection.md) that represents the snapshot collection to be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully-qualified path of the directory to which the virtual system collection is to be exported. If the **CreateVmExportSubdirectory** property in the *ExportSettingData* parameter is set to **True** then this directory can be reused for exporting multiple virtual system collections and this method places each virtual system collection definition in a separate subdirectory under this path.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An instance of [**Msvm\_CollectionSnapshotExportSettingData**](msvm-collectionsnapshotexportsettingdata.md) that represents the settings for the export operation.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](cim-concretejob.md) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the Job output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 




