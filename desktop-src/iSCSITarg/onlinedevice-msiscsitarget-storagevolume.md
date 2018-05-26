---
title: OnlineDevice method of the MSISCSITARGET\_StorageVolume class
description: Requests that the logical device be taken online or offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 415ba956-959b-4160-9dba-49b5483c2d1c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- OnlineDevice method iSCSI Software Target API
- OnlineDevice method iSCSI Software Target API , MSISCSITARGET_StorageVolume class
- MSISCSITARGET_StorageVolume class iSCSI Software Target API , OnlineDevice method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageVolume.OnlineDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineDevice method of the MSISCSITARGET\_StorageVolume class

Requests that the logical device be taken online or offline. Deprecated, use the [**RequestStateChange**](requeststatechange-msiscsitarget-storagevolume.md) method instead.

Only a device that has been configured and enabled can be brought online or taken offline.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 OnlineDevice(
  [in] boolean Online
);
```



## Parameters

<dl> <dt>

*Online* \[in\]
</dt> <dd>

Set **True** to take the device online, **false** to take the device offline.

</dd> </dl>

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

1

The request is not supported due to the current state of the device

</dd> <dt>


</dt> <dd>

3 = *value*

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

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





