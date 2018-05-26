---
title: UFS\_FLAGS\_DESCRIPTOR enumeration
description: UFS\_FLAGS\_DESCRIPTOR describes the different types of flags used by Universal Flash Storage (UFS) descriptors.
ms.assetid: D530355F-5824-4F7C-84C4-57D3D03A7116
keywords:
- UFS_FLAGS_DESCRIPTOR enumeration Storage Devices
topic_type:
- apiref
api_name:
- UFS_FLAGS_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UFS\_FLAGS\_DESCRIPTOR enumeration

**UFS\_FLAGS\_DESCRIPTOR** describes the different types of flags used by Universal Flash Storage (UFS) descriptors.

## Syntax


```C++
typedef enum _UFS_FLAGS_DESCRIPTOR { 
  UFS_Reserved1                    = 0,
  UFS_fDeviceInit,
  UFS_fPermanentWPEn,
  UFS_fPowerOnWPEn,
  UFS_fBackgroundOpsEn,
  UFS_fDeviceLifeSpanModeEn,
  UFS_fPurgeEnable,
  UFS_Reserved2,
  UFS_fPhyResourceRemoval,
  UFS_fBusyRTC,
  UFS_Reserved3,
  UFS_fPermanentlyDisableFwUpdate,
  UFS_Reserved4,
  UFS_Reserved5
} UFS_FLAGS_DESCRIPTOR;
```



## Constants

<dl> <dt>

<span id="UFS_Reserved1"></span><span id="ufs_reserved1"></span><span id="UFS_RESERVED1"></span>**UFS\_Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="UFS_fDeviceInit"></span><span id="ufs_fdeviceinit"></span><span id="UFS_FDEVICEINIT"></span>**UFS\_fDeviceInit**
</dt> <dd>

Indicates the device initialization is in progress.

</dd> <dt>

<span id="UFS_fPermanentWPEn"></span><span id="ufs_fpermanentwpen"></span><span id="UFS_FPERMANENTWPEN"></span>**UFS\_fPermanentWPEn**
</dt> <dd>

Indicates permanent write protection is enabled.

</dd> <dt>

<span id="UFS_fPowerOnWPEn"></span><span id="ufs_fpoweronwpen"></span><span id="UFS_FPOWERONWPEN"></span>**UFS\_fPowerOnWPEn**
</dt> <dd>

Indicates power on write protection is enabled.

</dd> <dt>

<span id="UFS_fBackgroundOpsEn"></span><span id="ufs_fbackgroundopsen"></span><span id="UFS_FBACKGROUNDOPSEN"></span>**UFS\_fBackgroundOpsEn**
</dt> <dd>

Indicates the device is permitted to run background operations.

</dd> <dt>

<span id="UFS_fDeviceLifeSpanModeEn"></span><span id="ufs_fdevicelifespanmodeen"></span><span id="UFS_FDEVICELIFESPANMODEEN"></span>**UFS\_fDeviceLifeSpanModeEn**
</dt> <dd>

Indicates Device Life Span Mode is enabled.

</dd> <dt>

<span id="UFS_fPurgeEnable"></span><span id="ufs_fpurgeenable"></span><span id="UFS_FPURGEENABLE"></span>**UFS\_fPurgeEnable**
</dt> <dd>

Indicates Purge Operation is enabled.

</dd> <dt>

<span id="UFS_Reserved2"></span><span id="ufs_reserved2"></span><span id="UFS_RESERVED2"></span>**UFS\_Reserved2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="UFS_fPhyResourceRemoval"></span><span id="ufs_fphyresourceremoval"></span><span id="UFS_FPHYRESOURCEREMOVAL"></span>**UFS\_fPhyResourceRemoval**
</dt> <dd>

Indicates that the dynamic capacity operation occurs on the device's EndPointReset or a hardware reset. The host cannot reset this flag.

</dd> <dt>

<span id="UFS_fBusyRTC"></span><span id="ufs_fbusyrtc"></span><span id="UFS_FBUSYRTC"></span>**UFS\_fBusyRTC**
</dt> <dd>

Indicates the device is executing internal operation related to Real Time Clock.

</dd> <dt>

<span id="UFS_Reserved3"></span><span id="ufs_reserved3"></span><span id="UFS_RESERVED3"></span>**UFS\_Reserved3**
</dt> <dd>

Reserved for the Unified Memory Extension standard..

</dd> <dt>

<span id="UFS_fPermanentlyDisableFwUpdate"></span><span id="ufs_fpermanentlydisablefwupdate"></span><span id="UFS_FPERMANENTLYDISABLEFWUPDATE"></span>**UFS\_fPermanentlyDisableFwUpdate**
</dt> <dd>

Indicates the UFS device will permanently disallow future firmware updates to the Universal Flash Storage (UFS) device.

</dd> <dt>

<span id="UFS_Reserved4"></span><span id="ufs_reserved4"></span><span id="UFS_RESERVED4"></span>**UFS\_Reserved4**
</dt> <dd>

Reserved for the Unified Memory Extension standard.

</dd> <dt>

<span id="UFS_Reserved5"></span><span id="ufs_reserved5"></span><span id="UFS_RESERVED5"></span>**UFS\_Reserved5**
</dt> <dd>

Reserved for the Unified Memory Extension standard.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_FLAGS_DESCRIPTOR%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





