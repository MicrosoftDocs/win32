---
title: STARTIO\_PERFORMANCE\_PARAMETERS structure
description: The STARTIO\_PERFORMANCE\_PARAMETERS structure describes the performance parameters that are returned to the miniport driver by the StorPortGetStartIoPerfParams routine.
ms.assetid: '984a8584-ebdd-4e93-868b-1537a3615c1b'
keywords: ["STARTIO_PERFORMANCE_PARAMETERS structure Storage Devices", "PSTARTIO_PERFORMANCE_PARAMETERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STARTIO_PERFORMANCE_PARAMETERS
api_location:
- storport.h
api_type:
- HeaderDef
---

# STARTIO\_PERFORMANCE\_PARAMETERS structure

The **STARTIO\_PERFORMANCE\_PARAMETERS** structure describes the performance parameters that are returned to the miniport driver by the [**StorPortGetStartIoPerfParams**](storportgetstartioperfparams.md) routine.

## Syntax


```C++
typedef struct _STARTIO_PERFORMANCE_PARAMETERS {
  ULONG Version;
  ULONG Size;
  ULONG MessageNumber;
  ULONG ChannelNumber;
} STARTIO_PERFORMANCE_PARAMETERS, *PSTARTIO_PERFORMANCE_PARAMETERS;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number of the structure. This member is valid starting with Windows 8.

</dd> <dt>

**Size**
</dt> <dd>

The size of the structure.

</dd> <dt>

**MessageNumber**
</dt> <dd>

The offset in the device's MSI-X table for the optimal MSI-X message with which to interrupt. If the device does not support MSI-X messages, this member will be zero.

</dd> <dt>

**ChannelNumber**
</dt> <dd>

Denotes the concurrent channel in which Storport is passing the I/O. If the miniport driver did not set up concurrent channels, this member will be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortGetStartIoPerfParams**](storportgetstartioperfparams.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STARTIO_PERFORMANCE_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






