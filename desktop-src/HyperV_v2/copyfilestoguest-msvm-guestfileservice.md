---
description: Copies files from the Hyper-V host to the virtual machine.
ms.assetid: 76667557-13B2-4286-BC6B-E32FADE62A7A
title: Msvm_GuestFileService::CopyFilesToGuest method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_GuestFileService.CopyFilesToGuest
api_type: 
- COM
api_location: 
- vmms.exe
---

# Msvm\_GuestFileService::CopyFilesToGuest method

Copies files from the Hyper-V host to the virtual machine.

## Syntax


```C++
uint32 CopyFilesToGuest(
  [in]            string                  CopyFileToGuestSettings[],
  [out]           CIM_ConcreteJob     Job,
  [out, optional] Msvm_CopyFileToGuestJob ParentPools[]
);
```



## Parameters

<dl> <dt>

*CopyFileToGuestSettings* \[in\]
</dt> <dd>

An array of instances of the [**Msvm\_CopyFileToGuestSettingData**](msvm-copyfiletoguestsettingdata.md) class that represents a guest file service operation job.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

> [!Note]  
> This parameter was added in Windows 10.

 

</dd> <dt>

*ParentPools* \[out, optional\]
</dt> <dd>

An optional array of [**Msvm\_CopyFileToGuestJob**](msvm-copyfiletoguestjob.md) references that are used for monitoring progress of the operation. **CopyFilesToGuest** uses *ParentPools* if it can't execute synchronously. If the operation executes asynchronously, the return value is 4096.

> [!Note]  
> This parameter was removed in Windows 10.

 

</dd> </dl>

## Return value

On success, returns 0; otherwise, returns an error value.

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
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | \\\\Root\\Virtualization\\V2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_GuestFileService**](msvm-guestfileservice.md)
</dt> </dl>

 

 




