---
title: GetError method of the Msvm\_ConcreteJob class
description: When the job is executing or has terminated without error, then this method does not return a CIM\_Error instance.
ms.assetid: '59a0d015-e851-4b5e-a3da-c74ceb916e6c'
keywords: ["GetError method Hyper-V", "GetError method Hyper-V , Msvm_ConcreteJob class", "Msvm_ConcreteJob class Hyper-V , GetError method"]
topic_type:
- apiref
api_name:
- Msvm_ConcreteJob.GetError
api_location:
- Root\Virtualization
api_type:
- COM
---

# GetError method of the Msvm\_ConcreteJob class

When the job is executing or has terminated without error, then this method does not return a [**CIM\_Error**](https://msdn.microsoft.com/library/mt445938) instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a **CIM\_Error** instance is returned.

## Syntax


```mof
uint32 GetError(
  [out] string Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

Type: **string**

If the operational status of the job is not 2 (OK), this method returns a [**CIM\_Error**](https://msdn.microsoft.com/library/mt445938) instance in CIM-XML format. Otherwise, if the Job is 2 (OK), **NULL** is returned.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.

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

## Remarks

Access to the [**Msvm\_ConcreteJob**](msvm-concretejob.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_ConcreteJob**](msvm-concretejob.md)
</dt> </dl>

 

 





