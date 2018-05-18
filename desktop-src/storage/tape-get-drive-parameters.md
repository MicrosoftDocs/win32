---
title: TAPE\_GET\_DRIVE\_PARAMETERS structure
description: The TAPE\_GET\_DRIVE\_PARAMETERS structure is used in conjunction with the IOCTL\_TAPE\_GET\_DRIVE\_PARAMS request to retrieve information about capabilities of the tape drive.
ms.assetid: '2b1b196f-f012-4136-983e-8c8192bdbd2f'
keywords: ["TAPE_GET_DRIVE_PARAMETERS structure Storage Devices", "PTAPE_GET_DRIVE_PARAMETERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_GET_DRIVE_PARAMETERS
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_GET\_DRIVE\_PARAMETERS structure

The TAPE\_GET\_DRIVE\_PARAMETERS structure is used in conjunction with the [**IOCTL\_TAPE\_GET\_DRIVE\_PARAMS**](ioctl-tape-get-drive-params.md) request to retrieve information about capabilities of the tape drive.

## Syntax


```C++
typedef struct _TAPE_GET_DRIVE_PARAMETERS {
  BOOLEAN ECC;
  BOOLEAN Compression;
  BOOLEAN DataPadding;
  BOOLEAN ReportSetmarks;
  ULONG   DefaultBlockSize;
  ULONG   MaximumBlockSize;
  ULONG   MinimumBlockSize;
  ULONG   MaximumPartitionCount;
  ULONG   FeaturesLow;
  ULONG   FeaturesHigh;
  ULONG   EOTWarningZoneSize;
} TAPE_GET_DRIVE_PARAMETERS, *PTAPE_GET_DRIVE_PARAMETERS;
```



## Members

<dl> <dt>

**ECC**
</dt> <dd>

When set to **TRUE**, indicates that the device uses hardware error correction.

</dd> <dt>

**Compression**
</dt> <dd>

When set to **TRUE**, indicates that compression is enabled on a device that supports it. When compression is enabled, the device compresses data prior to writing it. When set to **FALSE**, compression is not enabled on the device.

</dd> <dt>

**DataPadding**
</dt> <dd>

When set to **TRUE**, indicates that data padding is enabled on a device that supports it. When padding is enabled, the device pads data with zeros to keep the tape streaming until data is ready. When set to **FALSE**, data padding is not enabled.

</dd> <dt>

**ReportSetmarks**
</dt> <dd>

When set to **TRUE**, indicates that reporting setmarks is enabled on a device that supports it. The device reports setmarks encountered during read or space operations. When set to **FALSE**, reporting setmarks is not enabled.

</dd> <dt>

**DefaultBlockSize**
</dt> <dd>

Indicates the default block size, in bytes.

</dd> <dt>

**MaximumBlockSize**
</dt> <dd>

Indicates the maximum block size, in bytes, of either the tape device or the underlying host bus adapter (HBA), whichever is smaller.

</dd> <dt>

**MinimumBlockSize**
</dt> <dd>

Indicates the minimum block size, in bytes.

</dd> <dt>

**MaximumPartitionCount**
</dt> <dd>

Indicates the maximum number of partitions the device supports.

</dd> <dt>

**FeaturesLow**
</dt> <dd>

Indicates the features supported by this drive. The miniport driver sets TAPE\_DRIVE\_*XXX* flags for features supported by the drive and clears flags for features not supported. Callers can use the TAPE\_DRIVE\_*XXX* masks defined in *minitape.h* to determine whether a drive supports a particular feature. The masks available are as follows:



| Mask                                        | Meaning                                                                                                                    |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| TAPE\_DRIVE\_CLEAN\_REQUESTS<br/>     | The device can report whether it requires cleaning.<br/>                                                             |
| TAPE\_DRIVE\_COMPRESSION<br/>         | The device supports hardware data compression.<br/>                                                                  |
| TAPE\_DRIVE\_ECC<br/>                 | The device supports hardware error correction.<br/>                                                                  |
| TAPE\_DRIVE\_EJECT\_MEDIA<br/>        | The device ejects the media. <br/>                                                                                   |
| TAPE\_DRIVE\_EOT\_WZ\_SIZE<br/>       | The device can report the end of zone warning size. <br/>                                                            |
| TAPE\_DRIVE\_ERASE\_BOP\_ONLY<br/>    | The device performs the erase operation from the beginning-of-partition marker only.<br/>                            |
| TAPE\_DRIVE\_ERASE\_IMMEDIATE<br/>    | The device performs an immediate erase operation ?? that is, it returns when the erase operation begins.<br/>        |
| TAPE\_DRIVE\_ERASE\_LONG<br/>         | The device performs a long erase operation.<br/>                                                                     |
| TAPE\_DRIVE\_ERASE\_SHORT<br/>        | The device performs a short erase operation.<br/>                                                                    |
| TAPE\_DRIVE\_FIXED<br/>               | The device creates fixed data partitions.<br/>                                                                       |
| TAPE\_DRIVE\_FIXED\_BLOCK<br/>        | The device supports fixed-length block mode.<br/>                                                                    |
| TAPE\_DRIVE\_INITIATOR<br/>           | The device creates initiator-defined partitions.<br/>                                                                |
| TAPE\_DRIVE\_GET\_ABSOLUTE\_BLK<br/>  | The device provides the current device-specific block address.<br/>                                                  |
| TAPE\_DRIVE\_GET\_LOGICAL\_BLK<br/>   | The device provides the current logical block address (and logical tape partition).<br/>                             |
| TAPE\_DRIVE\_PADDING<br/>             | The device supports data padding.<br/>                                                                               |
| TAPE\_DRIVE\_REPORT\_SMKS<br/>        | The device supports setmark reporting.<br/>                                                                          |
| TAPE\_DRIVE\_RESERVED\_BIT<br/>       | A mask that identifies a reserved bit. Drivers must not set this bit. <br/>                                          |
| TAPE\_DRIVE\_SELECT<br/>              | The device creates select data partitions.<br/>                                                                      |
| TAPE\_DRIVE\_SET\_CMP\_BOP\_ONLY<br/> | The device only allows compression to be enabled when the read/write head is at the beginning of the partition.<br/> |
| TAPE\_DRIVE\_SET\_EOT\_WZ\_SIZE<br/>  | The device supports setting the end-of-medium warning size.<br/>                                                     |
| TAPE\_DRIVE\_TAPE\_CAPACITY<br/>      | The device returns the maximum capacity of the tape.<br/>                                                            |
| TAPE\_DRIVE\_TAPE\_REMAINING<br/>     | The device returns the remaining capacity of the tape.<br/>                                                          |
| TAPE\_DRIVE\_VARIABLE\_BLOCK<br/>     | The device supports variable-length block mode.<br/>                                                                 |
| TAPE\_DRIVE\_WRITE\_PROTECT<br/>      | The device returns an error if the tape is write-enabled or write-protected.<br/>                                    |



 

</dd> <dt>

**FeaturesHigh**
</dt> <dd>

Indicates the additional features supported by this drive if TAPE\_DRIVE\_HIGH\_FEATURES is set in **FeaturesLow**. The miniport driver sets TAPE\_DRIVE\_*XXX* flags for features supported by the drive and clears flags for features not supported. Callers can use the TAPE\_DRIVE\_*XXX* masks defined in *minitape.h* to determine whether a drive supports a particular feature.



| Mask                                       | Meaning                                                                                                                            |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| TAPE\_DRIVE\_ABS\_BLK\_IMMED<br/>    | The device moves the tape to a device-specific block address and returns as soon as the move begins.<br/>                    |
| TAPE\_DRIVE\_ABSOLUTE\_BLK<br/>      | The device moves the tape to a device specific block address.<br/>                                                           |
| TAPE\_DRIVE\_END\_OF\_DATA<br/>      | The device moves the tape to the end-of-data marker in a partition.<br/>                                                     |
| TAPE\_DRIVE\_FILEMARKS<br/>          | The device moves the tape forward (or backward) a specified number of filemarks.<br/>                                        |
| TAPE\_DRIVE\_FORMAT<br/>             | The device can format the media. <br/>                                                                                       |
| TAPE\_DRIVE\_FORMAT\_IMMEDIATE<br/>  | The device can format the media as an immediate command.<br/>                                                                |
| TAPE\_DRIVE\_HIGH\_FEATURES<br/>     | A bitmask that indicates those bits which correspond to high features. <br/>                                                 |
| TAPE\_DRIVE\_LOAD\_UNLOAD<br/>       | The device enables and disables the device for further operations.<br/>                                                      |
| TAPE\_DRIVE\_LOAD\_UNLD\_IMMED<br/>  | The device supports immediate load and unload operations.<br/>                                                               |
| TAPE\_DRIVE\_LOCK\_UNLOCK<br/>       | The device enables and disables the tape ejection mechanism.<br/>                                                            |
| TAPE\_DRIVE\_LOCK\_UNLK\_IMMED<br/>  | The device supports immediate lock and unlock operations.<br/>                                                               |
| TAPE\_DRIVE\_LOG\_BLK\_IMMED<br/>    | The device moves the tape to a logical block address in a partition and returns as soon as the move begins.<br/>             |
| TAPE\_DRIVE\_LOGICAL\_BLK<br/>       | The device moves the tape to a logical block address in a partition.<br/>                                                    |
| TAPE\_DRIVE\_RELATIVE\_BLKS<br/>     | The device moves the tape forward (or backward) a specified number of blocks.<br/>                                           |
| TAPE\_DRIVE\_REVERSE\_POSITION<br/>  | The device moves the tape backward over blocks, filemarks, or setmarks.<br/>                                                 |
| TAPE\_DRIVE\_REWIND\_IMMEDIATE<br/>  | The device supports immediate rewind operation.<br/>                                                                         |
| TAPE\_DRIVE\_SEQUENTIAL\_FMKS<br/>   | The device moves the tape forward (or backward) to the first occurrence of a specified number of consecutive filemarks.<br/> |
| TAPE\_DRIVE\_SEQUENTIAL\_SMKS<br/>   | The device moves the tape forward (or backward) to the first occurrence of a specified number of consecutive setmarks.<br/>  |
| TAPE\_DRIVE\_SET\_BLOCK\_SIZE<br/>   | The device supports setting the size of a fixed-length logical block or setting the variable-length block mode.<br/>         |
| TAPE\_DRIVE\_SET\_COMPRESSION<br/>   | The device enables and disables hardware data compression.<br/>                                                              |
| TAPE\_DRIVE\_SET\_ECC<br/>           | The device enables and disables hardware error correction.<br/>                                                              |
| TAPE\_DRIVE\_SET\_PADDING<br/>       | The device enables and disables data padding.<br/>                                                                           |
| TAPE\_DRIVE\_SET\_REPORT\_SMKS<br/>  | The device enables and disables the reporting of setmarks.<br/>                                                              |
| TAPE\_DRIVE\_SETMARKS<br/>           | The device moves the tape forward (or reverse) a specified number of setmarks.<br/>                                          |
| TAPE\_DRIVE\_SPACE\_IMMEDIATE<br/>   | The device supports immediate spacing.<br/>                                                                                  |
| TAPE\_DRIVE\_TENSION<br/>            | The device supports tape tensioning.<br/>                                                                                    |
| TAPE\_DRIVE\_TENSION\_IMMED<br/>     | The device supports immediate tape tensioning.<br/>                                                                          |
| TAPE\_DRIVE\_WRITE\_FILEMARKS<br/>   | The device writes filemarks.<br/>                                                                                            |
| TAPE\_DRIVE\_WRITE\_LONG\_FMKS<br/>  | The device writes long filemarks.<br/>                                                                                       |
| TAPE\_DRIVE\_WRITE\_MARK\_IMMED<br/> | The device supports immediate writing of short and long filemarks.<br/>                                                      |
| TAPE\_DRIVE\_WRITE\_SETMARKS<br/>    | The device writes setmarks.<br/>                                                                                             |
| TAPE\_DRIVE\_WRITE\_SHORT\_FMKS<br/> | The device writes short filemarks.<br/>                                                                                      |



 

</dd> <dt>

**EOTWarningZoneSize**
</dt> <dd>

Indicates the size in bytes of the early warning zone toward the end of the tape. The device returns a check condition when it enters the zone.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_GET\_DRIVE\_PARAMS**](ioctl-tape-get-drive-params.md)
</dt> <dt>

[**TapeMiniGetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567936)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_GET_DRIVE_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






