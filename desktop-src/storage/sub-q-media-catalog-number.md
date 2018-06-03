---
title: SUB\_Q\_MEDIA\_CATALOG\_NUMBER structure
description: The SUB\_Q\_MEDIA\_CATALOG\_NUMBER structure contains position information and is used in conjunction with the SUB\_Q\_CHANNEL\_DATA structure.
ms.assetid: 14b0aed7-1602-41a3-bc55-59da40650860
keywords:
- SUB_Q_MEDIA_CATALOG_NUMBER structure Storage Devices
- PSUB_Q_MEDIA_CATALOG_NUMBER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SUB_Q_MEDIA_CATALOG_NUMBER
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SUB\_Q\_MEDIA\_CATALOG\_NUMBER structure

The SUB\_Q\_MEDIA\_CATALOG\_NUMBER structure contains position information and is used in conjunction with the [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md) structure.

## Syntax


```C++
typedef struct _SUB_Q_MEDIA_CATALOG_NUMBER {
  SUB_Q_HEADER Header;
  UCHAR        FormatCode;
  UCHAR        Reserved[3];
  UCHAR        Reserved1  :7;
  UCHAR        Mcval  :1;
  UCHAR        MediaCatalog[15];
} SUB_Q_MEDIA_CATALOG_NUMBER, *PSUB_Q_MEDIA_CATALOG_NUMBER;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Indicates, among other things, the length of the Q subchannel data that was retrieved. See [**SUB\_Q\_HEADER**](sub-q-header.md) for further details.

</dd> <dt>

**FormatCode**
</dt> <dd>

Should have a value of IOCTL\_CDROM\_MEDIA\_CATALOG.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Mcval**
</dt> <dd>

Indicates that the media catalog number (MCN) data is valid if set to 1; set to zero otherwise.

</dd> <dt>

**MediaCatalog**
</dt> <dd>

Contains the catalog number if **Mcval** is set to 1.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_Q\_CHANNEL**](ioctl-cdrom-read-q-channel.md)
</dt> <dt>

[**CDROM\_SUB\_Q\_DATA\_FORMAT**](cdrom-sub-q-data-format.md)
</dt> <dt>

[**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md)
</dt> <dt>

[**SUB\_Q\_HEADER**](sub-q-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SUB_Q_MEDIA_CATALOG_NUMBER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






