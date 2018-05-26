---
title: GetError method of the CIM\_ConcreteJob class
description: Returns a CIM\_Error instance if the Job instance fails or is terminated by a client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1860e20-0efa-4fdb-8411-61af362fcb2f
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetError method
- GetError method, CIM_ConcreteJob class
- CIM_ConcreteJob class, GetError method
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.GetError
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetError method of the CIM\_ConcreteJob class

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

This method returns one of the following values.

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



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





