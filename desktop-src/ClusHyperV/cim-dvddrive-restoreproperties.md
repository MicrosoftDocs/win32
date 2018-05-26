---
title: RestoreProperties method of the CIM\_DVDDrive class
description: Restores a previous configuration and state of the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 595ac10a-7f30-4f52-81ce-3d79370dc776
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RestoreProperties method
- RestoreProperties method, CIM_DVDDrive class
- CIM_DVDDrive class, RestoreProperties method
topic_type:
- apiref
api_name:
- CIM_DVDDrive.RestoreProperties
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RestoreProperties method of the CIM\_DVDDrive class

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

2 ...

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_DVDDrive**](cim-dvddrive.md)
</dt> </dl>

 

 





