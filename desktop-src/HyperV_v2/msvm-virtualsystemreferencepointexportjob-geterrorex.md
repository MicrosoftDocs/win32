---
description: GetErrorEx method of the Msvm_VirtualSystemReferencePointExportJob class - Retrieves additional information about an error.
ms.assetid: 63ce4762-e5ce-405f-b5fc-74e505b0eaf1
title: GetErrorEx method of the Msvm_VirtualSystemReferencePointExportJob class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemReferencePointExportJob.GetErrorEx
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetErrorEx method of the Msvm\_VirtualSystemReferencePointExportJob class

Retrieves additional information about an error. When the job is executing or has terminated without error, **GetErrorEx** returns no **GetErrorEx** instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then **GetErrorEx** returns one or more [**Msvm\_Error**](msvm-error.md) instances.

## Syntax


```mof
uint32 GetErrorEx(
  [out] string Errors[]
);
```



## Parameters

<dl> <dt>

*Errors* \[out\]
</dt> <dd>

If the operational status of the job is not "OK", this parameter returns an array of [**Msvm\_Error**](msvm-error.md) instances. Otherwise, if the job is "OK", this parameter contains **NULL**.

</dd> </dl>

## Return value

On success, returns 0; otherwise, returns an error.

<dl> <dt>

**Completed with No Error** (0)
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

**System is in used** (32774)
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

[**Msvm\_VirtualSystemReferencePointExportJob**](msvm-virtualsystemreferencepointexportjob.md)
</dt> </dl>

 

 




