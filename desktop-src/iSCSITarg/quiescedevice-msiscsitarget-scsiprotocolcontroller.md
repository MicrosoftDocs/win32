---
title: QuiesceDevice method of the MSISCSITARGET\_SCSIProtocolController class
description: Requests that the logical device cleanly cease all current activity or resume activity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b74c4f51-63c9-4ac6-9f2e-de974bb9717c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["QuiesceDevice method iSCSI Software Target API", "QuiesceDevice method iSCSI Software Target API , MSISCSITARGET_SCSIProtocolController class", "MSISCSITARGET_SCSIProtocolController class iSCSI Software Target API , QuiesceDevice method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_SCSIProtocolController.QuiesceDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# QuiesceDevice method of the MSISCSITARGET\_SCSIProtocolController class

Requests that the logical device cleanly cease all current activity or resume activity.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 QuiesceDevice(
  [in] boolean Quiesce
);
```



## Parameters

<dl> <dt>

*Quiesce* \[in\]
</dt> <dd>

Set to **True** to cleanly cease all activity. Set to **false** to resume activity.

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

1

The request is not supported due to the current state of the device.

</dd> <dt>


</dt> <dd>

3 = *value*

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

[**MSISCSITARGET\_SCSIProtocolController**](msiscsitarget-scsiprotocolcontroller.md)
</dt> </dl>

 

 





