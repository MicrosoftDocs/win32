---
title: SUB\_Q\_CURRENT\_POSITION structure
description: The SUB\_Q\_CURRENT\_POSITION structure contains position information and is used in conjunction with SUB\_Q\_CHANNEL\_DATA.
ms.assetid: '816baec4-3dd0-4025-ba34-035bf6f241d3'
keywords: ["SUB_Q_CURRENT_POSITION structure Storage Devices", "PSUB_Q_CURRENT_POSITION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SUB_Q_CURRENT_POSITION
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# SUB\_Q\_CURRENT\_POSITION structure

The SUB\_Q\_CURRENT\_POSITION structure contains position information and is used in conjunction with [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md).

## Syntax


```C++
typedef struct _SUB_Q_CURRENT_POSITION {
  SUB_Q_HEADER Header;
  UCHAR        FormatCode;
  UCHAR        Control  :4;
  UCHAR        ADR  :4;
  UCHAR        TrackNumber;
  UCHAR        IndexNumber;
  UCHAR        AbsoluteAddress[4];
  UCHAR        TrackRelativeAddress[4];
} SUB_Q_CURRENT_POSITION, *PSUB_Q_CURRENT_POSITION;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Indicates, among other things, the length of the Q subchannel data that was retrieved. See [**SUB\_Q\_HEADER**](sub-q-header.md) for more details.

</dd> <dt>

**FormatCode**
</dt> <dd>

Should have a value of IOCTL\_CDROM\_CURRENT\_POSITION.

</dd> <dt>

**Control**
</dt> <dd>

Defines various types of information within the table of contents lead-in area. For more information about the permissible values for this member, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

</dd> <dt>

**ADR**
</dt> <dd>

Indicates the type of information encoded in the Q subchannel of the block. For information about the permissible values for this member, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

</dd> <dt>

**TrackNumber**
</dt> <dd>

Contains the current track number.

</dd> <dt>

**IndexNumber**
</dt> <dd>

Contains the current index number.

</dd> <dt>

**AbsoluteAddress**
</dt> <dd>

Gives the current location relative to the logical beginning of the media. The bytes in this array are arranged in big-endian order. **AbsoluteAddress**\[0\] contains the most significant byte, and **AbsoluteAddress**\[3\] contains the least significant byte.

</dd> <dt>

**TrackRelativeAddress**
</dt> <dd>

Gives the current location relative to the logical beginning of the current track. The bytes in this array are arranged in big-endian order. **TrackRelativeAddress**\[0\] contains the most significant byte, and **TrackRelativeAddress**\[3\] contains the least significant byte.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SUB_Q_CURRENT_POSITION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






