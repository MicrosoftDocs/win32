---
title: EnableDevice method of the MSISCSITARGET\_StorageVolume class
description: Requests that the logical device be enabled or disabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4e429b9f-6914-42f7-b65d-c35f57e3df4f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method iSCSI Software Target API
- EnableDevice method iSCSI Software Target API , MSISCSITARGET_StorageVolume class
- MSISCSITARGET_StorageVolume class iSCSI Software Target API , EnableDevice method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageVolume.EnableDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the MSISCSITARGET\_StorageVolume class

Requests that the logical device be enabled or disabled. Deprecated, use the [**RequestStateChange**](requeststatechange-msiscsitarget-storagevolume.md) method instead.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[in\]
</dt> <dd>

Set **True** to enable the device, **false** to disable the device.

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

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





