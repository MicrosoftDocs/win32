---
title: TAPE\_SET\_MEDIA\_PARAMETERS structure
description: The TAPE\_SET\_MEDIA\_PARAMETERS structure is used in conjunction with the IOCTL\_TAPE\_SET\_MEDIA\_PARAMS request to reset the block size of the media in a tape drive.
ms.assetid: f038eb24-71d2-414c-ad7c-06cb1fa24070
keywords:
- TAPE_SET_MEDIA_PARAMETERS structure Storage Devices
- PTAPE_SET_MEDIA_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- TAPE_SET_MEDIA_PARAMETERS
api_location:
- ntddtape.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# TAPE\_SET\_MEDIA\_PARAMETERS structure

The TAPE\_SET\_MEDIA\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_MEDIA\_PARAMS**](ioctl-tape-set-media-params.md) request to reset the block size of the media in a tape drive.

## Syntax


```C++
typedef struct _TAPE_SET_MEDIA_PARAMETERS {
  ULONG BlockSize;
} TAPE_SET_MEDIA_PARAMETERS, *PTAPE_SET_MEDIA_PARAMETERS;
```



## Members

<dl> <dt>

**BlockSize**
</dt> <dd>

Indicates the requested block size, in bytes, or zero for variable block size in a drive that supports it.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_SET\_MEDIA\_PARAMS**](ioctl-tape-set-media-params.md)
</dt> <dt>

[**TapeMiniSetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567953)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_SET_MEDIA_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






