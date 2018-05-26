---
title: TRACK\_DATA structure
description: Track descriptor is used in conjunction with CDROM\_TOC and CDROM\_TOC\_SESSION\_DATA.
ms.assetid: f412ff4e-6c65-40f8-9747-dc5059e588f6
keywords:
- TRACK_DATA structure Storage Devices
- PTRACK_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- TRACK_DATA
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TRACK\_DATA structure

Track descriptor is used in conjunction with [**CDROM\_TOC**](cdrom-toc.md) and [**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md).

## Syntax


```C++
typedef struct _TRACK_DATA {
  UCHAR Reserved;
  UCHAR Control  :4;
  UCHAR Adr  :4;
  UCHAR TrackNumber;
  UCHAR Reserved1;
  UCHAR Address[4];
} TRACK_DATA, *PTRACK_DATA;
```



## Members

<dl> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Control**
</dt> <dd>

Indicates the attributes of the track. For information about the permissible values for this member, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

</dd> <dt>

**Adr**
</dt> <dd>

Indicates the type of information encoded in the Q subchannel of the track where this table of contents entry was found. For information about the permissible values for this member, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

</dd> <dt>

**TrackNumber**
</dt> <dd>

Indicates the number of the track.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Address**
</dt> <dd>

Indicates the starting address of the track.

</dd> </dl>

## Remarks

This structure contains table of contents information for a track.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_TOC**](cdrom-toc.md)
</dt> <dt>

[**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TRACK_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






