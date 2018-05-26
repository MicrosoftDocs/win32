---
title: CDROM\_WRITE\_SPEED\_DESCRIPTOR structure
description: The CDROM\_WRITE\_SPEED\_DESCRIPTOR structure is returned for the IOCTL\_CDROM\_GET\_PERFORMANCE IOCTL when the request type is CdromWriteSpeedRequest.
ms.assetid: 21CFAA26-3E11-4E3B-949A-C905813E56A8
keywords:
- CDROM_WRITE_SPEED_DESCRIPTOR structure Storage Devices
- PCDROM_WRITE_SPEED_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_WRITE_SPEED_DESCRIPTOR
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_WRITE\_SPEED\_DESCRIPTOR structure

The **CDROM\_WRITE\_SPEED\_DESCRIPTOR** structure is returned for the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) IOCTL when the request type is **CdromWriteSpeedRequest**. The IOCTL returns the [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md) followed by one or more descriptors of type **CDROM\_WRITE\_SPEED\_DESCRIPTOR**.

## Syntax


```C++
typedef struct _CDROM_WRITE_SPEED_DESCRIPTOR {
  UCHAR MixedReadWrite  :1;
  UCHAR  Exact  :1;
  UCHAR  Reserved1  :1;
  UCHAR   WriteRotationControl  :2;
  UCHAR    Reserved2  :3;
  UCHAR   Reserved3[3];
  UCHAR EndLba[4];
  UCHAR   ReadSpeed[4];
  UCHAR  WriteSpeed[4];
} CDROM_WRITE_SPEED_DESCRIPTOR, *PCDROM_WRITE_SPEED_DESCRIPTOR;
```



## Members

<dl> <dt>

**MixedReadWrite**
</dt> <dd>

The MixedReadWrite (MRW) field corresponds to the MRW bit of the Write Speed Descriptor in the MultiMedia Command Set - 6 (MMC-6) specification. This field indicates that it is suitable for a mixture of streaming read and write requests (overwrite mode). The [**STREAMING\_CONTROL\_REQUEST\_TYPE**](streaming-control-request-type.md) enumeration specifies the type of request.

</dd> <dt>

 **Exact**
</dt> <dd>

The Exact field indicates whether the logical unit can perform the recording operation specified by CDM\_WRITE\_SPEED\_DESCRIPTOR on the whole medium mounted. This field corresponds to the Exact bit of the Write Speed Descriptor.

</dd> <dt>

 **Reserved1**
</dt> <dd>

Reserved fields.

</dd> <dt>

 **WriteRotationControl**
</dt> <dd>

The WriteRotationControl (WRC) field specifies the type of the rotation control for the medium.

</dd> <dt>

 **Reserved2**
</dt> <dd>

Reserved fields.

</dd> <dt>

 **Reserved3**
</dt> <dd>

Reserved fields.

</dd> <dt>

**EndLba**
</dt> <dd>

The End Logical Block Address (EndLBA) field indicates the capacity of the medium if a medium is mounted. It corresponds to the EndLBA field of the Write Speed Descriptor.

</dd> <dt>

 **ReadSpeed**
</dt> <dd>

The ReadSpeed field indicates the lowest read performance data of all blocks (in kilobytes per second).

</dd> <dt>

 **WriteSpeed**
</dt> <dd>

The WriteSpeed field indicates the lowest write performance data of all blocks (in kilobytes per second).

</dd> </dl>

## Remarks

The fields in the **CDROM\_WRITE\_SPEED\_DESCRIPTOR** structure correspond to the fields defined in the MultiMedia Command Set - 6 (MMC-6) specification for the Write Speed Descriptor.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md)
</dt> <dt>

[**STREAMING\_CONTROL\_REQUEST\_TYPE**](streaming-control-request-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_WRITE_SPEED_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






