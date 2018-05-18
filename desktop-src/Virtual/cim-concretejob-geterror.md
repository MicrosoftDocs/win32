---
title: GetError method of the CIM\_ConcreteJob class
description: Retrieves error information for the operational status of a concrete job. This method returns a CIM\_Error instance if job fails; otherwise it returns NULL.
ms.assetid: 'b0583406-4420-4d4a-a7ee-f83e9a9d85f9'
keywords: ["GetError method Hyper-V", "GetError method Hyper-V , CIM_ConcreteJob class", "CIM_ConcreteJob class Hyper-V , GetError method"]
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.GetError
api_location:
- Root\virtualization
api_type:
- COM
---

# GetError method of the CIM\_ConcreteJob class

Retrieves error information for the operational status of a concrete job. This method returns a [**CIM\_Error**](cim-error.md) instance if job fails; otherwise it returns **NULL**.

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

An embedded [**CIM\_Error**](cim-error.md) instance if the job fails; otherwise **NULL**.

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

**DMTF Reserved** (4098–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





