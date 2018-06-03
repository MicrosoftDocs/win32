---
title: UFS\_POWER\_DESCRIPTOR structure
description: UFS\_POWER\_DESCRIPTOR contains information about the power capabilities and power states of the device.
ms.assetid: FCF9DCD1-2C04-47E3-97C5-7ACC28B28C6C
keywords:
- UFS_POWER_DESCRIPTOR structure Storage Devices
- PUFS_POWER_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- UFS_POWER_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UFS\_POWER\_DESCRIPTOR structure

**UFS\_POWER\_DESCRIPTOR** contains information about the power capabilities and power states of the device.

## Syntax


```C++
typedef struct _UFS_POWER_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR wActiveICCLevelsVCC[32];
  UCHAR wActiveICCLevelsVCCQ[32];
  UCHAR wActiveICCLevelsVCCQ2[32];
} UFS_POWER_DESCRIPTOR, *PUFS_POWER_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the type of the descriptor. This descriptor will have a value of **UFS\_DESC\_POWER\_IDN**.

</dd> <dt>

**wActiveICCLevelsVCC**
</dt> <dd>

Specifies the maximum VCC current value for each UFS\_bActiveICCLevel, based on the index value.

</dd> <dt>

**wActiveICCLevelsVCCQ**
</dt> <dd>

Specifies the maximum VCCQ current value for each UFS\_bActiveICCLevel, based on the index value.

</dd> <dt>

**wActiveICCLevelsVCCQ2**
</dt> <dd>

Specifies the maximum VCCQ current value for each UFS\_bActiveICCLevel, based on the index value.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_POWER_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





