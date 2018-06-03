---
title: SaveProperties method of the MSISCSITARGET\_SCSIProtocolController class
description: Requests that the device capture its current configuration, setup, and/or state information in a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8bb1fe9f-7ca7-4324-82f1-60ab43a2e589
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SaveProperties method iSCSI Software Target API
- SaveProperties method iSCSI Software Target API , MSISCSITARGET_SCSIProtocolController class
- MSISCSITARGET_SCSIProtocolController class iSCSI Software Target API , SaveProperties method
topic_type:
- apiref
api_name:
- MSISCSITARGET_SCSIProtocolController.SaveProperties
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SaveProperties method of the MSISCSITARGET\_SCSIProtocolController class

Requests that the device capture its current configuration, setup, and/or state information in a backing store. This information can be restored at a later time by using the [**RestoreProperties**](restoreproperties-msiscsitarget-scsiprotocolcontroller.md) method.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 SaveProperties();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the following values.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_SCSIProtocolController**](msiscsitarget-scsiprotocolcontroller.md)
</dt> </dl>

 

 





