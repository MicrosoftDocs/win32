---
title: Reset method of the MSISCSITARGET\_StorageVolume class
description: Requests a reset of the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c2b917a3-32b8-4d59-9fa1-f86023b7aa2b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method iSCSI Software Target API", "Reset method iSCSI Software Target API , MSISCSITARGET_StorageVolume class", "MSISCSITARGET_StorageVolume class iSCSI Software Target API , Reset method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageVolume.Reset
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# Reset method of the MSISCSITARGET\_StorageVolume class

Requests a reset of the logical device.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>


</dt> <dd>

0

Success.

</dd> <dt>


</dt> <dd>

1

The request is not supported.

</dd> <dt>


</dt> <dd>

2 = *value*

Undefined error.

</dd> </dl>

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

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





