---
title: EnableDevice method of the MSFTSMNET\_EthernetPort class
description: Requests that the logical device be enabled or disabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 704949c0-78fb-4e97-a747-04984880f072
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method iSCSI Software Target API
- EnableDevice method iSCSI Software Target API , MSFTSMNET_EthernetPort class
- MSFTSMNET_EthernetPort class iSCSI Software Target API , EnableDevice method
topic_type:
- apiref
api_name:
- MSFTSMNET_EthernetPort.EnableDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableDevice method of the MSFTSMNET\_EthernetPort class

Requests that the logical device be enabled or disabled. Deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msftsmnet-ethernetport.md) method.

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

Set to **True** to enable the device Set to **false** to disable the device.

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

[**MSFTSMNET\_EthernetPort**](msftsmnet-ethernetport.md)
</dt> <dt>

[**RequestStateChange**](requeststatechange-msftsmnet-ethernetport.md)
</dt> </dl>

 

 





