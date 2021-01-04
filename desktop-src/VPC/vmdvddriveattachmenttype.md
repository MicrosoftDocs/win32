---
title: VMDVDDriveAttachmentType enumeration (VPCCOMInterfaces.h)
description: Specifies what is attached to a DVD drive.
ms.assetid: 66f33974-8622-4fa3-b5ac-3fae5a637434
keywords:
- VMDVDDriveAttachmentType enumeration Virtual PC
topic_type:
- apiref
api_name:
- VMDVDDriveAttachmentType
api_location:
- VPCCOMInterfaces.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# VMDVDDriveAttachmentType enumeration

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Specifies what is attached to a DVD drive.

## Syntax


```C++
typedef enum  { 
  vmDVDDrive_None       = 0,
  vmDVDDrive_Image      = 1,
  vmDVDDrive_HostDrive  = 2
} VMDVDDriveAttachmentType;
```



## Constants

<dl> <dt>

<span id="vmDVDDrive_None"></span><span id="vmdvddrive_none"></span><span id="VMDVDDRIVE_NONE"></span>**vmDVDDrive\_None**
</dt> <dd>

There is nothing attached.

</dd> <dt>

<span id="vmDVDDrive_Image"></span><span id="vmdvddrive_image"></span><span id="VMDVDDRIVE_IMAGE"></span>**vmDVDDrive\_Image**
</dt> <dd>

There is an ISO image file attached.

</dd> <dt>

<span id="vmDVDDrive_HostDrive"></span><span id="vmdvddrive_hostdrive"></span><span id="VMDVDDRIVE_HOSTDRIVE"></span>**vmDVDDrive\_HostDrive**
</dt> <dd>

There is a host CD or DVD drive attached.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |



## See also

<dl> <dt>

[**IVMDVDDrive::Attachment**](ivmdvddrive-attachment.md)
</dt> </dl>

 

