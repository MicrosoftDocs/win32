---
title: ExportSystemDefinition method of the Msvm\_VirtualSystemManagementService class
description: Exports a virtual system, or a snapshot of a virtual computer system to a file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '709c64e2-e6e9-426e-a033-e8941319dcea'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExportSystemDefinition method", "ExportSystemDefinition method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, ExportSystemDefinition method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ExportSystemDefinition
api_location:
- VMMS.exe
api_type:
- COM
---

# ExportSystemDefinition method of the Msvm\_VirtualSystemManagementService class

Exports a virtual system, or a snapshot of a virtual computer system to a file. The virtual system must be in a powered off or saved state for the export to succeed. The virtual system, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportSystemDefinition(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ExportDirectory,
  [in]  string                 ExportSettingData,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) that represents the virtual system to export.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully-qualified path of the directory that receives the exported virtual system. If the **CreateVmExportSubdirectory** property that is referenced by the *ExportSettingData* parameter is set to **true**, then this directory can be reused for exporting multiple virtual systems, and this method places each virtual system definition in a separate subdirectory under this path.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An instance of [**Msvm\_VirtualSystemExportSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850252) that represents the settings for the export operation.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





