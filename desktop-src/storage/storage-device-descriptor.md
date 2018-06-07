---
title: STORAGE\_DEVICE\_DESCRIPTOR structure
description: The STORAGE\_DEVICE\_DESCRIPTOR structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the storage device descriptor data for a device.
ms.assetid: 99b270a0-0634-41a8-9de7-d2a2d4c3059f
keywords:
- STORAGE_DEVICE_DESCRIPTOR structure Storage Devices
- PSTORAGE_DEVICE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_DEVICE\_DESCRIPTOR structure

The **STORAGE\_DEVICE\_DESCRIPTOR** structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the storage device descriptor data for a device.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_DESCRIPTOR {
  ULONG            Version;
  ULONG            Size;
  UCHAR            DeviceType;
  UCHAR            DeviceTypeModifier;
  BOOLEAN          RemovableMedia;
  BOOLEAN          CommandQueueing;
  ULONG            VendorIdOffset;
  ULONG            ProductIdOffset;
  ULONG            ProductRevisionOffset;
  ULONG            SerialNumberOffset;
  STORAGE_BUS_TYPE BusType;
  ULONG            RawPropertiesLength;
  UCHAR            RawDeviceProperties[1];
} STORAGE_DEVICE_DESCRIPTOR, *PSTORAGE_DEVICE_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Indicates the size of the **STORAGE\_DEVICE\_DESCRIPTOR** structure. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the descriptor in bytes, including ID strings which are appended to the structure.

</dd> <dt>

**DeviceType**
</dt> <dd>

Specifies the device type as defined by the Small Computer Systems Interface (SCSI) specification.

</dd> <dt>

**DeviceTypeModifier**
</dt> <dd>

Specifies the device type modifier, if any, as defined by the SCSI specification. If no device type modifier exists, this member is zero.

</dd> <dt>

**RemovableMedia**
</dt> <dd>

Indicates when **TRUE** that the device's media (if any) is removable. If the device has no media, this member should be ignored. When **FALSE** the device's media is not removable.

</dd> <dt>

**CommandQueueing**
</dt> <dd>

Indicates when **TRUE** that the device supports multiple outstanding commands (SCSI tagged queuing or equivalent). When **FALSE**, the device does not support SCSI-tagged queuing or the equivalent. The STORPORT driver is responsible for synchronizing the commands.

</dd> <dt>

**VendorIdOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the structure to a **NULL**-terminated ASCII string that contains the device's vendor ID. If the device has no vendor ID, this member is zero.

</dd> <dt>

**ProductIdOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the structure to a **NULL**-terminated ASCII string that contains the device's product ID. If the device has no product ID, this member is zero.

</dd> <dt>

**ProductRevisionOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the structure to a **NULL**-terminated ASCII string that contains the device's product revision string. If the device has no product revision string, this member is zero.

</dd> <dt>

**SerialNumberOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the structure to a **NULL**-terminated ASCII string that contains the device's serial number. If the device has no serial number, this member is zero.

</dd> <dt>

**BusType**
</dt> <dd>

Specifies an enumerator value of type [**STORAGE\_BUS\_TYPE**](storage-bus-type.md) that indicates the type of bus to which the device is connected. This should be used to interpret the raw device properties at the end of this structure (if any).

</dd> <dt>

**RawPropertiesLength**
</dt> <dd>

Indicates the number of bytes of bus-specific data that have been appended to this descriptor.

</dd> <dt>

**RawDeviceProperties**
</dt> <dd>

Contains an array of length one that serves as a place holder for the first byte of the bus specific property data.

</dd> </dl>

## Remarks

Applications and storage class drivers issue a device-control request with the I/O control code [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve this structure, which contains information about a target device. The structure can be retrieved only from an FDO; attempting to retrieve device properties from an adapter causes an error.

An application or driver can determine the required buffer size by casting the retrieved **STORAGE\_DEVICE\_DESCRIPTOR** structure to a [**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md), which contains only **Version** and **Size**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
</dt> <dt>

[**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md)
</dt> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






