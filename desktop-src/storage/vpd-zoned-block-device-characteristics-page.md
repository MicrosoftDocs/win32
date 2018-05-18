---
title: VPD\_ZONED\_BLOCK\_DEVICE\_CHARACTERISTICS\_PAGE structure
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: '9b1f83fd-e367-4b0d-8f93-24f35d9a5fd8'
keywords: ["VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure Storage Devices", "PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
api_location:
- scsi.h
api_type:
- HeaderDef
---

# VPD\_ZONED\_BLOCK\_DEVICE\_CHARACTERISTICS\_PAGE structure

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef struct _VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE {
  UCHAR  DeviceType  :5;
  UCHAR  DeviceTypeQualifier  :3;
  UCHAR  PageCode;
  UCHAR  PageLength[2];
  UCHAR  URSWRZ  :1;
  UCHAR  Reserved1  :7;
  UCHAR  Reserved2[3];
  UCHAR  OptimalNumberOfOpenSequentialWritePreferredZone[4];
  UCHAR  OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone[4];
  UCHAR  MaxNumberOfOpenSequentialWriteRequiredZone[4];
  UCHAR  Reserved3[44];
} VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, *PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE;
```



## Members

<dl> <dt>

**DeviceType**
</dt> <dd>

N/A

</dd> <dt>

**DeviceTypeQualifier**
</dt> <dd>

N/A

</dd> <dt>

**PageCode**
</dt> <dd>

N/A

</dd> <dt>

**PageLength**
</dt> <dd>

N/A

</dd> <dt>

**URSWRZ**
</dt> <dd>

N/A

</dd> <dt>

**Reserved1**
</dt> <dd>

N/A

</dd> <dt>

**Reserved2**
</dt> <dd>

N/A

</dd> <dt>

**OptimalNumberOfOpenSequentialWritePreferredZone**
</dt> <dd>

N/A

</dd> <dt>

**OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone**
</dt> <dd>

N/A

</dd> <dt>

**MaxNumberOfOpenSequentialWriteRequiredZone**
</dt> <dd>

N/A

</dd> <dt>

**Reserved3**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





