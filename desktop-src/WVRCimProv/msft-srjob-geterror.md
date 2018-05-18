---
title: GetError method of the MSFT\_SrJob class
description: Returns a CIM\_Error instance if the MSFT\_SrJob instance fails or is terminated by a client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bf4d4259-42e8-4cc5-bde9-ef14a0924403'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetError method", "GetError method, MSFT_SrJob class", "MSFT_SrJob class, GetError method"]
topic_type:
- apiref
api_name:
- MSFT_SrJob.GetError
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# GetError method of the MSFT\_SrJob class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Returns a [**CIM\_Error**](cim-error.md) instance if the [**MSFT\_SrJob**](msft-srjob.md) instance fails or is terminated by a client.

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

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SrJob**](msft-srjob.md)
</dt> </dl>

 

 





