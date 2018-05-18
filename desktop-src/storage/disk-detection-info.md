---
title: DISK\_DETECTION\_INFO structure
description: The DISK\_DETECTION\_INFO structure contains the detected drive parameters that are supplied by an x86 PC BIOS on boot.
ms.assetid: '67a508cf-79c4-4c86-9ad3-fa7cca99cf5f'
keywords: ["DISK_DETECTION_INFO structure Storage Devices", "PDISK_DETECTION_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_DETECTION_INFO
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_DETECTION\_INFO structure

The DISK\_DETECTION\_INFO structure contains the detected drive parameters that are supplied by an x86 PC BIOS on boot.

## Syntax


```C++
typedef struct _DISK_DETECTION_INFO {
  ULONG          SizeOfDetectInfo;
  DETECTION_TYPE DetectionType;
  union {
    struct {
      DISK_INT13_INFO    Int13;
      DISK_EX_INT13_INFO ExInt13;
    };
  };
} DISK_DETECTION_INFO, *PDISK_DETECTION_INFO;
```



## Members

<dl> <dt>

**SizeOfDetectInfo**
</dt> <dd>

Contains the quantity, in bytes, of retrieved detect information.

</dd> <dt>

**DetectionType**
</dt> <dd>

Indicates one of three possible detection types:

1.  **DetectNone**

2.  **DetectInt13**

3.  **DetectExInt13**

See the structure [**DETECTION\_TYPE**](detection-type.md) for further information.

</dd> <dt>

( *unnamed struct* )
</dt> <dd>

Contains the quantity, in bytes, of retrieved detect information.

<dl> <dt>

**Int13**
</dt> <dd>

Contains [**DISK\_INT13\_INFO**](disk-int13-info.md) structure with the disk parameters for INT 13 type partitions. This member is used if **DetectionType** == **DetectInt13**.

</dd> <dt>

**ExInt13**
</dt> <dd>

Contains a [**DISK\_EX\_INT13\_INFO**](disk-ex-int13-info.md) structure with the disk parameters for extended INT 13 type partitions. This member is used if **DetectionType** == **DetectExInt13**.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md)
</dt> <dt>

[**DISK\_INT13\_INFO**](disk-int13-info.md)
</dt> <dt>

[**DISK\_EX\_INT13\_INFO**](disk-ex-int13-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_DETECTION_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






