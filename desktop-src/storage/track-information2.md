---
title: TRACK\_INFORMATION2 structure
description: The TRACK\_INFORMATION2 structure is used to report track information.
ms.assetid: '2fea2f8a-eb55-409c-80d2-c3f49ab6bfdf'
keywords: ["TRACK_INFORMATION2 structure Storage Devices", "PTRACK_INFORMATION2 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TRACK_INFORMATION2
api_location:
- scsi.h
api_type:
- HeaderDef
---

# TRACK\_INFORMATION2 structure

The TRACK\_INFORMATION2 structure is used to report track information.

## Syntax


```C++
typedef struct _TRACK_INFORMATION2 {
  UCHAR Length[2];
  UCHAR TrackNumberLsb;
  UCHAR SessionNumberLsb;
  UCHAR Reserved4;
  UCHAR TrackMode  :4;
  UCHAR Copy  :1;
  UCHAR Damage  :1;
  UCHAR Reserved5  :2;
  UCHAR DataMode  :4;
  UCHAR FixedPacket  :1;
  UCHAR Packet  :1;
  UCHAR Blank  :1;
  UCHAR ReservedTrack  :1;
  UCHAR NWA_V  :1;
  UCHAR LRA_V  :1;
  UCHAR Reserved6  :6;
  UCHAR TrackStartAddress[4];
  UCHAR NextWritableAddress[4];
  UCHAR FreeBlocks[4];
  UCHAR FixedPacketSize[4];
  UCHAR TrackSize[4];
  UCHAR LastRecordedAddress[4];
  UCHAR TrackNumberMsb;
  UCHAR SessionNumberMsb;
  UCHAR Reserved7[2];
} TRACK_INFORMATION2, *PTRACK_INFORMATION2;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

The length, in bytes, of this structure.

</dd> <dt>

**TrackNumberLsb**
</dt> <dd>

The least significant byte of the track number.

</dd> <dt>

**SessionNumberLsb**
</dt> <dd>

The least significant byte of the session number.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved.

</dd> <dt>

**TrackMode**
</dt> <dd>

The track mode. See the *SCSI-3 Multi-Media* specification for an explanation of meaning of this member.

</dd> <dt>

**Copy**
</dt> <dd>

The copy bit indicates whether the track is a copy or not. If this bit is 1, the track is a copy. If it is 0, the track is not a copy.

</dd> <dt>

**Damage**
</dt> <dd>

The damage bit indicates, together with the NWA\_V bit, whether a write to the media is complete or not, and what sort of methods the CD-ROM class driver can use to complete the write. See the *SCSI-3 Multi-Media* specification for an explanation of how to interpret the values in the **Damage** and **NWA\_V** members.

</dd> <dt>

**Reserved5**
</dt> <dd>

Reserved.

</dd> <dt>

**DataMode**
</dt> <dd>

The data mode. This member can have any of the following values:



|                      |                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| **Value**<br/> | **Meaning**<br/>                                                                                    |
| 0x1<br/>       | The track uses data mode 1 (ISO/IEC 10149)<br/>                                                     |
| 0x2<br/>       | The track uses data mode 2 (ISO/IEC 10149 or CD-ROM XA)<br/>                                        |
| 0xf<br/>       | There is no track descriptor block, and therefore the data block type of the track is unknown.<br/> |



 

</dd> <dt>

**FixedPacket**
</dt> <dd>

The fixed packet bit indicates, under some circumstances, when set to 1, that write operations to the track must must use fixed packets. For a complete explanation of the meaning of this bit, see the *SCSI Multimedia Commands - 3 (MMC-3)* specification.

</dd> <dt>

**Packet**
</dt> <dd>

The fixed packet bit indicates, under some circumstances, when set to 1, that write operations to the track must must use fixed packets. For a complete explanation of the meaning of this bit, see the *SCSI Multimedia Commands - 3 (MMC-3)* specification.

</dd> <dt>

**Blank**
</dt> <dd>

The blank bit, when set to 1, indicates that the track contains no written data and last recorded address field is invalid. For a complete explanation of the meaning of this bit, see the *SCSI Multimedia Commands - 3 (MMC-3)* specification.

</dd> <dt>

**ReservedTrack**
</dt> <dd>

The reserved track bit, when 1, indicates that the track is reserved.

</dd> <dt>

**NWA\_V**
</dt> <dd>

A boolean value that indicates, when 1, that the value in **NextWritableAddress** is valid. If 0, the value in **NextWritableAddress** is invalid.

</dd> <dt>

**LRA\_V**
</dt> <dd>

A boolean value that indicates whether the **LastRecordedAddress** member is valid or not. If **LRA\_V** is 1, the **LastRecordedAddress** member is valid. If 0, the **LastRecordedAddress** member is not valid.

</dd> <dt>

**Reserved6**
</dt> <dd>

Reserved.

</dd> <dt>

**TrackStartAddress**
</dt> <dd>

The starting address of the specified track.

</dd> <dt>

**NextWritableAddress**
</dt> <dd>

The logical block address of the next writable user block in the track specified by the track number (**TrackNumberLsb** and **TrackNumberMsb**).

</dd> <dt>

**FreeBlocks**
</dt> <dd>

The maximum number of user data blocks that are available for recording in the track.

</dd> <dt>

**FixedPacketSize**
</dt> <dd>

The blocking factor. This value The fixed packet size is valid only when the Packet and the FP bits are both set to one.

</dd> <dt>

**TrackSize**
</dt> <dd>

Track Size is the number of user data blocks in the track.

</dd> <dt>

**LastRecordedAddress**
</dt> <dd></dd> <dt>

**TrackNumberMsb**
</dt> <dd>

The most significant byte of the track number.

</dd> <dt>

**SessionNumberMsb**
</dt> <dd>

The most significant byte of the session number.

</dd> <dt>

**Reserved7**
</dt> <dd>

Reserved7

</dd> </dl>

## Requirements



|                   |                                                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TRACK_INFORMATION2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





