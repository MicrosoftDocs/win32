---
title: RescanExtents method of the MSFTSM\_ComputerSystem class
description: Discovers newly added and newly removed storage extents, specifically Windows disks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c690a6e7-47f1-4b0c-9237-d4aded3ff1f3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RescanExtents method iSCSI Software Target API
- RescanExtents method iSCSI Software Target API , MSFTSM_ComputerSystem class
- MSFTSM_ComputerSystem class iSCSI Software Target API , RescanExtents method
topic_type:
- apiref
api_name:
- MSFTSM_ComputerSystem.RescanExtents
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RescanExtents method of the MSFTSM\_ComputerSystem class

Discovers newly added and newly removed storage extents, specifically Windows disks.

## Syntax


```mof
uint32 RescanExtents();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**Failed** (1)
</dt> <dt>

**Not Supported** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSM\_ComputerSystem**](msftsm-computersystem.md)
</dt> </dl>

 

 





