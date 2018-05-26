---
title: SCSI\_BUS\_DATA structure
description: The SCSI\_BUS\_DATA structure is used in conjunction with the IOCTL\_SCSI\_GET\_INQUIRY\_DATA request and the SCSI\_ADAPTER\_BUS\_INFO structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus.
ms.assetid: d7baddb5-ad12-4aea-9515-97511dc05fe7
keywords:
- SCSI_BUS_DATA structure Storage Devices
- PSCSI_BUS_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSI_BUS_DATA
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

# SCSI\_BUS\_DATA structure

The SCSI\_BUS\_DATA structure is used in conjunction with the [**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md) request and the [**SCSI\_ADAPTER\_BUS\_INFO**](scsi-adapter-bus-info.md) structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_BUS_DATA {
  UCHAR NumberOfLogicalUnits;
  UCHAR InitiatorBusId;
  ULONG InquiryDataOffset;
} SCSI_BUS_DATA, *PSCSI_BUS_DATA;
```



## Members

<dl> <dt>

**NumberOfLogicalUnits**
</dt> <dd>

Contains the number of logical units on the bus for which inquiry data is being retrieved.

</dd> <dt>

**InitiatorBusId**
</dt> <dd>

Contains the SCSI bus ID for the adapter.

</dd> <dt>

**InquiryDataOffset**
</dt> <dd>

Contains an offset from the beginning of the SCSI\_ADAPTER\_BUS\_INFO structure to the inquiry data.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](ioctl-scsi-get-inquiry-data.md)
</dt> <dt>

[**SCSI\_ADAPTER\_BUS\_INFO**](scsi-adapter-bus-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_BUS_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






