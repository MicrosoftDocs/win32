---
title: SaveProperties method of the MSFTSMNET\_EthernetPort class
description: Requests that the device capture its current configuration, setup, and/or state information in a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e3671d95-28ca-4dd2-8430-01c2f12e5d52'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SaveProperties method iSCSI Software Target API", "SaveProperties method iSCSI Software Target API , MSFTSMNET_EthernetPort class", "MSFTSMNET_EthernetPort class iSCSI Software Target API , SaveProperties method"]
topic_type:
- apiref
api_name:
- MSFTSMNET_EthernetPort.SaveProperties
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# SaveProperties method of the MSFTSMNET\_EthernetPort class

Requests that the device capture its current configuration, setup, and/or state information in a backing store. This information can be restored at a later time by using the [**RestoreProperties**](restoreproperties-msftsmnet-ethernetport.md) method.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Syntax


```mof
uint32 SaveProperties();
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

[**MSFTSMNET\_EthernetPort**](msftsmnet-ethernetport.md)
</dt> <dt>

[**RestoreProperties**](restoreproperties-msftsmnet-ethernetport.md)
</dt> </dl>

 

 





