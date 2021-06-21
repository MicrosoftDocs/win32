---
description: GetError method of the Msvm_StorageJob class - Retrieves the error.
ms.assetid: 785b83c4-06f4-46b5-81f7-35c6fce16c92
title: GetError method of the Msvm_StorageJob class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_StorageJob.GetError
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetError method of the Msvm\_StorageJob class

Retrieves the error.

## Syntax


```mof
uint32 GetError(
  [out] string Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

The retrieved error.

</dd> </dl>

## Return value

This method returns one of the following values:

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
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_StorageJob**](msvm-storagejob.md)
</dt> </dl>

 

 




