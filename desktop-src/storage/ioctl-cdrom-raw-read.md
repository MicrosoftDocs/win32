---
title: IOCTL\_CDROM\_RAW\_READ control code
description: Reads data from the CD-ROM in raw mode.
ms.assetid: 'b7791cf7-476c-4319-976d-9da3d96b6a76'
keywords: ["IOCTL_CDROM_RAW_READ control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_RAW_READ
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_RAW\_READ control code

Reads data from the CD-ROM in raw mode.

## Input Buffer

If the IOCTL is from user mode, **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**RAW\_READ\_INFO**](raw-read-info.md) structure that specifies the starting disk offset, the sector count, and the track mode (XA or CDDA) for the read. **Parameters.DeviceIoControl.InputBufferLength** specifies the size, in bytes, of the structure, which must be &gt;= **sizeof**(RAW\_READ\_INFO). **Parameters.DeviceIoControl.OutputBufferLength** specifies the size of the buffer to be read, which must be &gt;= **sizeof**(*SectorCount* \* RAW\_SECTOR\_SIZE).

If the IOCTL is from kernel mode, **Parameters.DeviceIoControl.Type3InputBuffer** contains a structure that specifies the starting disk offset, the sector count, and the track mode (XA or CDDA) for the read. **Parameters.DeviceIoControl.OutputBufferLength** specifies the size of the buffer, in bytes, to be read, which must be &gt;= **sizeof**(*SectorCount* \* RAW\_SECTOR\_SIZE).

## Input Buffer Length

See above.

## Output Buffer

The driver writes the requested bytes directly (using DMA or PIO) to the buffer described by the MDL at **Irp-&gt;MdlAddress**.

## Output Buffer Length

Length of an MDL.

## Status block

If the read is successful, the driver sets **Status** to STATUS\_SUCCESS and **Information** to the number of bytes transferred. If the read is not successful, the driver sets **Information** to zero and **Status** to possibly STATUS\_INVALID\_PARAMETER, STATUS\_INSUFFICIENT\_RESOURCES, or STATUS\_INVALID\_DEVICE\_REQUEST.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**RAW\_READ\_INFO**](raw-read-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_RAW_READ%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






