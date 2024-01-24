---
description: Service to create, destroy and export snapshot collection of virtual systems.
ms.assetid: 55a6c7b4-5352-4766-b5b7-6699b1f40b78
title: Msvm_CollectionSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionSnapshotService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectionSnapshotService class

Service to create, destroy and export snapshot collection of virtual systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionSnapshotService : CIM_Service
{
};
```

## Members

The **Msvm\_CollectionSnapshotService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_CollectionSnapshotService** class has these methods.



| Method                                                                                    | Description                                                                                                                                                                                                                   |
|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplySnapshot**](msvm-collectionsnapshotservice-applysnapshot.md)                     | Applies a snapshot collection to the collection of virtual computer system.<br/>                                                                                                                                        |
| [**ConvertToReferencePoint**](msvm-collectionsnapshotservice-converttoreferencepoint.md) | Convert an existing collection snapshot to a reference point collection. The snapshot collection gets deleted as a side effect. Only recovery snapshots can be converted to reference points.<br/>                      |
| [**CreateSnapshot**](msvm-collectionsnapshotservice-createsnapshot.md)                   | Creates a snapshot of a virtual system collection.<br/>                                                                                                                                                                 |
| [**DestroySnapshot**](msvm-collectionsnapshotservice-destroysnapshot.md)                 | Destroy an existing snapshot of virtual system collection. This method may as a side effect destroy other snapshots that are dependent on the affected snapshot.<br/>                                                   |
| [**ExportSnapshot**](msvm-collectionsnapshotservice-exportsnapshot.md)                   | Exports a snapshot collection of virtual computer systems to a file. The snapshot collection, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.<br/> |



 

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

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




