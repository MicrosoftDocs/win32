---
title: RestoreProperties method of the MSISCSITARGET\_StorageVolume class
description: Requests that the device return its configuration, setup, and/or state information to a previous state from a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8cec9690-9244-42f1-a4bc-d4810e51cd02'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RestoreProperties method iSCSI Software Target API", "RestoreProperties method iSCSI Software Target API , MSISCSITARGET_StorageVolume class", "MSISCSITARGET_StorageVolume class iSCSI Software Target API , RestoreProperties method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageVolume.RestoreProperties
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# RestoreProperties method of the MSISCSITARGET\_StorageVolume class

Requests that the device return its configuration, setup, and/or state information to a previous state from a backing store. Typically this information is stored by using the [**SaveProperties**](saveproperties-msiscsitarget-storagevolume.md) method.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 RestoreProperties();
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
</dt> <dt>

[**SaveProperties**](saveproperties-msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





