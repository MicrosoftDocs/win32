---
title: WT\_DVMountedPath class
description: Represents the mount point path of the shadow copy that was mounted locally on the iSCSI Target server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ea4d4f2-d972-44ce-9b25-458999aa18dc
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_DVMountedPath class iSCSI Software Target API
- WT_DVMountedPath class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_DVMountedPath
- WT_DVMountedPath.WTD
- WT_DVMountedPath.MountedPath
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_DVMountedPath class

Represents the mount point path of the shadow copy that was mounted locally on the iSCSI Target server.

**Windows Server 2012 R2:** This class is deprecated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_DVMountedPath
{
  uint32 WTD;
  string MountedPath;
};
```

## Members

The **WT\_DVMountedPath** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_DVMountedPath** class has these properties.

<dl> <dt>

**MountedPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume mount point of the locally mounted shadow copy. The related [**WT\_Disk**](wt-disk.md) object must have its **DVMountStatus** set to **MountSnapshot**.

</dd> <dt>

**WTD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Index of the locally mounted [**WT\_Disk**](wt-disk.md).

</dd> </dl>

## Remarks

**WT\_DVMountedPath** is similar to the [**WT\_Disk.GetDVMountPoints**](getdvmountpoints-wt-disk.md) method, but instead enumerates all mount points of all virtual disks that were mounted locally.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





