---
title: GetError method of the MSISCSITARGET\_ConcreteJob class
description: Returns a CIM\_Error instance if the MSISCSITARGET\_ConcreteJob instance fails or is terminated by a client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '77de9516-2be5-4ce3-b363-8a4590757d81'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetError method iSCSI Software Target API", "GetError method iSCSI Software Target API , MSISCSITARGET_ConcreteJob class", "MSISCSITARGET_ConcreteJob class iSCSI Software Target API , GetError method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ConcreteJob.GetError
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetError method of the MSISCSITARGET\_ConcreteJob class

Returns a [**CIM\_Error**](https://msdn.microsoft.com/library/cc150671) instance if the [**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md) instance fails or is terminated by a client.

This method is inherited from the [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) class.

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

If the **OperationalStatus** property on the job is not **OK**, then this method returns a [**CIM\_Error**](https://msdn.microsoft.com/library/cc150671) instance. Returns **NULL** while the job is executing or if the job terminated without error.

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



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
</dt> </dl>

 

 





