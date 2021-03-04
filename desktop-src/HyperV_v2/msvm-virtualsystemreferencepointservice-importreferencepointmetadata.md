---
description: Imports reference point metadata of the virtual system.
ms.assetid: 8e32fded-cd84-4586-83c4-c23200d4698e
title: ImportReferencePointMetadata method of the Msvm_VirtualSystemReferencePointService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemReferencePointService.ImportReferencePointMetadata
api_type: 
- COM
api_location: 
- vmms.exe
---

# ImportReferencePointMetadata method of the Msvm\_VirtualSystemReferencePointService class

Imports reference point metadata of the virtual system.

## Syntax


```mof
uint32 ImportReferencePointMetadata(
  [in]  Msvm_ComputerSystem REF AffectedSystem,
  [in]  string                  ConfigFilePath,
  [in]  string                  RuntimeStateFilePath,
  [out] CIM_ConcreteJob     REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSystem* \[in\]
</dt> <dd>

A reference to a [**Msvm\_ComputerSystem**](msvm-computersystem.md) describing the affected system.

</dd> <dt>

*ConfigFilePath* \[in\]
</dt> <dd>

The fully-qualified path of the config file from where the reference point metadata will be imported.

</dd> <dt>

*RuntimeStateFilePath* \[in\]
</dt> <dd>

The fully-qualified path of the runtime state file from where the reference point metadata will be imported.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

</dd> </dl>

## Return value

Returns either 0 (no error) or one of the following error messages:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

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

[**Msvm\_VirtualSystemReferencePointService**](msvm-virtualsystemreferencepointservice.md)
</dt> </dl>

 

 




