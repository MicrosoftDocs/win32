---
title: ExportReferencePoint method of the Msvm\_CollectionReferencePointService class
description: Exports a reference point collection to a file. The reference point collection, its configuration settings, and its resource settings will be preserved in the resulting file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4f05cbb-1143-445d-8c56-30f1d2a7f9a5
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExportReferencePoint method
- ExportReferencePoint method, Msvm_CollectionReferencePointService class
- Msvm_CollectionReferencePointService class, ExportReferencePoint method
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointService.ExportReferencePoint
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExportReferencePoint method of the Msvm\_CollectionReferencePointService class

Exports a reference point collection to a file. The reference point collection, its configuration settings, and its resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportReferencePoint(
  [in]  CIM_Collection  REF ReferencePointCollection,
  [in]  string              ExportDirectory,
  [in]  string              ExportSettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*ReferencePointCollection* \[in\]
</dt> <dd>

A reference to a [**CIM\_Collection**](cim-collection.md) object that represents the reference point collection to export.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully qualified path of the directory that will contain the exported reference point collection.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An embedded instance of [**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md) that represents the settings for the export operation.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to a job that is used if the operation is performed asynchronously.

</dd> </dl>

## Return value

If this method runs synchronously, it returns "0" if it succeeds. If this method runs asynchronously, it returns "4096" and a job is used to monitor the progress of the operation. Any other return value indicates an error.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 





