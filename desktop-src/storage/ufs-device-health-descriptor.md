---
title: UFS\_DEVICE\_HEALTH\_DESCRIPTOR structure
description: The UFS\_DEVICE\_HEALTH\_DESCRIPTOR structure describes the health of a device.
ms.assetid: 6B085DBB-2AAA-4170-A2B1-EA4D2C207A24
keywords:
- UFS_DEVICE_HEALTH_DESCRIPTOR structure Storage Devices
- PUFS_DEVICE_HEALTH_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- UFS_DEVICE_HEALTH_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UFS\_DEVICE\_HEALTH\_DESCRIPTOR structure

The **UFS\_DEVICE\_HEALTH\_DESCRIPTOR** structure describes the health of a device.

## Syntax


```C++
typedef struct _UFS_DEVICE_HEALTH_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bPreEOLInfo;
  UCHAR bDeviceLifeTimeEstA;
  UCHAR bDeviceLifeTimeEstB;
  UCHAR VendorPropInfo[32];
} UFS_DEVICE_HEALTH_DESCRIPTOR, *PUFS_DEVICE_HEALTH_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the descriptor's Identification value. **UFS\_DEVICE\_HEALTH\_DESCRIPTOR** will have a value of **UFS\_DESC\_HEALTH\_IDN**.

</dd> <dt>

**bPreEOLInfo**
</dt> <dd>

Contains Pre-End of Life Information. This member supplies information about a device's life time as reflected by the average number of reserved blocks. Contains one of the following values:



| Value            | Description                                        |
|------------------|----------------------------------------------------|
| 0x00             | Member is not defined.                             |
| 0x01             | Normal. Consumed less than 80% of reserved blocks. |
| 0x02             | Consumed 80% of reserved blocks.                   |
| 0x03             | Critical. Consumed 90% of reserved blocks.         |
| All other values | Reserved for future use.                           |



 

</dd> <dt>

**bDeviceLifeTimeEstA**
</dt> <dd>

**bDeviceLifeTimeEstA** provides an estimation of how much of a device's estimated life time has been used based on the amount of performed program/erase cycles. This calculation is vendor-specific and is referred as method A. Contains one of the following values:



| Value            | Description                                                    |
|------------------|----------------------------------------------------------------|
| 0x00             | Information about device's life time not found.                |
| 0x01             | 0% to 10% of the device's estimated life time has been used.   |
| 0x02             | 10% to 20% of the device's estimated life time has been used.  |
| 0x03             | 20% to 30% of the device's estimated life time has been used.  |
| 0x04             | 30% to 40% of the device's estimated life time has been used.  |
| 0x05             | 40% to 50% of the device's estimated life time has been used.  |
| 0x06             | 50% to 60% of the device's estimated life time has been used.  |
| 0x07             | 60% to 70% of the device's estimated life time has been used.  |
| 0x08             | 70% to 80% of the device's estimated life time has been used.  |
| 0x09             | 80% to 90% of the device's estimated life time has been used.  |
| 0x0A             | 90% to 100% of the device's estimated life time has been used. |
| 0x0B             | Device has exceeded it's estimated life time.                  |
| All other values | Reserved for future use.                                       |



 

</dd> <dt>

**bDeviceLifeTimeEstB**
</dt> <dd>

**bDeviceLifeTimeEstB** provides an estimation of how much of a device's estimated life time has been used based on the amount of performed program/erase cycles. This calculation is vendor-specific and is referred as method B. Contains the same possible values as **bDeviceLifeTimeEstA**.

</dd> <dt>

**VendorPropInfo\[32\]**
</dt> <dd>

Reserved for vendor use.

</dd> </dl>

## Remarks

The UFS Host Controller contains a series of configurable Descriptor Tables, which allow the driver to query and configure the host controller s capabilities. Query the Requested Descriptor from the Descriptor Table on the device.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_DEVICE_HEALTH_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





