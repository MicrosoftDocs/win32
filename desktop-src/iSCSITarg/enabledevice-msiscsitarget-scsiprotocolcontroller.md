---
title: EnableDevice method of the MSISCSITARGET\_SCSIProtocolController class
description: Requests that the logical device be enabled or disabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12de6429-2615-4b71-9555-dcb7f287de5f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method iSCSI Software Target API
- EnableDevice method iSCSI Software Target API , MSISCSITARGET_SCSIProtocolController class
- MSISCSITARGET_SCSIProtocolController class iSCSI Software Target API , EnableDevice method
topic_type:
- apiref
api_name:
- MSISCSITARGET_SCSIProtocolController.EnableDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the MSISCSITARGET\_SCSIProtocolController class

Requests that the logical device be enabled or disabled. Deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msiscsitarget-scsiprotocolcontroller.md) method.

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
</dt> <dt>

[**RequestStateChange**](requeststatechange-msiscsitarget-scsiprotocolcontroller.md)
</dt> <dt>

[**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)
</dt> </dl>

 

 





