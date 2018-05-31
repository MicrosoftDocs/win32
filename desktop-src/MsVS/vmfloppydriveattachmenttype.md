---
title: VMFloppyDriveAttachmentType enumeration
description: The VMFloppyDriveAttachmentType enumeration specifies what is attached to a floppy drive.
ms.assetid: 83276b8d-5025-4c44-a28d-f41d6fc9dec9
keywords:
- VMFloppyDriveAttachmentType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMFloppyDriveAttachmentType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# VMFloppyDriveAttachmentType enumeration

The **VMFloppyDriveAttachmentType** enumeration specifies what is attached to a floppy drive.

## Syntax


```C++
typedef enum  { 
  vmFloppyDrive_None       = 0,
  vmFloppyDrive_Image      = 1,
  vmFloppyDrive_HostDrive  = 2
} VMFloppyDriveAttachmentType;
```



## Constants

<dl> <dt>

<span id="vmFloppyDrive_None"></span><span id="vmfloppydrive_none"></span><span id="VMFLOPPYDRIVE_NONE"></span>**vmFloppyDrive\_None**
</dt> <dd>

Nothing attached.

</dd> <dt>

<span id="vmFloppyDrive_Image"></span><span id="vmfloppydrive_image"></span><span id="VMFLOPPYDRIVE_IMAGE"></span>**vmFloppyDrive\_Image**
</dt> <dd>

Floppy disk image file attached.

</dd> <dt>

<span id="vmFloppyDrive_HostDrive"></span><span id="vmfloppydrive_hostdrive"></span><span id="VMFLOPPYDRIVE_HOSTDRIVE"></span>**vmFloppyDrive\_HostDrive**
</dt> <dd>

Host floppy drive attached.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





