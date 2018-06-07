---
title: CDROM\_STREAMING\_CONTROL structure
description: The CDROM\_STREAMING\_CONTROL structure is used as an input parameter to the IOCTL\_CDROM\_ENABLE\_STREAMING IOCTL.
ms.assetid: 71D4008C-1F04-408B-93DF-DDE6FD352701
keywords:
- CDROM_STREAMING_CONTROL structure Storage Devices
- PCDROM_STREAMING_CONTROL structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_STREAMING_CONTROL
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CDROM\_STREAMING\_CONTROL structure

The **CDROM\_STREAMING\_CONTROL** structure is used as an input parameter to the [**IOCTL\_CDROM\_ENABLE\_STREAMING**](ioctl-cdrom-enable-streaming.md) IOCTL.

## Syntax


```C++
typedef struct _CDROM_STREAMING_CONTROL {
  STREAMING_CONTROL_REQUEST_TYPE    RequestType;
} CDROM_STREAMING_CONTROL, *PCDROM_STREAMING_CONTROL;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

The [**STREAMING\_CONTROL\_REQUEST\_TYPE**](streaming-control-request-type.md) enumeration specifies the type of request.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**STREAMING\_CONTROL\_REQUEST\_TYPE**](streaming-control-request-type.md)
</dt> <dt>

[**IOCTL\_CDROM\_ENABLE\_STREAMING**](ioctl-cdrom-enable-streaming.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_STREAMING_CONTROL%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






