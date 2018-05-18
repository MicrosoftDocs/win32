---
title: DVD\_STRUCTURE\_FORMAT enumeration
description: The DVD\_STRUCTURE\_FORMAT enumeration type is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request and the DVD\_READ\_STRUCTURE structure to retrieve a DVD descriptor.
ms.assetid: '0f3ca59b-f7e9-4bd7-a652-f7f0a6075d80'
keywords: ["DVD_STRUCTURE_FORMAT enumeration Storage Devices", "PDVD_STRUCTURE_FORMAT enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DVD_STRUCTURE_FORMAT
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# DVD\_STRUCTURE\_FORMAT enumeration

The DVD\_STRUCTURE\_FORMAT enumeration type is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request and the [**DVD\_READ\_STRUCTURE**](dvd-read-structure.md) structure to retrieve a DVD descriptor.

## Syntax


```C++
typedef enum DVD_STRUCTURE_FORMAT { 
  DvdPhysicalDescriptor      = 0,
  DvdCopyrightDescriptor     = 1,
  DvdDiskKeyDescriptor       = 2,
  DvdBCADescriptor           = 3,
  DvdManufacturerDescriptor  = 4,
  DvdMaxDescriptor           = 5
} DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT;
```



## Constants

<dl> <dt>

<span id="DvdPhysicalDescriptor"></span><span id="dvdphysicaldescriptor"></span><span id="DVDPHYSICALDESCRIPTOR"></span>**DvdPhysicalDescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD physical descriptor.

</dd> <dt>

<span id="DvdCopyrightDescriptor"></span><span id="dvdcopyrightdescriptor"></span><span id="DVDCOPYRIGHTDESCRIPTOR"></span>**DvdCopyrightDescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD copyright descriptor containing copyright information from the DVD lead-in area.

</dd> <dt>

<span id="DvdDiskKeyDescriptor"></span><span id="dvddiskkeydescriptor"></span><span id="DVDDISKKEYDESCRIPTOR"></span>**DvdDiskKeyDescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD key descriptor containing the disc key obfuscated using the bus key.

</dd> <dt>

<span id="DvdBCADescriptor"></span><span id="dvdbcadescriptor"></span><span id="DVDBCADESCRIPTOR"></span>**DvdBCADescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD burst cutting area (BCA) descriptor.

</dd> <dt>

<span id="DvdManufacturerDescriptor"></span><span id="dvdmanufacturerdescriptor"></span><span id="DVDMANUFACTURERDESCRIPTOR"></span>**DvdManufacturerDescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD manufacturer descriptor containing disc manufacturing information from the DVD lead-in area.

</dd> <dt>

<span id="DvdMaxDescriptor"></span><span id="dvdmaxdescriptor"></span><span id="DVDMAXDESCRIPTOR"></span>**DvdMaxDescriptor**
</dt> <dd>

Indicates that caller is requesting a DVD max descriptor.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_READ\_STRUCTURE**](dvd-read-structure.md)
</dt> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_STRUCTURE_FORMAT%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






