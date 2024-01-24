---
description: Exports a reference point collection to a file. The reference point collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.
ms.assetid: 0ed61ded-b4d6-40c5-98be-e192eb934387
title: ExportReferencePoint method of the Msvm_CollectionReferencePointService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionReferencePointService.ExportReferencePoint
api_type: 
- COM
api_location: 
- vmms.exe
---

# ExportReferencePoint method of the Msvm\_CollectionReferencePointService class

Exports a reference point collection to a file. The reference point collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

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

A reference to a [**CIM\_Collection**](cim-collection.md) that represents the reference point collection to be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully-qualified path of the directory to which the reference point collection is to be exported.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An instance of [**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md) that represents the settings for the export operation.

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

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 




