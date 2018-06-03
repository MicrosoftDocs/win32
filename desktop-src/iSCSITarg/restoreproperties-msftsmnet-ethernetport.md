---
title: RestoreProperties method of the MSFTSMNET\_EthernetPort class
description: Requests that the device return its configuration, setup, and/or state information to a previous state from a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9252bb7c-c1e1-4b85-83c6-4a3a743810a5
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RestoreProperties method iSCSI Software Target API
- RestoreProperties method iSCSI Software Target API , MSFTSMNET_EthernetPort class
- MSFTSMNET_EthernetPort class iSCSI Software Target API , RestoreProperties method
topic_type:
- apiref
api_name:
- MSFTSMNET_EthernetPort.RestoreProperties
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RestoreProperties method of the MSFTSMNET\_EthernetPort class

Requests that the device return its configuration, setup, and/or state information to a previous state from a backing store. Typically this information is stored by using the [**SaveProperties**](saveproperties-msftsmnet-ethernetport.md) method.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSMNET\_EthernetPort**](msftsmnet-ethernetport.md)
</dt> <dt>

[**SaveProperties**](saveproperties-msftsmnet-ethernetport.md)
</dt> </dl>

 

 





