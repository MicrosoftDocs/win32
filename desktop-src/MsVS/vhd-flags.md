---
title: VHD\_FLAGS enumeration
description: Indicates options to be used when mounting a virtual hard disk (VHD) file with the MountVHD function.
ms.assetid: 'a89df5fe-d384-45e1-9642-10f646716f0e'
keywords: ["VHD_FLAGS enumeration Virtual Server"]
topic_type:
- apiref
api_name:
- VHD_FLAGS
api_location:
- VHDMount.h
api_type:
- HeaderDef
---

# VHD\_FLAGS enumeration

Indicates options to be used when mounting a virtual hard disk (VHD) file with the [**MountVHD**](mountvhd.md) function.

## Syntax


```C++
typedef enum _VHD_FLAGS { 
  VHD_NORMAL             = 0,
  VHD_NW_MAPPED          = 1,
  VHD_MOUNT_AS_READONLY  = 2,
  VHD_FORCE_UNMOUNT      = 3
} VHD_FLAGS;
```



## Constants

<dl> <dt>

<span id="VHD_NORMAL"></span><span id="vhd_normal"></span>**VHD\_NORMAL**
</dt> <dd>

Mount or unmount the VHD file normally.

</dd> <dt>

<span id="VHD_NW_MAPPED"></span><span id="vhd_nw_mapped"></span>**VHD\_NW\_MAPPED**
</dt> <dd>

This value is reserved.

</dd> <dt>

<span id="VHD_MOUNT_AS_READONLY"></span><span id="vhd_mount_as_readonly"></span>**VHD\_MOUNT\_AS\_READONLY**
</dt> <dd>

This value is reserved.

</dd> <dt>

<span id="VHD_FORCE_UNMOUNT"></span><span id="vhd_force_unmount"></span>**VHD\_FORCE\_UNMOUNT**
</dt> <dd>

Force the system to unmount the VHD file without sending any device eject notification. This could result in a message getting logged in the event viewer.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VHDMount.h</dt> </dl>             |



## See also

<dl> <dt>

[Virtual Server Enumerations](enumerations.md)
</dt> <dt>

[**MountVHD**](mountvhd.md)
</dt> <dt>

[**UnmountVHD**](unmountvhd.md)
</dt> </dl>

 

 





