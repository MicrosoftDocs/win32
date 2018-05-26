---
title: GetDefinitionFileSummaryInformation method of the Msvm\_VirtualSystemManagementService class
description: Returns virtual system summary information for an array of virtual machine definition files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c999508a-b3bd-4bca-b908-d475b657cceb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDefinitionFileSummaryInformation method
- GetDefinitionFileSummaryInformation method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, GetDefinitionFileSummaryInformation method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetDefinitionFileSummaryInformation
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetDefinitionFileSummaryInformation method of the Msvm\_VirtualSystemManagementService class

Returns virtual system summary information for an array of virtual machine definition files.

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

An array of paths to the XML configuration files.

</dd> <dt>

*SummaryInformation* \[out\]
</dt> <dd>

An array of [**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md) instances that contain the requested summary information. Only the **Name**, **ElementName**, **CreateTime**, and **Notes** properties are returned. All other **Msvm\_SummaryInformationBase** properties should be **NULL**.

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





