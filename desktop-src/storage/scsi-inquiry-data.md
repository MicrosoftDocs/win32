---
title: SCSI\_INQUIRY\_DATA structure
description: The SCSI\_INQUIRY\_DATA structure is used in conjunction with the IOCTL\_SCSI\_GET\_INQUIRY\_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus.
ms.assetid: f62c35dd-791d-4c21-9836-308cc5fb102b
keywords:
- SCSI_INQUIRY_DATA structure Storage Devices
- PSCSI_INQUIRY_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSI_INQUIRY_DATA
api_location:
- ntddscsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSI\_INQUIRY\_DATA structure

The SCSI\_INQUIRY\_DATA structure is used in conjunction with the [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md) request to retrieve the SCSI inquiry data for all devices on a given SCSI bus.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_INQUIRY_DATA {
  UCHAR   PathId;
  UCHAR   TargetId;
  UCHAR   Lun;
  BOOLEAN DeviceClaimed;
  ULONG   InquiryDataLength;
  ULONG   NextInquiryDataOffset;
  UCHAR   InquiryData[1];
} SCSI_INQUIRY_DATA, *PSCSI_INQUIRY_DATA;
```



## Members

<dl> <dt>

**PathId**
</dt> <dd>

Indicates the number of the bus the device is located on.

</dd> <dt>

**TargetId**
</dt> <dd>

Indicates the number of the device on the bus.

</dd> <dt>

**Lun**
</dt> <dd>

Indicates the logical unit number of the logical unit on the target device.

</dd> <dt>

**DeviceClaimed**
</dt> <dd>

When **TRUE**, indicates that the device has been claimed by a class driver.

</dd> <dt>

**InquiryDataLength**
</dt> <dd>

Indicates the length in bytes of inquiry data.

</dd> <dt>

**NextInquiryDataOffset**
</dt> <dd>

Contains an offset to the inquiry data for the next logical unit on the target device.

</dd> <dt>

**InquiryData**
</dt> <dd>

Pointer to buffer containing the inquiry data for the logical unit.

</dd> </dl>

## Remarks

The [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md) request retrieves inquiry data for all devices associated with a specified adapter. An adapter can potentially have multiple buses. The **PathId** member identifies the bus. Each bus can have multiple target devices. The **TargetId** member identifies the target device, and each target device can have multiple logical units. The **Lun** member identifies the logical unit.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md)
</dt> <dt>

[**SCSI\_BUS\_DATA**](scsi-bus-data.md)
</dt> <dt>

[**SCSI\_ADAPTER\_BUS\_INFO**](scsi-adapter-bus-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_INQUIRY_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






