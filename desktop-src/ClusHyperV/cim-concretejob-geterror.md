---
title: GetError method of the CIM\_ConcreteJob class
description: Retrieves error information for the operational status of a concrete job. This method returns a CIM\_Error instance if job fails; otherwise it returns NULL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff87846f-09bf-4358-aff2-8ee873990bb7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetError method", "GetError method, CIM_ConcreteJob class", "CIM_ConcreteJob class, GetError method"]
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.GetError
api_location:
- VMMS.exe
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

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





