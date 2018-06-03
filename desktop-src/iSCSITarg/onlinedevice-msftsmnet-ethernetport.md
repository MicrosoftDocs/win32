---
title: OnlineDevice method of the MSFTSMNET\_EthernetPort class
description: Requests that the logical device be taken online or offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eae29a5f-ec0b-4ac6-a310-65babc0456d6
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- OnlineDevice method iSCSI Software Target API
- OnlineDevice method iSCSI Software Target API , MSFTSMNET_EthernetPort class
- MSFTSMNET_EthernetPort class iSCSI Software Target API , OnlineDevice method
topic_type:
- apiref
api_name:
- MSFTSMNET_EthernetPort.OnlineDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnlineDevice method of the MSFTSMNET\_EthernetPort class

Requests that the logical device be taken online or offline. Deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msftsmnet-ethernetport.md) method.

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

Set to **True** to take the device online. Set to **false** to take the device offline.

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

[**MSFTSMNET\_EthernetPort**](msftsmnet-ethernetport.md)
</dt> <dt>

[**RequestStateChange**](requeststatechange-msftsmnet-ethernetport.md)
</dt> </dl>

 

 





