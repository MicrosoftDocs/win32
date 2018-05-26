---
title: GetDVMountPoints method of the WT\_Disk class
description: Returns a list of all volume mount points that are associated with a virtual disk that was mounted via Data View.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6ddd0fc0-7e47-4e2d-b677-4abaf227677f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDVMountPoints method iSCSI Software Target API
- GetDVMountPoints method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , GetDVMountPoints method
topic_type:
- apiref
api_name:
- WT_Disk.GetDVMountPoints
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetDVMountPoints method of the WT\_Disk class

Returns a list of all volume mount points that are associated with a virtual disk that was mounted via Data View. This is used for locally mounted shadow copies.

**Windows Server 2012 R2:** This method is deprecated.

## Syntax


```mof
sint32 GetDVMountPoints(
  [out] string MountPoints[]
);
```



## Parameters

<dl> <dt>

*MountPoints* \[out\]
</dt> <dd>

An array of strings that contain volume mount points.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> </dl>

 

 





