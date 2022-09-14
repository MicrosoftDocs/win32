---
description: Returns virtual machine summary information for the specified virtual machine definition files.
ms.assetid: 5a3d7f2c-3b89-4dd6-909d-4452afc3705f
title: GetDefinitionFileSummaryInformation method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.GetDefinitionFileSummaryInformation
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetDefinitionFileSummaryInformation method of the Msvm\_VirtualSystemManagementService class

Returns virtual machine summary information for the specified virtual machine definition files.

## Syntax


```mof
uint32 GetDefinitionFileSummaryInformation(
  [in]  string                      DefinitionFiles[],
  [out] Msvm_SummaryInformationBase SummaryInformation[]
);
```



## Parameters

<dl> <dt>

*DefinitionFiles* \[in\]
</dt> <dd>

An array of paths to XML configuration files for which to return summary information.

</dd> <dt>

*SummaryInformation* \[out\]
</dt> <dd>

An array of [**Msvm\_SummaryInformationBase**](msvm-summaryinformation.md) instances containing the requested information for the virtual machines and/or snapshots specified in the *DefinitionFiles* array. Only the **Name**, **ElementName**, **CreationTime**, and **Notes** properties are returned, all other properties will be **Null**.

> [!Note]  

 

Prior to Windows 10, version 1703, datatype was [**Msvm\_SummaryInformation**](msvm-summaryinformation.md).

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

 

 




