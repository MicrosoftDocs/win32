---
title: ImportWTDisk method of the WT\_Disk class
description: Import an existing VHD or SCSI device as a iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e0d3a11d-a999-4bb9-9838-12e236c6a477
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportWTDisk method iSCSI Software Target API
- ImportWTDisk method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , ImportWTDisk method
topic_type:
- apiref
api_name:
- WT_Disk.ImportWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ImportWTDisk method of the WT\_Disk class

Import an existing VHD or SCSI device as a iSCSI virtual disk.

## Syntax


```mof
WT_Disk ImportWTDisk(
  [in] string DevicePath,
  [in] string Description,
  [in] string ResourceGroup
);
```



## Parameters

<dl> <dt>

*DevicePath* \[in\]
</dt> <dd>

Full path to an existing VHD file or a decorated path in the format of "SCSI:" to a pass-through SCSI device.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

iSCSI disk description.

</dd> <dt>

*ResourceGroup* \[in\]
</dt> <dd>

Cluster resource group name (only needed to import a SCSI device in a cluster).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>Wmiwtprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> </dl>

 

 





