---
title: UFS\_DEVICE\_DESCRIPTOR structure
description: UFS\_DEVICE\_DESCRIPTOR is the main descriptor for Universal Flash Storage (UFS) devices and should be the first descriptor retrieved as it specifies the device class and sub-class and the protocol (command set) to use to access this device and the maximum number of logical units contained within the device.
ms.assetid: CD1F59DA-3D84-422B-A862-8F4C5E1AA515
keywords:
- UFS_DEVICE_DESCRIPTOR structure Storage Devices
- PUFS_DEVICE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- UFS_DEVICE_DESCRIPTOR
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

# UFS\_DEVICE\_DESCRIPTOR structure

**UFS\_DEVICE\_DESCRIPTOR** is the main descriptor for Universal Flash Storage (UFS) devices and should be the first descriptor retrieved as it specifies the device class and sub-class and the protocol (command set) to use to access this device and the maximum number of logical units contained within the device.

## Syntax


```C++
typedef struct _UFS_DEVICE_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bDevice;
  UCHAR bDeviceClass;
  UCHAR bDeviceSubClass;
  UCHAR bProtocol;
  UCHAR  bNumberLU;
  UCHAR bNumberWLU;
  UCHAR bBootEnable;
  UCHAR bDescrAccessEn;
  UCHAR bInitPowerMode;
  UCHAR bHighPriorityLUN;
  UCHAR bSecureRemovalType;
  UCHAR bSecurityLU;
  UCHAR bBackgroundOpsTermLat;
  UCHAR bInitActiveICCLevel;
  UCHAR wSpecVersion[2];
  UCHAR wManufactureDate[2];
  UCHAR iManufacturerName;
  UCHAR iProductName;
  UCHAR iSerialNumberID;
  UCHAR iOemID;
  UCHAR wManufacturerID[2];
  UCHAR bUD0BaseOffset;
  UCHAR bUDConfigPLength;
  UCHAR bDeviceRTTCap;
  UCHAR wPeriodicRTCUpdate[2];
  UCHAR bUFSFeaturesSupport;
  UCHAR bFFUTimeout;
  UCHAR bQueueDepth;
  UCHAR wDeviceVersion[2];
  UCHAR bNumSecureWPArea;
  UCHAR dPSAMaxDataSize[4];
  UCHAR bPSAStateTimeout;
  UCHAR  iProductRevisionLevel;
  UCHAR Reserved[5];
  UCHAR Reserved2[16];
} UFS_DEVICE_DESCRIPTOR, *PUFS_DEVICE_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the type of the descriptor. This descriptor will have a value of **UFS\_DESC\_DEVICE\_IDN**.

</dd> <dt>

**bDevice**
</dt> <dd>

Specifies the device type.



| Value            | Description              |
|------------------|--------------------------|
| 0x00             | Device                   |
| All other values | Reserved for future use. |



 

</dd> <dt>

**bDeviceClass**
</dt> <dd>

Specifies the device class.



| Value            | Description              |
|------------------|--------------------------|
| 0x00             | Mass Storage             |
| All other values | Reserved for future use. |



 

</dd> <dt>

**bDeviceSubClass**
</dt> <dd>

Specifies the UFS mass storage subclasses in a bit map as follows:



| Bit              | Value                        |
|------------------|------------------------------|
| 0                | Bootable / Non-Bootable      |
| 1                | Embedded / Removable         |
| 2                | Reserved for JESD220-1 (UME) |
| All other values | Reserved for future use.     |



 

</dd> <dt>

**bProtocol**
</dt> <dd>

Specifies the protocol support by the UFS device.



| Value            | Description              |
|------------------|--------------------------|
| 0x00             | SCSI                     |
| All other values | Reserved for future use. |



 

</dd> <dt>

 **bNumberLU**
</dt> <dd>

Specifies the number of Logical Units. This does not include the number of well known logical units.

</dd> <dt>

**bNumberWLU**
</dt> <dd>

Specifies the number of well known logical units.

</dd> <dt>

**bBootEnable**
</dt> <dd>

Specifies if a device's boot feature is enabled.



| Value            | Description              |
|------------------|--------------------------|
| 0x00             | Boot feature disabled    |
| 0x01             | Boot feature enabled     |
| All other values | Reserved for future use. |



 

</dd> <dt>

**bDescrAccessEn**
</dt> <dd>

Indicates whether the Device Descriptor can be read after the partial initialization phase of the boot sequence.



| Value            | Description                       |
|------------------|-----------------------------------|
| 0x00             | Device Descriptor access disabled |
| 0x01             | Device Descriptor access enabled  |
| All other values | Reserved for future use.          |



 

</dd> <dt>

**bInitPowerMode**
</dt> <dd>

**bInitPowerMode** defines the Power Mode after device initialization or hardware reset.



| Value            | Description              |
|------------------|--------------------------|
| 0x00             | UFS-Sleep mode           |
| 0x01             | Active-mode              |
| All other values | Reserved for future use. |



 

</dd> <dt>

**bHighPriorityLUN**
</dt> <dd>

**bHighPriorityLUN** defines the high priority logical unit.

</dd> <dt>

**bSecureRemovalType**
</dt> <dd>

Specifies the secure removal type.



| Value            | Description                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| 0x00             | Information removed by an erase of the physical memory                                                                |
| 0x01             | Information removed by overwriting the addressed locations with a single character followed by an erase.              |
| 0x02             | Information removed by overwriting the addressed locations with a character, its complement, then a random character. |
| 0x03             | Information removed using a vendor define mechanism.                                                                  |
| All other values | Reserved for future use.                                                                                              |



 

</dd> <dt>

**bSecurityLU**
</dt> <dd>

Specifies if there is support for security LU's



| Value            | Description                          |
|------------------|--------------------------------------|
| 0x00             | Not supported                        |
| 0x01             | Replay Protected Memory Block (RPMB) |
| All other values | Reserved for future use.             |



 

</dd> <dt>

**bBackgroundOpsTermLat**
</dt> <dd>

**bBackgroundOpsTermLat** defines the maximum latency for starting data transmission when background operations are ongoing. The termination latency limit applies to two cases:

-   When the device receives a COMMAND UFS Protocol Information Units (UPIU) with a transfer request. The device shall start the data transfer and send a DATA IN UPIU or a RTT UPIU within the latency limit.
-   When the device receives QUERY REQUEST UPIU to clear the **fBackgroundOpsEn** Flag. The device is expected to terminate background operations within the latency limit.

</dd> <dt>

**bInitActiveICCLevel**
</dt> <dd>

**bInitActiveICCLevel** defines the **bActiveICCLevel** value after power on or reset. The range of the value is from 0x00 to 0x0F.

</dd> <dt>

**wSpecVersion**
</dt> <dd>

Indicates the specification version in Binary Coded Decimal (BCD) format.

</dd> <dt>

**wManufactureDate**
</dt> <dd>

Specifies the manufacturing date in BCD format as 0xMMYY.

</dd> <dt>

**iManufacturerName**
</dt> <dd>

Contains an index value to the string which contains the manufacturer's name.

</dd> <dt>

**iProductName**
</dt> <dd>

Contains an index value to the string which contains the product's name.

</dd> <dt>

**iSerialNumberID**
</dt> <dd>

Contains an index value to the string which contains the serial's number.

</dd> <dt>

**iOemID**
</dt> <dd>

Contains an index value to the string which contains the OEM ID.

</dd> <dt>

**wManufacturerID**
</dt> <dd>

Specifies the Manufacturer ID of the device.

</dd> <dt>

**bUD0BaseOffset**
</dt> <dd>

Specifies the Offset of Unit Descriptor 0's configurable parameters within the Configuration Descriptor, [**UFS\_CONFIG\_DESCRIPTOR**](ufs-config-descriptor.md).

</dd> <dt>

**bUDConfigPLength**
</dt> <dd>

Total size of a **UFS\_UNIT\_CONFIG\_DESCRIPTOR**'s parameters.

</dd> <dt>

**bDeviceRTTCap**
</dt> <dd>

Specifies the maximum number of outstanding READY TO TRANSFER UPIU'S supported by device. The minimum value is 2.

</dd> <dt>

**wPeriodicRTCUpdate**
</dt> <dd>

Specifies the frequency and method of real-time clock updates. Bits 10 to 15 are reserved.

</dd> <dt>

**bUFSFeaturesSupport**
</dt> <dd>

Specifies which features are supported on this device. A feature is supported if its related bit is set to 1.



| Bit              | Value                           |
|------------------|---------------------------------|
| 0                | Field Firmware Update (FFU)     |
| 1                | Production State Awarness (PSA) |
| 2                | Device Life Span                |
| All other values | Reserved for future use.        |



 

</dd> <dt>

**bFFUTimeout**
</dt> <dd>

The maximum time, in seconds, that access to the device is limited or not possible through any ports associated due to execution of a WRITE BUFFER command.

</dd> <dt>

**bQueueDepth**
</dt> <dd>

Specifies the queue depth. If this member is equal to 0, the device implements the per-LU queuing architecture.

</dd> <dt>

**wDeviceVersion**
</dt> <dd>

Specifies the device version.

</dd> <dt>

**bNumSecureWPArea**
</dt> <dd>

Specifies the total number of Secure Write Protect Areas supported by the device. The value of this member is between **bNumberLU** and 32

</dd> <dt>

**dPSAMaxDataSize**
</dt> <dd>

Specifies the maximum amount of data that may be written during the pre-soldering phase of the PSA flow.

</dd> <dt>

**bPSAStateTimeout**
</dt> <dd>

Specifies the command maximum timeout for a change in **bPSAState**. The timeout value is calculated as follows (in microseconds):

100 x 2 ^ **bPSAStateTimeout**

</dd> <dt>

 **iProductRevisionLevel**
</dt> <dd>

Specifies the index to the string which contains the Product Revision Level.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Remarks

If **bBootEnable** in the **UFS\_DEVICE\_DESCRIPTOR** is set to zero or if the Boot well known logical unit is not mapped to an enabled logical unit, then the Boot well known logical unit shall terminate.

**UFS\_DEVICE\_DESCRIPTOR** is read only, some of its parameters may be changed by changing the corresponding parameter in [**UFS\_UNIT\_CONFIG\_DESCRIPTOR**](ufs-unit-config-descriptor.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



## See also

<dl> <dt>

[**UFS\_UNIT\_CONFIG\_DESCRIPTOR**](ufs-unit-config-descriptor.md)
</dt> <dt>

[**UFS\_CONFIG\_DESCRIPTOR**](ufs-config-descriptor.md)
</dt> <dt>

[**UFS\_GEOMETRY\_DESCRIPTOR**](ufs-geometry-descriptor.md)
</dt> <dt>

[**UFS\_UNIT\_DESCRIPTOR**](ufs-unit-descriptor.md)
</dt> <dt>

[**UFS\_RPMB\_UNIT\_DESCRIPTOR**](ufs-rpmb-unit-descriptor.md)
</dt> <dt>

[**UFS\_POWER\_DESCRIPTOR**](ufs-power-descriptor.md)
</dt> <dt>

[**UFS\_INTERCONNECT\_DESCRIPTOR**](ufs-interconnect-descriptor.md)
</dt> <dt>

[**UFS\_STRING\_DESCRIPTOR**](ufs-string-descriptor.md)
</dt> <dt>

[**UFS\_DEVICE\_HEALTH\_DESCRIPTOR**](ufs-device-health-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_DEVICE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






