---
title: DVD\_COPYRIGHT\_DESCRIPTOR structure
description: The DVD\_COPYRIGHT\_DESCRIPTOR structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD copyright descriptor.
ms.assetid: 'e3478867-394b-466c-ad9a-259bedd66669'
keywords: ["DVD_COPYRIGHT_DESCRIPTOR structure Storage Devices", "PDVD_COPYRIGHT_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DVD_COPYRIGHT_DESCRIPTOR
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# DVD\_COPYRIGHT\_DESCRIPTOR structure

The DVD\_COPYRIGHT\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD copyright descriptor.

## Syntax


```C++
typedef struct _DVD_COPYRIGHT_DESCRIPTOR {
  UCHAR  CopyrightProtectionType;
  UCHAR  RegionManagementInformation;
  USHORT Reserved;
} DVD_COPYRIGHT_DESCRIPTOR, *PDVD_COPYRIGHT_DESCRIPTOR;
```



## Members

<dl> <dt>

**CopyrightProtectionType**
</dt> <dd>

Indicates, when set to 1, the presence of data specific to a copyright protection system. A value of zero indicates there is no such data. All other values are reserved.

</dd> <dt>

**RegionManagementInformation**
</dt> <dd>

Indicates in which regions of the world the disc can be played. Each bit represents one of eight regions. If a bit is set, the disc cannot be played in the corresponding region. If a bit is not set, the disc can be played in the corresponding region.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_COPYRIGHT_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






