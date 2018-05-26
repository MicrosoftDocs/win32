---
title: DEVICE\_DATA\_SET\_RANGE structure
description: The DEVICE\_DATA\_SET\_RANGE structure specifies a block of data set ranges for the attributes for a device.
ms.assetid: 9f610927-d8d0-44c5-8a66-0204953c1859
keywords:
- DEVICE_DATA_SET_RANGE structure Storage Devices
- PDEVICE_DATA_SET_RANGE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_DATA_SET_RANGE
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DEVICE\_DATA\_SET\_RANGE structure

The **DEVICE\_DATA\_SET\_RANGE** structure specifies a block of data set ranges for the attributes for a device.

The block of data set ranges is specified in the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure that is contained in the system buffer of an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

## Syntax


```C++
typedef struct _DEVICE_DATA_SET_RANGE {
  LONGLONG  StartingOffset;
  ULONGLONG LengthInBytes;
} DEVICE_DATA_SET_RANGE, *PDEVICE_DATA_SET_RANGE;
```



## Members

<dl> <dt>

**StartingOffset**
</dt> <dd>

Contains the starting offset, in bytes, of the data set range. The offset value must be block aligned.

</dd> <dt>

**LengthInBytes**
</dt> <dd>

Contains the length, in bytes, of the data set range. The length value must be block aligned.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_DATA_SET_RANGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






