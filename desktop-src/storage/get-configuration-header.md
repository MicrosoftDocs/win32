---
title: GET\_CONFIGURATION\_HEADER structure
description: The GET\_CONFIGURATION\_HEADER structure is used to format the output data retrieved by the IOCTL\_CDROM\_GET\_CONFIGURATION request.
ms.assetid: '8de19f1b-faca-4b27-9287-20edc12f2c83'
keywords: ["GET_CONFIGURATION_HEADER structure Storage Devices", "PGET_CONFIGURATION_HEADER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GET_CONFIGURATION_HEADER
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# GET\_CONFIGURATION\_HEADER structure

The GET\_CONFIGURATION\_HEADER structure is used to format the output data retrieved by the [**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md) request.

## Syntax


```C++
typedef struct _GET_CONFIGURATION_HEADER {
  UCHAR DataLength[4];
  UCHAR Reserved[2];
  UCHAR CurrentProfile[2];
  UCHAR Data[];
} GET_CONFIGURATION_HEADER, *PGET_CONFIGURATION_HEADER;
```



## Members

<dl> <dt>

**DataLength**
</dt> <dd>

Indicates the amount of data, in bytes, that is being returned in the buffer area pointed to by the **Data** member. If the data length is greater than 65,530 bytes, multiple GET CONFIGURATION commands will be required for the Initiator to read all configuration data. The bytes in this array are arranged in big-endian order. **DataLength**\[0\] has the most significant byte, and **DataLength**\[3\] has the least significant byte.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**CurrentProfile**
</dt> <dd>

Contains an enumerator value of type [**FEATURE\_PROFILE\_TYPE**](feature-profile-type.md) that indicates the device's current profile. The bytes in this array are arranged in big-endian order. **CurrentProfile**\[0\] has the most significant byte, and **CurrentProfile**\[3\] has the least significant byte.

</dd> <dt>

**Data**
</dt> <dd>

Contains the feature data, beginning with the [**FEATURE\_HEADER**](feature-header.md).

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md)
</dt> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> <dt>

[**FEATURE\_PROFILE\_TYPE**](feature-profile-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GET_CONFIGURATION_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






