---
description: This class represents a collection reference point export operation job.
ms.assetid: c752ff1d-163c-4aa9-b29e-76478a18a08c
title: Msvm_CollectionReferencePointExportJob class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionReferencePointExportJob
- Msvm_CollectionReferencePointExportJob.Cancellable
- Msvm_CollectionReferencePointExportJob.ErrorSummaryDescription
- Msvm_CollectionReferencePointExportJob.CollectionId
- Msvm_CollectionReferencePointExportJob.ReferencePointGroupId
- Msvm_CollectionReferencePointExportJob.BaseReferencePointGroupId
- Msvm_CollectionReferencePointExportJob.VirtualMachineId
- Msvm_CollectionReferencePointExportJob.ExportDirectory
- Msvm_CollectionReferencePointExportJob.ExportedDisks
- Msvm_CollectionReferencePointExportJob.ExportedLogFilePaths
- Msvm_CollectionReferencePointExportJob.ExportedConfigFilePaths
- Msvm_CollectionReferencePointExportJob.ExportedRuntimeFilePaths
- Msvm_CollectionReferencePointExportJob.ExportedGuestStateFilePaths
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectionReferencePointExportJob class

This class represents a collection reference point export operation job.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionReferencePointExportJob : CIM_ConcreteJob
{
  boolean Cancellable;
  string  ErrorSummaryDescription;
  string  CollectionId;
  string  ReferencePointGroupId;
  string  BaseReferencePointGroupId;
  string  VirtualMachineId[];
  string  ExportDirectory;
  string  ExportedDisks[];
  string  ExportedLogFilePaths[];
  string  ExportedConfigFilePaths[];
  string  ExportedRuntimeFilePaths[];
  string  ExportedGuestStateFilePaths[];
};
```

## Members

The **Msvm\_CollectionReferencePointExportJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_CollectionReferencePointExportJob** class has these methods.



| Method                                                                                  | Description                                        |
|:----------------------------------------------------------------------------------------|:---------------------------------------------------|
| [**GetError**](msvm-collectionreferencepointexportjob-geterror.md)                     | Retrieves an error.<br/>                     |
| [**GetErrorEx**](msvm-collectionreferencepointexportjob-geterrorex.md)                 | Retrieves additional error information.<br/> |
| [**RequestStateChange**](msvm-collectionreferencepointexportjob-requeststatechange.md) | Requests a state change.<br/>                |



 

### Properties

The **Msvm\_CollectionReferencePointExportJob** class has these properties.

<dl> <dt>

**BaseReferencePointGroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the collection reference point which is used as the base in the exportoperation.

</dd> <dt>

**Cancellable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the job can be cancelled. The value of this property does not guarantee that a request to cancel the job will succeed.

</dd> <dt>

**CollectionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the virtual machine group for which log files wereexported.

</dd> <dt>

**ErrorSummaryDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Job**](cim-job.md).**ErrorCode**")
</dt> </dl>

Contains an error summary description.

</dd> <dt>

**ExportDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Export Location.

</dd> <dt>

**ExportedConfigFilePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path of the exported virtual machine config file.

</dd> <dt>

**ExportedDisks**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Instance IDs of virtual disks for which log files were exported.

</dd> <dt>

**ExportedGuestStateFilePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path of the exported virtual machine guest state file.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**ExportedLogFilePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Paths of the log files which were exported.

</dd> <dt>

**ExportedRuntimeFilePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path of the exported virtual machine runtime state file.

</dd> <dt>

**ReferencePointGroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the collection reference point which is exported.

</dd> <dt>

**VirtualMachineId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the virtual machines for which export operation has been performed.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

