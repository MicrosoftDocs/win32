---
title: TAPE\_SET\_DRIVE\_PARAMETERS structure
description: The TAPE\_SET\_DRIVE\_PARAMETERS structure is used in conjunction with the IOCTL\_TAPE\_SET\_DRIVE\_PARAMS request to adjust the configurable parameters of a tape drive.
ms.assetid: '87317972-b0df-4691-a9a5-bd0bbc150e53'
keywords: ["TAPE_SET_DRIVE_PARAMETERS structure Storage Devices", "PTAPE_SET_DRIVE_PARAMETERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_SET_DRIVE_PARAMETERS
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_SET\_DRIVE\_PARAMETERS structure

The TAPE\_SET\_DRIVE\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_DRIVE\_PARAMS**](ioctl-tape-set-drive-params.md) request to adjust the configurable parameters of a tape drive.

## Syntax


```C++
typedef struct _TAPE_SET_DRIVE_PARAMETERS {
  BOOLEAN ECC;
  BOOLEAN Compression;
  BOOLEAN DataPadding;
  BOOLEAN ReportSetmarks;
  ULONG   EOTWarningZoneSize;
} TAPE_SET_DRIVE_PARAMETERS, *PTAPE_SET_DRIVE_PARAMETERS;
```



## Members

<dl> <dt>

**ECC**
</dt> <dd>

When set to **TRUE**, instructs the device to use hardware error correction. When **FALSE**, the device does not use hardware error correction.

</dd> <dt>

**Compression**
</dt> <dd>

When set to **TRUE**, instructs the device to compress data prior to writing it. If a drive must be at beginning of partition before it can set compression (TAPE\_DRIVE\_SET\_CMP\_BOP\_ONLY), the caller is responsible for positioning the drive before attempting to set compression. When **FALSE**, the device does not compress data prior to writing it.

</dd> <dt>

**DataPadding**
</dt> <dd>

When set to **TRUE**, instructs the device to pad data with zeros. This is to keep the tape streaming until data is ready. When **FALSE**, the device does not pad data with zeros.

</dd> <dt>

**ReportSetmarks**
</dt> <dd>

When set to **TRUE**, instructs the device to report setmarks encountered during read or space operations. When **FALSE**, the device does not report setmarks encountered during read or space operations.

</dd> <dt>

**EOTWarningZoneSize**
</dt> <dd>

Indicates the size in bytes of the early warning zone toward the end of the tape in which the drive returns a check condition when it enters the zone.

</dd> </dl>

## Remarks

The miniclass driver can ignore parameters its device does not support. The calling application is responsible for determining whether a device supports a particular feature before attempting to set it.

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_SET\_DRIVE\_PARAMS**](ioctl-tape-set-drive-params.md)
</dt> <dt>

[**TapeMiniSetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567952)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_SET_DRIVE_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






