---
description: Exports a virtual machine, or a snapshot of a virtual machine, to a file.
ms.assetid: b88712e4-a1a6-4188-8082-f4973f89018d
title: ExportSystemDefinition method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.ExportSystemDefinition
api_type: 
- COM
api_location: 
- vmms.exe
---

# ExportSystemDefinition method of the Msvm\_VirtualSystemManagementService class

Exports a virtual machine, or a snapshot of a virtual machine, to a file. The virtual machine must be in the "powered off" or "saved" state to be exported. The virtual machine, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportSystemDefinition(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ExportDirectory,
  [in]  string                 ExportSettingData,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) that represents the virtual machine to be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

The fully qualified path of the directory to which the virtual machine is to be exported. If the **CreateVmExportSubdirectory** property of the [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md) class in the *ExportSettingData* parameter is set to **True**, then this directory can be reused for exporting multiple virtual machines and this method places each virtual machine definition in a separate subdirectory under this path.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

An embedded instance of the [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md) class that represents the settings for the export operation.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

