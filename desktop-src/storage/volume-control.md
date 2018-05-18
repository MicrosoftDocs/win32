---
title: VOLUME\_CONTROL structure
description: The VOLUME\_CONTROL structure is used in conjunction with the IOCTL\_CDROM\_GET\_VOLUME request to retrieve volume values for up to four audio ports.
ms.assetid: '47512360-60fe-43f2-8052-58ca78e36d86'
keywords: ["VOLUME_CONTROL structure Storage Devices", "PVOLUME_CONTROL structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- VOLUME_CONTROL
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# VOLUME\_CONTROL structure

The VOLUME\_CONTROL structure is used in conjunction with the [**IOCTL\_CDROM\_GET\_VOLUME**](ioctl-cdrom-get-volume.md) request to retrieve volume values for up to four audio ports.

## Syntax


```C++
typedef struct _VOLUME_CONTROL {
  UCHAR PortVolume[4];
} VOLUME_CONTROL, *PVOLUME_CONTROL;
```



## Members

<dl> <dt>

**PortVolume**
</dt> <dd>

Pointer to an array of volume values, one for each of the ports, with a maximum of four ports.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_VOLUME**](ioctl-cdrom-get-volume.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VOLUME_CONTROL%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






