---
title: GetError method of the CIM\_ConcreteJob class
description: When the job is executing or has terminated without error, then this method returns no CIM\_Error instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '327500c9-468a-4149-94ae-857bfafda2bf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetError method", "GetError method, CIM_ConcreteJob class", "CIM_ConcreteJob class, GetError method"]
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.GetError
api_location:
- MSPSService.dll
api_type:
- COM
---

# GetError method of the CIM\_ConcreteJob class

When the job is executing or has terminated without error, then this method returns no [**CIM\_Error**](cim-error.md) instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a **CIM\_Error** instance is returned.

## Syntax


```mof
uint32 GetError(
  [out] CIM_Error Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

If the **OperationalStatus** property on the Job is not "OK", then this method will return a [**CIM\_Error**](cim-error.md) instance. Otherwise, when the Job is "OK", null is returned.

</dd> </dl>

## Return value

<dl> <dt>

**Success**
</dt> <dd>

0

**Success**

</dd> <dt>

**Not Supported**
</dt> <dd>

1

**Not Supported**

</dd> <dt>

**Unspecified Error**
</dt> <dd>

2

**Unspecified Error**

</dd> <dt>

**Timeout**
</dt> <dd>

3

**Timeout**

</dd> <dt>

**Failed**
</dt> <dd>

4

**Failed**

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

**Invalid Parameter**

</dd> <dt>

**Access Denied**
</dt> <dd>

6

**Access Denied**

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

7–32767

**DMTF Reserved**

</dd> <dt>

**Vendor Specific**
</dt> <dd>

32768–65535

**Vendor Specific**

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





