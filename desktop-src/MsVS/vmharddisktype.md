---
title: VMHardDiskType enumeration
description: The VMHardDiskType enumeration specifies a hard disk image type.
ms.assetid: 4f76b8ab-56cb-4b41-bdeb-6e9f78de529c
keywords:
- VMHardDiskType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMHardDiskType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VMHardDiskType enumeration

The **VMHardDiskType** enumeration specifies a hard disk image type.

## Syntax


```C++
typedef enum  { 
  vmDiskType_Dynamic       = 0,
  vmDiskType_FixedSize     = 1,
  vmDiskType_Differencing  = 2,
  vmDiskType_HostDrive     = 4
} VMHardDiskType;
```



## Constants

<dl> <dt>

<span id="vmDiskType_Dynamic"></span><span id="vmdisktype_dynamic"></span><span id="VMDISKTYPE_DYNAMIC"></span>**vmDiskType\_Dynamic**
</dt> <dd>

Dynamically expanding hard disk image.

</dd> <dt>

<span id="vmDiskType_FixedSize"></span><span id="vmdisktype_fixedsize"></span><span id="VMDISKTYPE_FIXEDSIZE"></span>**vmDiskType\_FixedSize**
</dt> <dd>

Fixed-size hard disk image.

</dd> <dt>

<span id="vmDiskType_Differencing"></span><span id="vmdisktype_differencing"></span><span id="VMDISKTYPE_DIFFERENCING"></span>**vmDiskType\_Differencing**
</dt> <dd>

Differencing hard disk image.

</dd> <dt>

<span id="vmDiskType_HostDrive"></span><span id="vmdisktype_hostdrive"></span><span id="VMDISKTYPE_HOSTDRIVE"></span>**vmDiskType\_HostDrive**
</dt> <dd>

Hard disk image linked to a host drive.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





