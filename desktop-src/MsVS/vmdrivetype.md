---
title: VMDriveType enumeration
description: The VMDriveType enumeration specifies the type of drive attached to a bus location.
ms.assetid: 4a89c407-11c6-4d5b-9281-70aab9eb3a7a
keywords:
- VMDriveType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMDriveType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMDriveType enumeration

The **VMDriveType** enumeration specifies the type of drive attached to a bus location.

## Syntax


```C++
typedef enum  { 
  vmDriveType_Null      = 0,
  vmDriveType_HardDisk  = 1,
  vmDriveType_DVD       = 2
} VMDriveType;
```



## Constants

<dl> <dt>

<span id="vmDriveType_Null"></span><span id="vmdrivetype_null"></span><span id="VMDRIVETYPE_NULL"></span>**vmDriveType\_Null**
</dt> <dd>

No drive attached.

</dd> <dt>

<span id="vmDriveType_HardDisk"></span><span id="vmdrivetype_harddisk"></span><span id="VMDRIVETYPE_HARDDISK"></span>**vmDriveType\_HardDisk**
</dt> <dd>

Hard disk attached.

</dd> <dt>

<span id="vmDriveType_DVD"></span><span id="vmdrivetype_dvd"></span><span id="VMDRIVETYPE_DVD"></span>**vmDriveType\_DVD**
</dt> <dd>

CD/DVD drive attached.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





