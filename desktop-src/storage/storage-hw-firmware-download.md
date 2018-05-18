---
title: STORAGE\_HW\_FIRMWARE\_DOWNLOAD structure
description: This structure contains a firmware image payload to be downloaded to the target.
ms.assetid: 'EFF4688D-E5B2-4F4C-837D-D536F9244AB6'
keywords: ["STORAGE_HW_FIRMWARE_DOWNLOAD structure Storage Devices", "PSTORAGE_HW_FIRMWARE_DOWNLOAD structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_HW_FIRMWARE_DOWNLOAD
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_HW\_FIRMWARE\_DOWNLOAD structure

This structure contains a firmware image payload to be downloaded to the target.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_DOWNLOAD {
  ULONG     Version;
  ULONG     Size;
  ULONG     Flags;
  UCHAR     Slot;
  UCHAR     Reserved[3];
  ULONGLONG Offset;
  ULONGLONG BufferSize;
  UCHAR     ImageBuffer[ANYSIZE_ARRAY];
} STORAGE_HW_FIRMWARE_DOWNLOAD, *PSTORAGE_HW_FIRMWARE_DOWNLOAD;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to sizeof(STORAGE\_HW\_FIRMWARE\_DOWNLOAD).

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure and the download image buffer.

</dd> <dt>

**Flags**
</dt> <dd>

Flags associated with this download. The following are valid flags that this member can hold.



| Flag                                                | Description                                                                                                                                    |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| STORAGE\_HW\_FIRMWARE\_REQUEST\_FLAG\_CONTROLLER    | Indicates that the target of the request is a controller or adapter, different than the device handle or object itself (e.g. NVMe SSD or HBA). |
| STORAGE\_HW\_FIRMWARE\_REQUEST\_FLAG\_LAST\_SEGMENT | Indicates that the current firmware image segment is the last one.                                                                             |



 

</dd> <dt>

**Slot**
</dt> <dd>

The slot number that the firmware image will be downloaded to.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Offset**
</dt> <dd>

The offset in this buffer of where the Image file begins. This should be aligned to ImagePayloadAlignment from [**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md).

</dd> <dt>

**BufferSize**
</dt> <dd>

The buffer size of the ImageBuffer. This should be a multiple of ImagePayloadAlignment from [**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md).

</dd> <dt>

**ImageBuffer**
</dt> <dd>

The firmware image file.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                 |
| Server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_HW_FIRMWARE_DOWNLOAD%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





