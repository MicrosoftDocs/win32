---
description: Retrieves the key protector for a virtual system.
ms.assetid: fd827da8-b2fc-4c57-bb7d-7da46db8e8be
title: GetKeyProtector method of the Msvm_SecurityService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecurityService.GetKeyProtector
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetKeyProtector method of the Msvm\_SecurityService class

Retrieves the key protector for a virtual system.

## Syntax


```mof
uint32 GetKeyProtector(
  [in]  string SecuritySettingData,
  [out] uint8  KeyProtector[]
);
```



## Parameters

<dl> <dt>

*SecuritySettingData* \[in\]
</dt> <dd>

String contains an embedded instance of the [**Msvm\_SecuritySettingData**](msvm-securitysettingdata.md) class representing the security settings of a virtual system.

</dd> <dt>

*KeyProtector* \[out\]
</dt> <dd>

Receives the raw byte array that contains the key protector currently in use.

</dd> </dl>

## Return value

On success, returns a 0 or 4096. Otherwise, returns an error.

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

[**Msvm\_SecurityService**](msvm-securityservice.md)
</dt> </dl>

 

 




