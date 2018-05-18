---
title: LockMedia method of the CIM\_DVDDrive class
description: Represents a device that can use media to store and retrieve data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2a3a94a7-de70-4aa3-bec9-41b26f5fefc1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["LockMedia method", "LockMedia method, CIM_DVDDrive class", "CIM_DVDDrive class, LockMedia method"]
topic_type:
- apiref
api_name:
- CIM_DVDDrive.LockMedia
api_location:
- VMMS.exe
api_type:
- COM
---

# LockMedia method of the CIM\_DVDDrive class

Represents a device that can use media to store and retrieve data.

## Syntax


```mof
uint32 LockMedia(
  [in] boolean Lock
);
```



## Parameters

<dl> <dt>

*Lock* \[in\]
</dt> <dd>

**true** to lock the media, or **false** to unlock the media.

</dd> </dl>

## Return value

This method returns "0" if successful, "1" if not supported, and any other value if an error occurred.

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

[**CIM\_DVDDrive**](cim-dvddrive.md)
</dt> </dl>

 

 





