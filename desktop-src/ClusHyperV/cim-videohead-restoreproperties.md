---
title: RestoreProperties method of the CIM\_VideoHead class
description: Restores a previous configuration and state of the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60aa4d23-d15a-4586-bfe7-306a1edbff63'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RestoreProperties method", "RestoreProperties method, CIM_VideoHead class", "CIM_VideoHead class, RestoreProperties method"]
topic_type:
- apiref
api_name:
- CIM_VideoHead.RestoreProperties
api_location:
- VMMS.exe
api_type:
- COM
---

# RestoreProperties method of the CIM\_VideoHead class

Restores a previous configuration and state of the logical device.

## Syntax


```mof
uint32 RestoreProperties();
```



## Parameters

This method has no parameters.

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

The operation completed successfully.

</dd> <dt>


</dt> <dd>

1

The operation was not completed because it is not supported.

</dd> <dt>


</dt> <dd>

2–...

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VideoHead**](cim-videohead.md)
</dt> </dl>

 

 





