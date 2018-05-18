---
title: VMDVDDriveAttachmentType enumeration
description: The VMDVDDriveAttachmentType enumeration specifies what is attached to a DVD drive.
ms.assetid: '60a98e93-626a-423c-b87a-b1dc95cf9f1e'
keywords: ["VMDVDDriveAttachmentType enumeration Virtual Server"]
topic_type:
- apiref
api_name:
- VMDVDDriveAttachmentType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMDVDDriveAttachmentType enumeration

The **VMDVDDriveAttachmentType** enumeration specifies what is attached to a DVD drive.

## Syntax


```C++
typedef enum  { 
  vmDVDDrive_None       = 0,
  vmDVDDrive_Image      = 1,
  vmDVDDrive_HostDrive  = 2
} VMDVDDriveAttachmentType;
```



## Constants

<dl> <dt>

<span id="vmDVDDrive_None"></span><span id="vmdvddrive_none"></span><span id="VMDVDDRIVE_NONE"></span>**vmDVDDrive\_None**
</dt> <dd>

Nothing attached.

</dd> <dt>

<span id="vmDVDDrive_Image"></span><span id="vmdvddrive_image"></span><span id="VMDVDDRIVE_IMAGE"></span>**vmDVDDrive\_Image**
</dt> <dd>

ISO image file attached.

</dd> <dt>

<span id="vmDVDDrive_HostDrive"></span><span id="vmdvddrive_hostdrive"></span><span id="VMDVDDRIVE_HOSTDRIVE"></span>**vmDVDDrive\_HostDrive**
</dt> <dd>

Host CD or DVD drive attached.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





