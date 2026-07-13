---
description: Returns a CIM_Error instance if the Job instance fails or is terminated by a client.
ms.assetid: 0ee9c545-d372-4b16-b48d-57b23fe704c7
title: GetError method of the CIM_ConcreteJob WMI class
ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ConcreteJob.GetError
api_type: 
- COM
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# GetError method of the CIM_ConcreteJob WMI class

Returns a [**CIM\_Error**](cim-error.md) instance if the Job instance fails or is terminated by a client.

## Syntax


```mof
uint32 GetError(
  [out] CIM_Error Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

If the **OperationalStatus** property on the job is not **OK**, then this method returns a [**CIM\_Error**](cim-error.md) instance. Returns **NULL** while the job is executing or if the job terminated without error.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Access Denied** (6)
</dt> <dt>

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




